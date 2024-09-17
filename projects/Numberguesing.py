import random
a,b=map(int,input().split())
c=random.randint(a,b)
print("You have 5 chances")
for i in range(0,6):
    d=int(input("Enter number "))
    if(d==c):
        print("You Guessed")
        break
    elif(d>c):
        print("you guessed too large")
    elif(d<c):
        print("You guesed too small")  
    else:
        print("You're wrong")