class Protected:
    def __init__(self):
        self._protectedVariable = "This variable is protected!"
        self.__privateVariable = "This variable is private!"

    def getPrivate(self):
        print(self.__privateVariable)

    def setPrivate(self, private):
        self.__privateVariable = private

classObj = Protected()
print(classObj._protectedVariable)
classObj._protectedVariable = "I have changed the protected variable!"
print(classObj._protectedVariable)
classObj.getPrivate()
classObj.setPrivate("I have changed the private variable!")
classObj.getPrivate()
