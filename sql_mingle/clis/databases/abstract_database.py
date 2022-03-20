from abc import ABC, abstractmethod
from typing import List, Dict

class AbstractDatabase(ABC):
    """
    Abstract class for databases
    """
    def __init__(self):
        self.schema: Dict
        self.string_type: List
        self.int_type: List
        self. float_type: List
        self. bool_type: List
        self.date_type: List
        self.datetime_type: List
        self.time_type: List
        self.timestamp_type: List
        self.json_type: List
        self.blob_type: List

    @property
    def internal_column_types(self):
        """
        Get internal column types.
        """
        return [
            'string_type',
            'int_type',
            'float_type',
            'bool_type',
            'date_type',
            'datetime_type',
            'time_type',
            'timestamp_type',
            'json_type',
            'blob_type'
        ]

    @abstractmethod
    def connect(self, **kwargs):
        """
        Connect to the database.
        """
        pass

    @abstractmethod
    def get_schema(self, *args, **kwargs):
        """
        Get the schema of the database.
        """
        pass

    def add_internal_column_type(self, schema_column_type: str):
        """
        Add internal column type.
        """
        for idx in range(len(self.internal_column_types)):
            column_type = self.internal_column_types[idx]
            if schema_column_type in self.__getattribute__(column_type):
                return column_type
