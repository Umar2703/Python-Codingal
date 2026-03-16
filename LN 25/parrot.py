class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
p1=parrot("Ali",12)
p2=parrot("hmaza",13)
print("parrot 1 name is",p1.name)
print("parrot 1 name is",p1.age)
print("parrot 2 name is",p2.name)
print("parrot 2 name is",p1.age)
print("parrot1 is", p1.species)
print("parrot1 is", p2.species)