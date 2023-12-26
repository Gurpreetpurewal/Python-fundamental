# programme to make a list while taking user input
li = []

li_size = int(input("Enter the size of list:"))
for i in range(li_size):
    x = input("enter the first variable:")
    li.append(x)
print(li)
 
while True:
    print("Enter the following command for particular operation:")
    print("For insertion enter 1 \n For removal enter 2 \n For sorting enter 3 \n for extension of two list enter 4 ")
    num_in = int(input("enter your choice:"))
    if num_in == 1:
        li2 = []
        list_size = 1
        position = int(input("enter the position:"))
        for i in range(list_size):
            x = input("enter the varible:")
            li2.insert(position,x)
        for i in li2:
            li.append(i)
        print(li)
    elif num_in == 2:
        print("Hi user,your input list is this:",li)
        inp_user = input("what woukd you like to remove please enter:")
        li.remove(inp_user)
        print("Hi user, after removing the variable your new list is this, please chreck:",li)
    elif num_in == 3:
        print(" Hi user, your input list is this:",li)
        li.sort(reverse = True)
        print(li)
    elif num_in == 4:
        my_list_second=li.copy()
        print("this is my first list",li)
        print("this is my second list",my_list_second)
        
    else:    
        pass
    num_con = input("What would you like to do, Do you want to continue [Yes/No]=")
    if num_con == 'No':
        break
print("Hi user, Good luck for next!! Always there to assist you")
    
    
    
    
    
    
    
    
    
    
    
    
        