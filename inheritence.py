class Person:
    def __init__(self,fname,lname):
        self.firstname = fname
        self.lastname = lname
    def printname(self):
        print(self.firstname,self.lastname)
x = Person("Kousi",24)
x.printname()

class Student1(Person):
    def __init__(self,fname,lname):
        Person.__init__(self,fname,lname)
y = Student1("Vamsi",24)
y.printname()

class Student2(Person):
    def __init__(self,fname,lname,year):
        super().__init__(fname,lname)
        self.graduationyear = year
    def welcome(self):
        print("Welcome",self.firstname,self.lastname,"to the class of",self.graduationyear)

z = Student2("Kousi Vamsi",24,2024)
z.printname()
print(z.graduationyear)
z.welcome()
