class Secret:
    __privateVar=5
    def __privMeth(self):
        print("This is Secret")
    
    def hello(self):
        print(self.__privateVar)

ob=Secret()
ob.hello()
ob.__privMeth()