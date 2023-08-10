# a=int(input("enter first no:"))
# b=int(input("enter second no:"))
# if a<b:
#     print("b is greater")
# else:
#     print("a is greater")   
 

# a=int(input("enter a no:"))
# if a%2 == 0:
#     print(a ,"is even")
# else:
#     print(a ,"is odd")    


# age=int(input("enter your age:"))
# if age>=18:
#     print("you are eligible")
# else:
#     print("you are not eligible")    


# dob=int(input("enter your dob:"))
# age=2023-dob
# if age>=18:
#     print("you are eligible")
# else:
#     print("you are not eligible")    



# a=int(input("enter a no:"))
# if a>0:
#     print("positive")
# elif a==0:
#     print("zero")
# else:
#     print("negative")







# a=int(input("enter first no:"))
# b=int(input("enter second no:"))
# c=int(input("enter third no:"))
# if a>b:
#     print(a ,"is greater")
# elif b>c:
#     print(b,"is greater")
# else:
#     print(c,"is greater")



# a=int(input("enter a no:"))
# if a % 2 == 0 and a % 3 ==0:
#     print(a,"is even and divisible by 3")
# else:
#     print(a,"is not even and divisible by 3")


# a=str(input("enter a letter:"))
# b=['a','e','i','o','u']
# if a in b:
#     print(a,"is a vowel")
# else:
#     print(a,"is not a vowel")



# year=int(input("enter your birth year:"))
# if 1981<=year and year<=1996:
#     print("you are millennial")
# else:
#     print("you are not a millennial")



# a=str(input("enter a string:"))
# b=a[::-1]
# print(b)
# if a==b:
#     print(a,"is a palindrom")
# else:
#     print(a,"is not a palindrom")


# age=int(input("enter your age:"))
# if age>=18:
#     print("you are eligible")
# else:
#     print("you are not eligible")



age=int(input("enter your age:"))
day=str(input("day:"))
if age<12 or age>65:
    print("ticket cost is $5")
elif 12<=age<=18  and  day=="wednesday":
    print("ticket cost is $4")
else:
    print("ticket cost is $8")