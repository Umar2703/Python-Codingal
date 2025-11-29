print("enter marks obtained in 6 subjects:")
math = int(input("enter your math marks:"))
english = int(input("enter your english marks:"))
Social = int(input("enter your Social marks:"))
Islamic = int(input("enter your Islamic marks:"))
Science = int(input("enter your Science marks:"))
Urdu = int(input("enter your Urdu marks:"))
sum = math+english+Science+Social+Urdu+Islamic
print("sum of all subjects" ,sum)
percentage = (sum/600) * 100
print("the percentage is",percentage)