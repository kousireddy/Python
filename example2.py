class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}({self.age})"
    
name = input("Enter name : ")
age = int(input("Enter age : "))
p1 = Person(name,age)
print(p1)
