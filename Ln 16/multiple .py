try:
    num1 , num2 = eval(input("Enter two numbers separated by a comma:"))
    result = num1/num2
    print("Result is" ,result)
except ZeroDivisionError:
    print("Division bt zero is error") 
except SyntaxError:
    print("comma is missing, enter numbers separated by comma")  
except:
    print("wrong input")         
else:
    print("No exceptions") 
finally:
    print("this will execute no matter what")    