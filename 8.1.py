class employee:
    people=0
    def __init__(self,time,salary,num):
        self.time=time
        self.salary=salary
        self.num=num
    def Settime(self,time):
        self.time=eval(time)
    def Setsalary(self,salary):
        self.salary=eval(salary)
    def Setnum(self,num):
        self.num=num
    def compute(self):
        return self.time*self.salary
employee.people=eval(input("Enter the number of the employee:"))
i,SUM,store,praise=0,0,[],[]
emp=employee(0,0,0)
while i<employee.people:
    i+=1
    emp.Setnum(i)
    emp.Settime(input("Enter the"+str(i)+"employee 's worktime"))
    emp.Setsalary(input("Enter the"+str(i)+"employee 's salary per hour"))
    SUM+=emp.compute()
    store.append(emp.compute())
ave=SUM/employee.people
for j in store:
    if j>ave:
        praise.append(store.index(j)+1)
        store[store.index(j)]=0
print("The sum salary of all employees:",SUM)
print("These emplyee(s) earned more than average:",praise)
