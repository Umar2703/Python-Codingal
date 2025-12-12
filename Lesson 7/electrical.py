un= int(input("please enter the number of units consumed"))
if un < 50:
    amount= un * 2.67
    surcharge = 25
elif un<=100:
    amount= 130 + ((un-50)* 3.67)
    surcharge =35
elif un<=200:
    amount= 130+162.50 +((un-100) *5.67)
    surcharge=45
else:
    amount=130+162.50 + 526 +((un-200)* 8.67)
    surcharge =75
total = amount + surcharge
print("electricity bill is:" , total  ) 
