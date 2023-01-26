#!/usr/bin/python3
"""Parent class for the Airbnb"""


from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Defines all common attributes and methods"""

    def __init__(self, *args, **kwargs):
        if not kwargs:
            self.id = uuid4()
            self.id = str(self.id)
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            for key, value in kwargs.items():
                format = "%Y-%m-%dT%H:%M:%S.%f"
                if key == 'created_at' or key == "updated_at":
                    value = datetime.strptime(kwargs[key], format)

                if key != "__class__":
                    setattr(self, key, value)

    def __str__(self) -> str:
        # Return a string representation of the class name, id and dictionary
        return f'[{self.__class__.__name__}] ({self.id}) {self.__dict__}'

    def save(self):
        # updates to current time
        updated_at = datetime.now()
        return updated_at

    def to_dict(self):
        # Dictionary representation of the instance with "__class__" name included
        new_dict = {}
        for key, values in self.__dict__.items():
            if key == 'created_at' or key == "updated_at":
                new_dict[key] = values.strftime("%Y-%m-%dT%H:%M:%S.%f")
            else:
                new_dict[key] = values

        new_dict['__class__'] = self.__class__.__name__

        return new_dict
