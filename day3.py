#check whether sting is Armstrong or not
n=input("Enter a number : ")
sum=0
for i in n:
    sum=sum+int(i)**3
print(sum)
if(sum==int(n)):
    print("Entered number is armstrong number!!")
else:
    print("Enterd number is not Armstrong number")


#print fabinocci series
n=int(input("Enter a number - "))
a=0
b=1
print(a,b,end=' ')
for i in range(n+1):
    c=a+b
    b=c
    a=b
    print(c,end=' ')

#User ATM machine to deposite,withdraw,checkbalance

balance = 1000

while(True):
    print("*****Menu*******")
    print("1.Deposit Money")
    print("2.Withdraw Money")
    print("3.Check Balance amount")
    print("4.Exit")

    n=int(input("Enter your choice: "))
    
    if(n==1):
        amount=int(input("Enter amount to deposit: "))
        balance+=amount
        print("Money successfully deposited!")
    elif(n==2):
        amount=int(input("Enter money to withdraw"))
        if(amount>balance):
            print("Invalid amount , enter valid amount")
        else:
            balance-=amount
            print("Money is getting withdrawed!!")
            print("Money withdrawn...")
    elif(n==3):
        print("Your balance amount is : ",balance)
    
    elif(n==4):
        print("Thank you for visiting SBI ATM!!")
    
    else:
        print("Enter value as shown in ATM Menu")

#Guess the number
import random
num = random.choice([1,2,3,4,5,6,7,8,9,0])
print(num)
while(True):
    n=int(input("Enter a number to guess a number : "))
    if(n==num):
        print("You guessed it correctly")

    else:
        print("your Guess is wrong , Try again!")







