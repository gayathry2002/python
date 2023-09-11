
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


# def add(a,b):
#     print(a+b)
# def sub(a,b): 
#     print(a-b)
# def mul(a,b):
#     print(a*b)
# def div(a,b):
#     print(a%b)   
# x=int(input("enter 1st no:"))
# y=int(input("enter 2nd no:"))
# user=input("which one?")
# if user == "add":
#     add(x,y)
# elif user == "sub":
#     sub(x,y)
# elif user == "mul":
#     mul(x,y)
# else:
#     div(x,y)


# def remove_duplicates(lst):
#     l=[]
#     for i in lst:
#         if i not in l:
#             l.append(i)
#     print(l)
# l1= [1,2,3,2,2,1,4,5,3]
# remove_duplicates(l1)       


# def sum_of_squares(n):
#     sum=0
#     for i in range(1,n+1):
#         sq=i**2
#         sum+=sq
#     print(sum)
# a=int(input("enter a no:"))
# sum_of_squares(a)


# def filter_even_nmbers(lst):
#     l=[]
#     for i in lst:
#         if i%2==0:
#             l.append(i)
#     print(l)
# l1=[1,2,3,4,5,6,7,8,9,10]
# filter_even_nmbers(l1)

# def is_valid_email(email):
#     if "@" in email and "." in email:
#         print("True")
#     else:
#         print("False")
# a=str(input("enter your email:"))
# is_valid_email(a)


#return

# def sample(a,b):
#     return a+b 

# print(sample(10,20))



# def are_anagrams(str1,str2):
#   a=str(str1)
#   b=str(str2)
#   for i in a:
#     if i in b:
#        return True
#     return False
# a=str(input("enter a string:"))
# b=str(input("enter a string:"))
# print(are_anagrams(a,b))



# def number_to_words(number):
#    num={0:"zero",1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine"}
#    for i in number:
#       j=int(i)
#       if j in num.keys():
#          print(num[j])
# n=input("enter a no:")
# number_to_words(n)


# b="python"
# def sample():
#     global a
#     a="abc"
#     print("first:",b)
# def sample2():
#     print("second:",b)
#     print(a)
# sample()
# sample2()


# def sample(*args):
#     print(args[0])
# sample(5,4,7)

# default parameters

# def sample(a=4,b=10):
#     print(a+b)
# sample()

# def sample(a=4,b=10):
#     print(a+b)
# sample(7,8)

#recursion

# def sample(a):
#     if a>0:
#         print("hello")
#         a-=1
#         sample(a)
# sample(5)

def sample(a):
    if a<20:
        if a%2!=0:
           print(a)
        a+=1
        sample(a)

sample(1)
