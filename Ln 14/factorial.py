def factorial(num):
    '''this is a recrusive function to find the factorial of a number
    '''
    if num==0 or num==1:
        return 1
    else:
        return num * factorial(num-1)
print(factorial.__doc__)
print("the factorial of 0:" , factorial(0))
print("the factorial of 1:" , factorial(1))
print("the factorial of 4:" , factorial(4))
print("the factorial of 6:" , factorial(6))
print("the factorial of 10:" , factorial(10))  