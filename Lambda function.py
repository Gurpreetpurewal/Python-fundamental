user_input = int(input("enter the variable:"))

from functools import reduce
arr = []

num = int(input("enter the size of array:"))
for i in range(num):
    nums = int(input("enter the number:"))
    arr.append(nums)
    
result = reduce(lambda a,b: a*b, arr) 
print(result)   