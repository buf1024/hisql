
简单修改[pugsql](https://github.com/mcfunley/pugsql) 使其支持直接执行sql。

#### 使用

```python
from hisql import *
from datetime import datetime

q = hisql()
q.connect('mysql+pymysql://bbq:bbq@localhost/bbq')
# 选择9.1号前10个接近10块股票
res = q.execute('select a.code as code, b.name as name, a.close as close '
                'from stock_daily a left join stock_info b on a.code=b.code '
                'where a.trade_date=:trade_date and a.close < 10 order by close desc limit 10',
                Many(), trade_date=datetime(year=2021, month=9, day=1))
data = [d for d in res]
data
```

### 结果
```shell
[{'code': 'sz002820', 'name': '桂发祥', 'close': Decimal('9.9900')},
 {'code': 'sz002556', 'name': '辉隆股份', 'close': Decimal('9.9700')},
 {'code': 'sz002322', 'name': '理工环科', 'close': Decimal('9.9700')},
 {'code': 'sz000920', 'name': '南方汇通', 'close': Decimal('9.9600')},
 {'code': 'sz002545', 'name': '东方铁塔', 'close': Decimal('9.9600')},
 {'code': 'sz002926', 'name': '华西证券', 'close': Decimal('9.9600')},
 {'code': 'sh603056', 'name': '德邦股份', 'close': Decimal('9.9600')},
 {'code': 'sz300434', 'name': '金石亚药', 'close': Decimal('9.9500')},
 {'code': 'sz300437', 'name': '清水源', 'close': Decimal('9.9400')},
 {'code': 'sz300030', 'name': '阳普医疗', 'close': Decimal('9.9300')}]
```

