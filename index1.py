grades={"alice":85,
        "bob":90,
        "charlie":78,
        "david":92
        }
print(grades["bob"])
grades.update({"eva":88})
print(grades)
grades.pop("charlie")
print(grades)
print("alice" in grades)
len=len(grades)
print(len)
print(grades.keys())
print(grades.values())