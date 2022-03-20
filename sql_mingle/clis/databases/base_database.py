from abstract_database import AbstractDatabase


class BaseDatabase:
    string_type: str = "string"
    int_type: str = "int"
    float_type: str = "float"
    bool_type: str = "bool"
    date_type: str = "date"
    datetime_type: str = "datetime"
    time_type: str = "time"
    timestamp_type: str = "timestamp"
    json_type: str = "json"
    blob_type: str = "blob"

