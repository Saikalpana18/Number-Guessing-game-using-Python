
import random
print("WELCOME TO NUMBER GUESSING GAME")
n1=int(input("Enter the first number:"))
n2=int(input("Enter the second number:"))
sysgen=random.randint(n1,n2)
n=int(input("Enter the Guessing number:"))
count=0
sum=0
while sysgen!=n:
    if n<sysgen:
        print("wrong guess,Too low!")
        n= int(input("Enter number again: "))
        sum=sum+1
    elif n>sysgen:
        print("wrong guess,Too high!")
        n= int(input("Enter number again: "))
        count=count+1
    else:
      break
print("you guessed it right!!")
total=count+sum
if total >=1:
    print("You take ",total,"attempts")
    print("Better Luck Next time")
elif total==0:
    print("congratulations,You Guessed in single Attempt")
