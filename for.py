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
a=str(input("enter a string:"))
vowel=['a','e','i','o','u']
count=0
for b in a:
    if  b in vowel:
        count+=1
print(count)  
    


    