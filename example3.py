class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def myfunc(self):
        print("Hello my name is " + self.name)
name = input("Enter name : ")
age = int(input("Enter age : "))
p1 = person(name,age)
p1.myfunc()
