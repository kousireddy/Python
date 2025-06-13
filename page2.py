name = input("Enter your name - ")
college = input("Enter your college name - ")
output1 = " ".join(name)        #divides string by using given separator
output2 = ",".join(college)
print(output1)
print(output2)

#string format
name =input("Enter your name ")
age = input("Enter your age ")
place = input("Enter your native place")
print(f"my name is {name} i am {age} years old i am from {place}")
print("my name is {} i am {} years old i am from {}".format(name,age,place))


