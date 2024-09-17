#squares
'''
a=[i*i for i in range(1,11)]
print(a)
'''
#even
'''a=[i for i in range(1,20) if i%2==0]
print(a)
'''
#list of length of words in a sentence
'''
a=[]
word=input("Enter a sentence: ")
for i in word.split():
    a.append(len(i))

print(a)    
'''
'''
#list of tuples containing its num and its square
a=[(i,i*i) for i in range(1,10)]
print(a)
'''
#list of lowercase
'''
a=[chr(i) for i in range(ord('a'),ord('z')+1)]
print(a)
'''
#list of even numbers squared and odd numbers cubed
'''
a=[]
for i in range(1,11):
    if i%2==0:
        a.append(i*i)
    else:
        a.append(i*i*i)
print(a)
'''
'''
a=[i*i if i%2==0 else i*i*i for i in range(1,11) ]
print(a)
'''

#list of common multiples of 3 and 5 upto 100
'''

a=[i  for i in range(3,101) if (i%3==0) and (i%15==0)]
print(a)
'''
#list of prime from 1 to 50
'''
lower=1
upper=50
a=[]
for num in range(lower,upper+1):
    if num>1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            a.append(num)
print(a)
'''            
#list of numbers with their square if the num is even
'''
a=[int(input()) for i in range(1,11)]
print(a)
b=[j*j for j in a if j%2==0]
print(b)
'''
#list of uppercase from a sentence
word=input()
a=[i.upper() for i in word.split()]
print(word)
print(a)