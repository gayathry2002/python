# class A:
#     def __init__(self,n,m):
#         self.num1=n 
#         self.num2=m

#     def add(self):
#         print(self.num1+self.num2)

# ob=A(10,20) 
# ob.add()  

#single inhertance
# class A:
#     def dis(self):
#         print("hai")
# class B(A):
#     pass
# obj=B()
# obj.dis() 


#multiple inhertance
# class A:
#     def dis(self):
#         print("hello")
# class B:
#     def display(self):
#         print(10)
# class C(A,B):
#     pass
# ob=C()
# ob.dis()
# ob.display()

# class Vehicle:
#     def start_engine(self):
#         print("Engine is starting")
# class Car(Vehicle):
#     def drive(self):
#         print("Car is Driving")
# obj=Car()
# obj.start_engine()
# obj.drive()pass


# class Person:
#     def dis(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
# class Student(Person):
#     def display(self,grade):
#         self.grade=grade
#         print(self.grade)
# ob=Student()
# ob.dis("gayathry",20)
# ob.display(100)

pass
#multi-level-inheritance

# class A:
#     def dis(self):
#         print("hai")
# class B(A):
#     def display(self):
#         print("hello")
# class C(B):
#     def d(self):
#         print(7)
# class D(C):
#     def c(self):
#         pass
# ob=D()
# ob.dis()
# ob.display()
# ob.d()
# ob.c()


class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def person(self):
        print(self.name,self.age)
class Employee(Person):
    def __init__(self, salary):
        self.salary=salary
    def employee(self):
        print(self.salary)
class Manager(Employee):
    def __init__(self, department):
        self.department=department
    def manager(self):
        print(self.department)
ob=Manager("sales")
p=Person("anu",26)
p.person()
e=Employee(20000)
e.employee()
ob.manager()