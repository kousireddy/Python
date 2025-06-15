#Math module
import math
import random
x=float(input("Enter a number: "))
print(math.floor(x))
print(math.ceil(x))
print(math.fabs(x))

x=int(input("Enter a number: "))
y=int(input("Enter a number: "))
print(math.factorial(x))
print(math.fmod(x,y))
print(math.frexp(x))
print(math.gcd(x,y))
print(math.ldexp(x,y))
print(math.modf(x))
print(math.trunc(x))
print(math.exp(x))
print(math.fabs(y))
print(math.log(x,y))
print(math.pow(x,y))
print(math.sqrt(x))
print(math.exp(x))
print(math.log(x))
print(math.log10(x))
print(math.log2(x))

#trigonometric functions
print(math.sin(x))
print(math.cos(x))
print(math.tan(x))


print(math.degrees(x))
print(math.radians(x))

a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
print(math.hypot(a,b))
print(math.isfinite(a))
print(math.isinf(a))
print(math.isnan(a))
print(math.isqrt(a))

print(math.comb(a,b))
print(math.perm(a,b))


#constants
print(math.pi)
print(math.e)
print(math.tau)
print(math.inf)
print(math.nan)


k=int(input("k= "))
l=int(input("l= "))
list=[1,2,3,4,5,6,7,8,9,0]
print(random.random())
print(random.uniform(k,l))
print(random.randint(k,l))
print(random.choice([1,2,3,4,5,6,7,8,9,0]))
print(random.choices([123,456,678,9,23],k=1))
random.shuffle(list)
print(list)


