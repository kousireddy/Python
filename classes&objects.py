class book:
    book1="harryportter"

    def __init__(self,title,author,publisher,rating):
        self.t=title
        self.a=author
        self.p=publisher
        self.r=rating
    def __str__(self):
        return f"Book name is {self.t} is written by {self.a} and published by {self.p}"
    def get_book_info(self):
        print(f"{self.t},{self.a},{self.p}this is book information")
        return True
    def rating(self):
        return f"{self.r} is book rating"
    
    
    @staticmethod
    def is_returned():
        return "Yes! book has been returned"
    
    @staticmethod
    def is_available():
        return "book is avilable"

    @classmethod
    def harry(cls):
        return f"{cls.book1} is class method"
    
    
    
class notebook(book):
    def __init__(self, title, author, publisher, rating):
        super().__init__(title, author, publisher, rating)
        print("This is book single level inheritance")

    def translate(self):
        return "transulate into telugu"
    
    @staticmethod
    def read():
        return "This notebook is read"
    
class note(notebook):
    def __init__(self, title, author, publisher, rating):
        super().__init__(title, author, publisher, rating)
        print("This is multilevel inheritence")

class studentnote:
    def __init__(self,name,book):
        self.n = name
        self.b = book
    def __str__(self):
        return f"{self.b} written by,{self.n}"

t=input("Enter book title : ")
a=input("Enter author name : ")
p=input("Enter publisher : ")   
r=input("Enter book rating : ")

book1=book(t,a,p,r)
notebook1=notebook(t,a,p,r)
note1=note(t,a,p,r)
student1=studentnote("kousalya","how to win")

#book 
print(book1)
print(book1.get_book_info())
print(book1.rating())
print(book1.is_available())
print(book.harry())
print(book1.is_returned())

#notebook
print(notebook1.get_book_info())
print(notebook1.rating())
print(notebook1.harry())
print(notebook1.translate())
print(notebook1.read())

#note
print(note1.get_book_info())
print(note1.read())
print(note1.translate())

#studentnote
print(student1)



