class Employee:
    emCount = 0
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        Employee.emCount +=1
    def disPlayCount(self):
        print("Employee total {0}".format(Employee.emCount))

    def disPlayEmployee(self):
        print("name:{0},salary:{1}".format(self.name,self.salary))
emp = Employee("张三",2000)

emp.disPlayCount()
emp.disPlayEmployee()
emp.age = 7
print(emp.age)
print(getattr(emp, 'age'))

print(Employee.__doc__)
print(Employee.__name__)
print(Employee.__module__)
print(Employee.__bases__)
print(Employee.__dict__)