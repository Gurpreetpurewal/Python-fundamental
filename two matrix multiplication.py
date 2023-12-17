"""program to multiply two matrixs"""
a = int(input("enter the number of rows:"))
b = int(input("enter the number of columns:"))
m1 = []
for i in range(a):
    arr = []
    for j in range(b):
        fn = int(input("enter the elements:"))
        arr.append(fn)
    m1.append(arr)
    
for i in range(a):
    for j in range(b):
        print(m1[i][j],end =" ")
    print()    
    
m2 = []
x = int(input("enter the number of rows of second matrix:"))
y = int(input("enter the number of columns of second matrix:"))

for i in range(x):
    arr = []
    for j in range(y):
        el = int(input("enter the elements:"))
        arr.append(el)
    m2.append(arr)
for i in range(a):
    for j in range(b):
        print(m2[i][j],end =" ")
    print()
    

var = len(m1)
varr = len(m2[0])
result = [[0 for _ in range(var)] for _ in range(varr)]
for i in range(len(m1)):
    for j in range(len(m2[0])):
        for k in range(len(m2)):
            result[i][j] += m1[i][k] * m2[k][j]
            
for i in result:
    print(i)
            
        

    