import enum


class BaseEnum(str, enum.Enum):
    @classmethod
    def has_value(cls, val):
        return any(val == item.value for item in cls)