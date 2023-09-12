#filter function

# def dis(n):
#     return n%2==0
# s=filter(dis,[1,2,3,4,5,6])
# print(list(s))

# def dis(n):
#     return n%2!=0
# s=filter(dis,[1,2,3,4,5,6])
# print(list(s))


# def dis(n):
#     return n%3==0
# l1=filter(dis,[1,22,55,9,12])
# print(list(l1))



#mapfunction

# def dis(n):
#     return n*3
# s=map(dis,[1,2,3,4])
# print(list(s))

# def dis(a,b):
#     return a+b
# s=map(dis,[1,2,3,4],[5,6,7,8])
# print(list(s))


# s=map(lambda n: n * 3,[1,2,3,4])
# print(list(s))


# def dis(n):
#     return "a" in n
# s=filter(dis,('apple','orange','xyz'))
# print(list(s))


# s=filter(lambda n:'a' in n,('apple','orange','xyz'))
# print(list(s))


# from functools import reduce
# def dis(a,b):
#     return a+b
# s=reduce(dis,range(1,6))
# print(s)


# from functools import reduce
# s=reduce(lambda a,b:a+b,range(1,5))
# print(s)


# from functools import reduce
# def dis(n):
#     return n % 2==0
# s=filter(dis,[66,18,22,55,9,12])
# def sum(a,b):
#     return a+b
# c=reduce(sum,s)
# print(c)

from functools import reduce
s=filter(lambda n:n%2==0,[66,18,22,55,9,12])
c=reduce(lambda a,b:a+b,s)
print(c)