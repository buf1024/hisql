import random
import string
from decimal import Decimal

from pugsql.compiler import Module
from pugsql.statement import Statement, Many
from pugsql.statement import Result

import pandas as pd


class FloatDataFrame(Many):
    def transform(self, r):
        ks = r.keys()
        rs = [{k: float(v) if isinstance(v, Decimal) else v for k, v in zip(ks, row)} for row in r.fetchall()]
        return None if len(rs) == 0 else pd.DataFrame(rs)

    @property
    def display_type(self):
        return 'float_dataframe'


class DataFrame(Many):
    def transform(self, r):
        ks = r.keys()
        rs = [{k: v for k, v in zip(ks, row)} for row in r.fetchall()]
        return None if len(rs) == 0 else pd.DataFrame(rs)

    @property
    def display_type(self):
        return 'dataframe'


class HiModule(Module):
    def add_queries(self, *paths, encoding=None):
        new_paths = []
        for p in paths:
            if p is not None:
                self._add_path(p, encoding=encoding)
                new_paths.append(p)

        self.sqlpaths |= set(new_paths)

    def execute(self, sql, result, *multiparams, **params):
        """

        :param sql:  sql语句
        :param result: 返回的结果类型, One, Many, Insert, Affected, Raw
        :param multiparams: sql参数
        :param params: sql参数
        :return: 根据result返回的结果
        """
        name = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        if not isinstance(result, Result):
            result = result()
        stmt = Statement(name=name, sql=sql, result=result, doc='', filename=None)
        stmt.set_module(self)
        return stmt(*multiparams, **params)

    def prepare(self, *sqls):
        for it in sqls:
            name, sql, result = None, None, None
            if isinstance(it, dict):
                keys = it.keys()
                if 'name' not in keys or 'sql' not in keys or 'result' not in keys:
                    raise ValueError(
                        'sql dict {} - should have the following key: name, sql, result'.format(it))
                name, sql, result = it['name'], it['sql'], it['result']
            if isinstance(it, list) or isinstance(it, tuple):
                if len(it) < 3:
                    raise ValueError(
                        'sql seq {} - should have the at least 3 items'.format(it))
                name, sql, result = it[0], it[1], it[2]

            if name is None:
                raise ValueError(
                    'arguments should be dict/list/tuple'.format(it))

            if not isinstance(result, Result):
                result = result()

            stmt = Statement(name=name, sql=sql, result=result, doc='', filename=None)
            if hasattr(self, name):
                if name not in self._statements:
                    raise ValueError(
                        'Error the function name "{}" is '
                        'reserved. Please choose another name.'.format(s.name))

                raise ValueError('Error a SQL function named {} was '
                                 'already defined in.'.format(name))

            stmt.set_module(self)
            setattr(self, name, stmt)
            self._statements[name] = stmt
