class capital:
    def __init__(self):
        self.str1= ""
    def get_string(self):
        self.str1= input("Enter the string")
    def print_string(self):
        print("the result is: ",self.str1.upper())
a=capital()
a.get_string()
a.print_string()
