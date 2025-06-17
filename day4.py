#functions in python
import math
#find power of a number using python
def power(a,b):
    c=a**b
    return c

k=int(input("Enter a number - "))
l=int(input("Enter a number - "))
result=power(k,l)
print("Power of given number is : ",result)


#find out largest element in an array
def largest_inarray(arr):
    largest = arr[0]
    for i in arr:
        if i>largest:
            largest = i
    return largest

array=[1,2,3,4,5,6]
result=largest_inarray(array)
print(result)

def largest_inarray(arr):
    largest = arr[0]
    for i in arr:
        if i>largest:
            largest = i
    return largest

array=[]
for i in range(5):
    n=int(input("Enter array values : "))
    array.append(n)
print(array)
result=largest_inarray(array)
print(result)


#find smallest element in array
def smallest_inarray(arr):
    smallest = arr[0]
    for i in arr:
        if i<smallest:
            smallest=i
    return smallest
array = []
for i in range(6):
    n=int(input("Enter array values: "))
    array.append(n)
result=smallest_inarray(array)
print(result)


#find lcm 
def lcm(a,b):
    return math.lcm(a,b)
a=int(input("Enter a number : "))
b=int(input("Enter a number : "))
result=lcm(a,b)
print(result)

#reverse a string
def reverse(a):
    reverse = ' '.join(reversed(a))
    return reverse
n=input("Enter a number or a string: ")
print(reverse(n))

#calculate length of a string
def length(str):
    length = len(str)
    return length

str = input("Enter a string: ")
print(length(str))

#calculate factorial of a number
def factorial(a):
    factorial=math.factorial(a)
    return factorial
n=int(input("Enter a number: "))
print(factorial(n))

'''Exeption Handling'''
try:
    n=int(input("Enter a number : "))
    result = 10/n
except ZeroDivisionError:
    print("This is zero division error ,Number cannot by divided by zero , it leads to infinity")
except ValueError:
    print("This is value error enter correct type")
except Exception as e:
    print(e)
else:
    print(result)
finally:
    print("Code ended")

try:
    n=int(input("Enter a number : "))
    result=math.sqrt(n)
except ValueError:
    print("Enter a positive number")
except Exception as e:
    print(e)
else:
    print(result)
finally:
    print("Finished")

try:
    n1=int(input("Enter value : "))
    n2=input("Enter value : ")
    n3=n1+n2
except TypeError:
    print("You are trying to add a string and number")
else:
    print(n3)
finally:
    print("Finish")

try:
    list=[2,3,4,5]
    n=int(input("Enter index value"))
    result=list[n]
except IndexError:
    print("Index not exist")
except Exception as e:
    print(e)
else:
    print(result)
finally:
    print("Completed")

'''key error'''
my_dict = {"name1":"Kousalya","age1":21,"name2":"v","age2":21}
try:
    print(my_dict["name1"])
except KeyError:
    print("entered key is not avilable")
except Exception as e:
    print(e)
finally:
    print("Finished")

'''attribute error'''
try:
    n=int(input("Enter a number"))
    result=n.append(9)
except AttributeError:
    print("int doesnt contain append")
except Exception as e:
    print(e)
finally:
    print("finished")

'''     Decorators'''
def greeting(func):
    def wrapper(name):
        print("Good Morning")
        func(name)
        print("great day!!!")
    return(wrapper)
@greeting
def say(n):
    print(f"Hello Good morning , {n}")

say("Kousi")


def my_decorator(function):
    def wrapper(value):
        print("Before excecution")
        function(value)
        print("After excecution")
    return wrapper
@my_decorator
def value(a):
    print("value ",a+2)

y=int(input("Enter values : "))
value(y)

def bold(func):
    def wrapper():
        return "<b>"+func()+"</b>"
    return wrapper
def italic(func):
    def wrapper():
        return "<i>"+func()+"</i>"
    return wrapper

@bold
@italic
def text():
    return "HI"

print(text())
