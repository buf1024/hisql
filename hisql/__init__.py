__version__ = "0.0.1"

from hisql.himodule import HiModule, DataFrame
from pugsql.statement import One, Many, Affected, Scalar, Insert, Raw


def hisql(sqlpath=None, encoding=None):
    return HiModule(sqlpath=sqlpath, encoding=encoding)


__all__ = ['__version__', 'hisql',
           'One', 'Many', 'Affected', 'Scalar', 'Insert', 'Raw', 'DataFrame']
