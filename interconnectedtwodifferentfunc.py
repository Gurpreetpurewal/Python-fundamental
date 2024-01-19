# Write a programe to find the common element between the lists.

def common_element_inlists():
    list1 = []
    list2 = []
    li1 = int(input("enter the size of list one:"))
    for i in range(li1):
        li1_element = int(input("enter the elements of list one:"))
        list1.append(li1_element)
    print(list1)
    
    li2 = int(input("enter the size of list two:"))
    for i in range(li2):
        li2_element = int(input("enter the elements of list two:"))
        list2.append(li2_element)
    print(list2)
    
    common_element = []
    for i in list1:
        if i in list2:
            common_element.append(i)
    print("common element in both the lists are:", common_element)
common_element_inlists()
        
        
        
        
# Write a Python program to remove duplicates from a list.

def remove_duplicate():
    variable_store = []
    list_size = int(input("enter the size of the list: "))
    for i in range(list_size):
        element = int(input("enter the variable:"))
        variable_store.append(element)
    print("*** list before unique number***")
    print(variable_store)
    
    unique_number = []
    for i in variable_store:
        if i not in unique_number:
            unique_number.append(i)
    print("***list after removal unique number***")
    print(unique_number)

remove_duplicate()

# interconnected to different function of list

def main():
    common_element_inlists()
    remove_duplicate()
    if __name__ == "__main__":
        main()    
