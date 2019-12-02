class __FunctionTable:
    def __init__(self):
        # {"name" : <fn> }
        self.__name_to_fn = {}

        # {"name" : [<arg1>, <arg2>, ...]}
        self.__name_to_arg_list = {}

    def getFunction(self, name):
        return self.__name_to_fn[name]

    def setFunction(self, name, fn, arglist):
        self.__name_to_fn[name] = fn
        self.__name_to_arg_list[name] = arglist

    def getFunctionArgs(self, name):
        return self.__name_to_arg_list[name]

FunctionTable = __FunctionTable()
