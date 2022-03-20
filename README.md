High level ideas

class for each database
attributes for each data type

example
```python
import abc
import dataclasses

@dataclasses.dataclass
class BaseDatabase(metaclass=abc.ABCMeta):
    string_type = 'str' 
    int_type = 'int'
    
    def to_base(self):
        ...
    
    def from_base(self):
        ...

@dataclasses.dataclass
class BigQuery(BaseDatabase):
    
    string_type = 'STRING'
    int_type = 'INT64' #INT, SMALLINT, INTEGER, BIGINT, TINYINT, and BYTEINT are aliases for INT64.


class Postgres(BaseDatabase):
    string_type = 'VARCHAR'
    int_type = 'INT'
```


covert csv to database
https://github.com/frictionlessdata/tableschema-py