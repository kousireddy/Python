<<<<<<< HEAD
#String maipulation

name = input("Enter your name: ")
print(name)                                      #print stirng
print(name[2:])      
print(name[3:6])                            #slicing
print("My name is :"+name)                       #concatination
print(len(name))


# case conversion

print(name.upper()) #upper
print(name.lower()) #lower
print(name.capitalize())  #capitalize first character

y=input("Enter a sentence")
print(y.title())       #capitalizes each letter in a word in sentence

s = "i am from india"
print("india" in s)  #returns boolean true or false


=======
import store.arraysquare as arrsq
import store.addition
arr1=[]
for i in range(5):
    n=int(input("Enter array values: "))
    arr1.append(n)
print(arr1)
print(arrsq.array_square(arr1))
print(arrsq.greeting())
print(store.addition.addition(arr1))


import pandas as pd
import matplotlib.pyplot as plt
dataframe = pd.DataFrame([1,2,3,4,5])
print(dataframe)
try:
    df = pd.read_csv('data.csv')
    print(df.to_string())
except Exception as e:
    print(e)

print(pd.__version__)

a=[1,4,5,7,3,5]
print(pd.Series(a))


data={
    "students":["radha","krishna","srinivas","narayan"],
    "rollnumbers":[456,432,421,478]
}

df=pd.DataFrame(data,index=["ece","ece","ece","ece"])
print(df)

>>>>>>> 073523b (day5python)
