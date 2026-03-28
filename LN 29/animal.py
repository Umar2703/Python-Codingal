from abc import ABC, abstractmethod
class animal(ABC):
    def move(self):
        pass
class snake(animal):
    def move(self):
        print("I can sliyther")
class human(animal):
    def move(self):
        print("I can walk and run ")
class Lion(animal):
    def move(self):
        print("I can roar ")
class dog(animal):
    def move(self):
        print("I can bark")



a= snake() 
a.move()
b=human()
b.move()
c=dog()
c.move()
d=Lion()
d.move()