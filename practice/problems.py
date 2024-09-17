"""a=int(input("enter 1st num:"))
b=int(input("enter 2nd num:"))"""
#sum of two numbers
#print(a+b)

#maximum
#print(max(a,b))
'''
#factorial
def fact(n):
    return 1 if (n==0 or n==1) else n*fact(n-1)
n=int(input("Enter number"))
print(fact(n))
'''
#simple interest
'''
p=int(input("ENter principal amount"))
n=int(input("Enter time"))
r=int(input("Enter interest"))
si=(p*n*r)/100
print(si)
'''
#compund interest

#p=int(input("ENter principal amount "))
#t=int(input("enter time "))
#r=int(input("Enter interest "))
#A=p*(pow((1+r/100),t))
#ci=A-p
#print(ci)
'''
#Armstrong num
n=int(input("Enter number: "))
num_2_str=str(n)
length=len(num_2_str)   
sum=0
for i in num_2_str:
    sum+=int(i)**length   
if sum==n:
    print("It\'s an amstrong number")
else:
    print("It\'s not an amstrong number")
print(sum)
print(n)
'''
#area of circle\
'''
import math
r=int(input("Enter radius "))
print(math.pi*(r*r))
'''
#check num is prime or not
'''
n=int(input("Enter number: "))
a=False
if n==1:
    print("Its not a prime number")
else:
    for i in range(2,n):
        if (n%i)==0:
           a=True
           break
if a:
    print("not a prime")
else:
    print("prime")
            '''
#print all prime in a given interval
'''
lower=10
upper=100
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
'''

#print fibanacci series
'''
n=int(input("Enter integer: "))
a=0
b=1
print(a)
print(b)
c=0
i=1
while i<n:
    c=a+b
    a=b
    b=c
    print(c)
    i=i+1
'''
#check fibonacci num
'''
n=int(input("Enter number: "))
a=0
b=1
c=0
if(n==0) or(n==1):
    print(n,"is a fibonacci number")
else:
    while(True):
        c=a+b
        if(c==n):
            print(n,"is a fiboacci number")
            break
        elif c>n:
            print(n,"is not a fibonacci number")
            break
        else:
            a=b
            b=c
'''
'''
#find nth multiple of an integer in fibonacci series
def find(num,mul):
    a=0
    b=1
    i=2
    while(i!=0):
        c=a+b
        a=b
        b=c
        if b%mul==0:
            return num*i
        i+=1
    return

num=int(input("Enter number:"))
mul=int(input("Enter multiple"))
print(find(num,mul))
'''
#to print ascii
"""c=input("Enter a character:")
print(ord(c))"""

#sum of squares of first n natural numbers
'''
n=int(input("Enter number: "))
sum=int((n*(n+1)*((2*n)+1))/6)
print(sum)'''

#cube sum
'''
n=int(input("Enter number: "))
sum=int(((n*(n+1))/2)**2)
print(sum)
'''
#sum of elements that are not perfect square
'''list1=[25,36,82,65,225]
sum=0
count=0
for i in list1:
    for j in range(1,i//2):
        if (i/j)==j:
            sum+=i
    count+=i 
sum=count-sum
print(sum)

'''

#sum of non prime numbers
'''
list1=[9,19,6,29,3,5]
sum=0

for i in list1:
    count=0
    for j in range(1,i):
        if i%j==0:
            count+=1
    if count>1:
        sum+=i
print(sum)'''
