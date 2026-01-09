bill= float(input("Enter the total amount :"))
paid= int(input("enter the paid amount:"))
def dueamount(bill,paid):
    due=bill-paid
    return due
print("the due amount is", dueamount(bill,paid))