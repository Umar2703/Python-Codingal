test_dict={'Umar':2,'is':2,'the':2,'best':1}
print("original dictionary",test_dict)
k=2
count=0
for key in test_dict:
    if test_dict[key]==k:
        count=count+1
print("frequency of k is",count)