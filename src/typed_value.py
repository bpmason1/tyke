class TypedValue:
    def __init__(self, value, valueType):
        self.__value = value
        self.__valueType = valueType

    @property
    def value(self):
        return self.__value

    @property
    def type(self):
        return self.__valueType
