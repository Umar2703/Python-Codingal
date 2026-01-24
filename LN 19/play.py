L= [4,5,6,7,44,3,2,9,1,7]
print("orriginal list:",L)
sum=0
for i in L:
    sum=sum+i
average=sum /len(L)
print("sum =" ,sum)
print("average =" ,average)
L.sort(
)
print("smallest element is :",L[0])
print("largest element is:" ,L[-1])
