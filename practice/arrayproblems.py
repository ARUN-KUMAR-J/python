#sum of array
"""
a=[1,4,5]

sum=0
for i in a:
    sum+=i
print(sum)
"""

#find largest element in an array
'''
a=[5,6,9,10,8]
n=len(a)
max=a[0]
for i in range(1,n):
    if a[i]>max:
        max=a[i]
print(max)
'''
#array rotation-left
'''
a=[4,5,2,1,7,8,9]
d=2
c=0
def reversearr(a,d):
    c=(a[d:])+(a[:d])
    return c
print(reversearr(a,d))
'''

#array rotation right
'''
a=[4,5,2,1,7,8,9]
d=2
c=0
l=len(a)
def reversearr(a,d):
    c=a[l-d:l]+a[:l-d]
    return c
print(reversearr(a,d))
'''
#split the array and rejoin
'''
a=[12,10,5,6,52,36]
d=2
l=len(a)
def splitarr(a,d):
    c=a[d:]+a[:d]
    return c
print(splitarr(a,d))

'''
#remainderof value get by multiply all elements in an array
'''
a=[100,10,5,25,35,14]
mul=1
n=11
for i in a:
    mul*=i
print(mul%n)

'''
#monotonic
'''
a=[6,7,4,4]
def monotone(a):
    n=len(a)
    if n==1:
        return True
    else:
        if all(a[i]>=a[i+1] for i in range(0,n-1) or a[i]<=a[i+1] for i in range(0,n-1)):
            return True
        else:
            return False
print(monotone(a))'''
'''
b=list(map(int,input().split()))
print(b)
'''
'''
li=[10,11,13,14,15]
count=0
for i in li:
    count+=1
print(count)'''