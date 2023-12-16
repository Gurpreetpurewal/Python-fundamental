import calculations as cal
a = int(input("enter the first variable:"))
b = int(input("enter the second vairable:"))
 
while True:
    print("for addition enter 1","for substraction enter 2","for substraction enter 3","for substraction enter 4")
    x = int(input("enter your choice:"))
    if x == 1:
        cal.addition(a, b)
    elif x == 2:
        cal.substraction(a, b)
    elif x == 3:
        cal.multiplication(a, b)
    elif x == 4:
        cal.divide(a, b)
    else:
        pass 
    
    
    y = input("Do you want to continue yes/no:")
    if y == "no":
        break
print("Good luck for next")
    