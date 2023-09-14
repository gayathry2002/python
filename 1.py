# class person:
#     def add(self,a,b):
#         self.a=a
#         sum=a+b
#         print(sum)


#     def display(self):
#         print(self.a)

# ob = person()
# ob.add(1,6)
# ob.display()


class calculator:
    def add(self,a,b):
        self.a=a
        self.b=b
        sum=a+b
        print(sum)
    def sub(self):
        dif=self.a-self.b
        print(dif)
    def mul(self):
        mul=self.a*self.b
        print(mul)
    def div(self):
        div=self.a/self.b
        print(div)

v=int(input("::"))
m=int(input("::"))
ob=calculator()
ob.add(v,m)
ob.sub()
ob.mul()
ob.div()