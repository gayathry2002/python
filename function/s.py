
# def sample():
#    print("hello")

# a=int(input(":"))

# if a==1:
#    sample() 
# else:
#    pass


# function with arguments

# def sample(a,b):
#     print(a+b)
# x=int(input("first:"))  
# y=int(input("second:")) 
# sample(x,y) 


def add(a,b):
    print(a+b)
def sub(a,b): 
    print(a-b)
def mul(a,b):
    print(a*b)
def div(a,b):
    print(a%b)   
x=int(input("enter 1st no:"))
y=int(input("enter 2nd no:"))
user=input("which one?")
if user == "add":
    add(x,y)
elif user == "sub":
    sub(x,y)
elif user == "mul":
    mul(x,y)
else:
    div(x,y)




