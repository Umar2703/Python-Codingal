from abc import ABC , abstractmethod
class absclass(ABC):
    def print(self,x):
        print("passed value", x)
    @abstractmethod
    def task(self):
        print("WE are inside Abs class task")
class test_class(absclass):
    def task(self):
        print("We are indide tex class task")
obj = test_class()
obj.task()
obj.print(100)