# i=1
# while i < 6:
#     print(i)
#     i+=1

# n=1
# a=int(input("enter a no:")) 
# while n<a+1: 
#     if n % 2 == 0:
#        print(n)
#     n+=1      

# n=1
# a=int(input("enter a no:"))
# while n < a+1:
#     if n % 2!=0:
#         print(n)
#     n+=1     
    
# n=1
# l1=[]
# l2=[]
# a=int(input("enter a no:"))
# while n < a+1:
#     if n % 2 ==0:
#         l1.append(n)
#     else:

#         l2.append(n)
#     n+=1
# print(l1)
# print(l2)

# n=1
# a=int(input("enter a no:"))
# while n < 11:
#     print(n,"x",a,"=",n*a)
#     n+=1



a=int(input("enter 1st no:"))
b=int(input("enter 2nd no:"))
l=[]
i=1
while i<a or i<b:
    if a%i==0 and b%i==0:
        print(i)
        l.append(i)
    i+=1
max(l)
gcd=max(l)
print("gcd is:",gcd) 