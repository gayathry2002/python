#even
# l=[1,2,3,4,5,6,8,10,22,9]
# for a in l:
#     if a % 2 == 0:
#         print(a)

#odd
# l=[1,2,3,4,5,6,8,10,22,9]
# for a in l:
#     if a % 2 != 0:
#        print(a)

# odd $ even from l
# l=[1,2,3,4,5,6,8,10,22,9]
# l1=[]
# l2=[]
# for a in l:
#     if a % 2 == 0:                                                                                          
#        l1.append(a)
# print(l1)
# for b in l:
#     if b % 2 != 0:
#         l2.append(b)
# print(l2)

# sum (l)
# l=[1,2,3,4,5,6,8,10,22,9]
# fact=1
# for a in l:
#     fact*=a
# print(fact)


#common list
# l1=[1,2,3,4,5,6]
# l2=[2,7,4,5,6,9]
# l=[]
# for a in l1:
#     if a in l2:
#         l.append(a)
# print(l)


#vowel
# a=str(input("enter a string:"))
# vowel=['a','e','i','o','u']
# count=0
# for b in a:
#     if  b in vowel:
#         count+=1
# print(count)  
    
#name
# s=" "
# a=str(input("enter your name: "))
# l=a.split()
# for b in l:
#     c=b.capitalize()
#     s+=c + ' '
   
# print(s)


#special char
# a="p@#.yt.@@hon#]"
# s=" "
# for b in a:
#     if b.isalpha():
#        s+=b 
        
# print(s)



# a=str(input("enter a string:"))
# s=" "
# for b in a:
#     if b.isalpha():
#        s+=b 
# print(s)


# for i in range(1,n+1):
#     print(i) 


# n=int(input("enter a range:"))
# for i in range(1,n+1):
#     if i % 2 == 0:
#         print(i)
    

# a=int(input("enter a no:"))
# fact=1
# for i in range(1,a+1):
#     fact*=i
# print(fact)

#sum and divisible by 3 or 5
# a=[2,3,4,10,20,9,6,15]
# sum=0
# for i in a:
#     if i % 3==0 or i % 5 == 0:
#         sum+=i
# print(sum)



# l=[]
# for i in range(8):
#     a=int(input("enter no:"))
#     l.append(a)
#     sum=0
# for b in l:
#     if b % 3 == 0 or b % 5 == 0:
#         sum+=b
# print(sum) 

#sum of n digits
# x=int(input("enter a range:"))
# sum=0
# for i in range(1,x+1):
#     sum+=i
# print(sum)
 

#count
# a=int(input("enter a no:"))
# b=str(a)
# count=0
# for i in b:
#     count+=1
# print(count)    

l=[]
sum=0
for i in range(4):
    a=int(input("enter a no:"))
    l.append(a)
    
for i in l:
    sum+=i

average=sum/4

for i in l:
    if i>average:
       print(i)
    


