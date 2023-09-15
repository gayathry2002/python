# s=open("sample.txt","w")
# s.write("hello\n")
# s.write("hello\n")
# s.write("hello\n")
# s.close() 

# s=open("sample.txt","r")

# print(s.read()) 


# import os
# old="sample.txt"
# new="demo.html"
# # os.rename(old,new)
# os.remove("demo.html") 


import shutil
# s=r"c:\Users\Software-4pm\Downloads\sample.txt"
# d=r"c:\Users\Software-4pm\Documents"
# shutil.copy(s,d)

src=r"c:\Users\Software-4pm\Downloads\demo.txt"
des=r"c:\Users\Software-4pm\Documents"
shutil.move(src,des)