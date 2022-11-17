from abc import ABC, abstractmethod

class data(ABC):
    def dataInput(self, value):
        print("Your input: ",value)

    @abstractmethod
    def dataType(self, value):
        pass

class DataValue(data):
    def dataType(self, value):
        print("{} is a {}".format(value,type(value)))

obj = DataValue()
obj.dataInput("$400")
obj.dataType("$400")
