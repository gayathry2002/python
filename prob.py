# a=input("::")
# vowel=['a','e','i','o','u']
# l=[]  
# char=" "

# for i in a:
#     if i in vowel:
#         l.append(i)
# r=l[::-1] 

# l1=list(a)  
# l1[1]=r[0]
# l1[4]=r[1]  


# for i in l1:
#      char+=i
# print(char)
  

a="leadership"
vowels = []
l=[]
char=" "
for i in a:
    if i in ['a','e','i','o','u']:
        vowels.append(i)
r=vowels[::-1]
l1=list(a)
# l1[1]=r[0]
# l1[2]=r[1]
# l1[4]=r[2]
# l1[8]=r[3]


for i in l1:
    char+=i

print(char)
        
