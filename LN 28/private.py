class myclass:
    __privatevar = 27
    def __privmeth(self):
        print("I am inside class myclass")
    def hello(self):
        print("private variable value",myclass.__privatevar)
obj = myclass()
obj.hello()
obj.privmeth()