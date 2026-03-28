class Japan():
    def capital(self):
        print(" capital of japan is Tokyo")
    def language(self):
        print("Japanese")
    def type (self):
        print("Developed")
class Germany():
    def capital(self):
        print(" capital of Germany is BErlin")
    def language(self):
        print("German")
    def type (self):
        print("Developed")
jap= Japan()
ger= Germany()
for country in(jap,ger):
    country.capital()
    country.language()
    country.type()