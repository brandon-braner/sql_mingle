from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Database(ABC):
    """
    Abstract class for databases
    """

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

    @abstractmethod
    def connect(self, **kwargs):
        """
        Connect to the database
        """
        pass

    @abstractmethod
    def get_schmea(self):
        """
        Get the schema of the database
        """
        pass

    @abstractmethod
    def from_base(self):
        """
        Get column properties from a base database.
        """
        pass

    @abstractmethod
    def to_base(self):
        """
        Create a base database from column properties
        """
        pass
