def add(P,Q):
    return P+Q
def substract(P,Q):
    return P-Q
def multiply(P,Q):
        return P*Q
def divide(P,Q):
     return P/Q
print("please select the operation:")
print("a.add")
print("b.substract")
print("c.multiply")
print("d.divide")
choise= input("please enter ur choice a/b/c/d")
num1 = int(input("ENter ur first number:"))
num2 = int(input("ENter ur second number:"))
if choise == "a":
    print(num1 , "+ ",num2,"=" ,add(num1 ,num2))
elif choise == "b":
    print(num1 , "- ",num2,"=" ,substract(num1 ,num2))
elif choise == "c":
    print(num1 , "* ",num2,"=" ,multiply(num1 ,num2))
elif choise == "d":
    print(num1 , "/ ",num2,"=" ,divide(num1 ,num2))
else:
     print("this in valid input")    