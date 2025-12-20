string =input("please enter ur word:")
char=input("please enter ur character" 
)
i=0
count=0
while i<len(string):
    if string[i]== char:
        count=count+1
    i=i+1
print("the number of times" ,char,"has occured is" ,count)       