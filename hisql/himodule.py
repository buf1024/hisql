import random
import string

from pugsql.compiler import Module
from pugsql.statement import Statement


class HiModule(Module):
    def add_queries(self, *paths, encoding=None):
        new_paths = []
        for p in paths:
            if p is not None:
                self._add_path(p, encoding=encoding)
                new_paths.append(p)

        self.sqlpaths |= set(new_paths)

    def execute(self, sql, result, *multiparams, **params):
        name = ''.join(random.sample(string.ascii_letters + string.digits, 10))
        stmt = Statement(name=name, sql=sql, result=result, doc='', filename=None)
        stmt.set_module(self)
        return stmt(*multiparams, **params)
