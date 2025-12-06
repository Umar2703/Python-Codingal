height= float(input("Enter the height in cm"))
weight = float(input("Enter the weight in kg"))
BMI = weight / (height/100) ** 2
print("your BMi is"  ,BMI)
if BMI <=18.4:   

      print("you r underweight")
elif BMI <=24.9:
      print("u r healthy")
elif BMI <=29.9:
    print("u r overweight")
elif BMI <=34.9:
     print("u r severely overweight")
elif BMI <=39.9:
     print("u r obese")
else:
     print("u r severely obese")