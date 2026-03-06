import array as arr
array_num=arr.array('i',[1,2,4,3,7,9,3])
print("Original array;",array_num)
print("Number of occurences of the number 3 in the said array:",array_num.count(3))
array_num.reverse()
print("Reverse the order of the items:")
print(array_num)