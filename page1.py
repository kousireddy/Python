#stripping
s = input("Enter a Sentance : ")
print(s.strip())       #removes leading and tailing white space
print(s.lstrip())      #removes leading whitespace
print(s.rstrip())      #removes tailing whitespace

#substring
s=input("Enter a sentence : ")
print(s.find("i am"))   #returns index of substring
print(s.index("am g"))    #returns index of substring
print(s.count("i"))     #returns count of substring
print(s.replace("i am","you"))  #replace with substring

#string splitting
s=input("enter a word : ")
print(s.split(" "))  #return list of a substring

#string padding
n=input("Enter string: ")
print(n.center(100))
print(n.ljust(40))
print(n.rjust(50))
print(n.zfill(30))

x=n.encode()
print(x)


x ="xyzabcACGBJK<gVJKVL&TWT1237JHGDAKlzAGE7236E10"
for i in x:
    if i.islower():
        print("lower case letter")
    
    elif i.isupper():
        print("upper case letter")
    
    elif i.isascii():
        print("This is ascii character")
    elif i.isnumeric():
        print("This is a number")
    else:
        print("This is a special character")

