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


# class Animal:
#     def __init__(self,name):
#         self.name=name
#     def dis(self):
#         print(self.name)
# class CanFly:
#     def fly(self):
#         pass
# class CanSwim:
#     def swim(self):
#         pass
# class Duck(Animal,CanFly,CanSwim):
#     def __init__(self, color):
#         self.color=color
#     def display(self):
#         print(self.color)
# ob=Duck("purple")
# obj=Animal("gayathry")
# a=CanFly()
# b=CanSwim()
# obj.dis()
# a.fly()
# b.swim()
# ob.display()


# #multi-level-inheritance

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


# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def person(self):
#         print(self.name,self.age)
# class Employee(Person):
#     def __init__(self, salary):
#         self.salary=salary
#     def employee(self):
#         print(self.salary)
# class Manager(Employee):
#     def __init__(self, department):
#         self.department=department
#     def manager(self):
#         print(self.department)
# ob=Manager("sales")
# p=Person("anu",26)
# p.person()
# e=Employee(20000)
# e.employee()
# ob.manager()


# class A:
#     def sample(self):
#         print("hello")
# class B(A):
#     pass
# class C(A):
#     pass
# class D(A):
#     pass
# o=D()
# ob=C()
# obj=D()
# obj.sample()
# o.sample()
# ob.sample()

# class Vehicle:
#     def start_engine(self,brand,model):
#         self.brand=brand
#         self.model=model
#         print(self.brand,self.brand,"engine has started")
# class Car(Vehicle):
#     def drive(self,color,seat):
#         self.color=color
#         self.seat=seat
#         print(self.color,self.seat,"car is being driven")
# class Bike(Vehicle):
#     def ride(self,color,type):
#         self.color=color
#         self.type=type
#         print(self.color,self.type,"the bike is being ridden")

# ob=Bike()
# ob.ride("black","dgyy")
# ob.start_engine("black","Harleys")
# obj=Car()
# obj.drive("black","dgyy")
# obj.start_engine("black","Harleys")


class A:
        def sample(self):
               print("hai")
class B:
        def dis(self):
            print("hello")
class C(A,B):
       def dispaly(self):
              print("zzz")
class D(A):
              pass
class E(A):
              pass
e=E()
e.sample()
ob=D()
ob.sample()
obj=C()
obj.dispaly()
obj.sample()
obj.dis()
o=B()
o.dis()

        
