class Employee:
    def __init__(self, Name, Age,Employee_id, Address, Mobile):
        self.Name = Name
        self.Age = Age
        self.Employee_id = Employee_id
        self.Address = Address
        self.Mobile = Mobile
    def user(self):
        print(self.Name,self.Age,self.Employee_id, self.Address, self.Mobile)
        
        
x = input("enter the name of Employee:")      
y =  input("enter the age of employee:")
z = input("enter the employee_id:")
a = input("enter the Address of employee:")
b = input("enter the mobile:")

obj = Employee(x,y,z,a,b)

obj.user() 

    
