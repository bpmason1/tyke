class __FunctionTable:
    def __init__(self):
        self.__name_to_fn = {}

    def getFunction(self, name):
        return self.__name_to_fn[name]

    def setFunction(self, name, fn):
        self.__name_to_fn[name] = fn

FunctionTable = __FunctionTable()
