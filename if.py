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



# age=int(input("enter your age:"))
# day=str(input("day:"))
# if age<12 or age>65:
#     print("ticket cost is $5")
# elif 12<=age<=18  and  day=="wednesday":
#     print("ticket cost is $4")
# else:
#     print("ticket cost is $8")

# amnt=int(input("enter your amount:"))
# discount=(10/100)*amnt
# if amnt>=100:
#    print("applied a 10% discount of $",discount)
# else:
#    print("no discount is applied")

print("which of the following is fruit")
print("optins are:" "a.dog"  "b.hat"  " c.ball"   "d.apple")
answer=str(input("enter your ans:"))
ans="apple"
score=0
if answer==ans:
    score+=1 
    print("which of the following is even")
    print("optins are:" "a.2"  "b.1"  " c.3"   "d.7")
    answer=int(input("enter your ans:"))
    ans=2

    if answer==ans:
       score+=1
       print("captital of india")
       print("optins are:" "a.delhi"  "b.kerala"  " c.maharastra"   "d.gujarat")
       answer=str(input("enter your ans:"))
       ans="delhi"
       if answer==ans:
          score+=1
          print(score)
else:
    print("you entered wrong ans")
    score-=1
    print(score)
    c= input("would you wanto to continue?")
    if c == "yes":
         print("captital of india")
         print("optins are:" "a.delhi"  "b.kerala"  " c.maharastra"   "d.gujarat")
         answer=str(input("enter your ans:"))
         ans="delhi"
         if answer==ans:
            score+=1
            print(score)

    else:
        print("thank you")

print("total is:",score)




