#swap first and last element
'''a=[1,2,3]
l=len(a)
temp=a[0]
a[0]=a[l-1]
a[l-1]=temp
print(a)
'''

#swap 2 numbers
'''
list=[1,4,3,2]
pos1=2
pos2=4
def exchange(a,pos1,pos2):
    a[pos1],a[pos2]=a[pos2],a[pos1]
    return a
print(exchange(list,pos1-1,pos2-1))
'''
#num of elements
'''
list=[1,4,3,2]
count=0
for i in list:
    count+=1
print(count)
'''
#reverse list
'''
list=[1,3,22,5]
print(list[::-1])

'''

#clear list
'''
a=[1,2,3,4]
print(a)
a*=0
print(a)

'''

#min  or max
'''
a=[4,6,4,1,7,2]
min=a[0]
for i in range(len(a)):
    if a[i]<min:
        min=a[i]
print(min)
'''
#second largest
'''
a=[4,9,4,1,7,2]
max=a[0]
second_max=a[0]
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
for i in range(len(a)):
    if a[i] > second_max and a[i]!= max:
        second_max=a[i]
print(second_max)

#innerlist
a=[1,3,4,5,6,6]
result=[]
for i in range(0,len(a),2):
    result.append([a[i],a[i+1]])
print(a)
print(result)

#sum of elements
a=[1,2,3,4]
sum=0
for i in a:
    sum+=i
print(sum)

#Multiply of elements
a=[1,2,3,4]
mul=1
for i in a:
    mul*=i
print(mul)

#check element in list
a=[1,3,4,3,5]
if 6 in a:
    print("yes")
else:
    print("no")
'''
#N largest elements
'''a=[1,4,5,6,7,5,4]
result=[]
n=int(input())
for i in range(0,n):
    max=0
    for i in a:
        if i>max:
            max=i
    a.remove(max)
    result.append(max)
print(result)'''

'''#print all +ve numbers
min=-1
max=5
for i in range(min,max+1):
    if i>0:
        print(i,end=' ')'''
'''list=[]
num=int(input("Enter length of list"))
for i in range(num):
    j=int(input("Enter elements in list:"))
    list.append(j)
print("list before deletion",list)
n=int(input("Number of elements to be removed"))
unwanted_elem=[]
for i in range(n):
    j=int(input("Enter number:"))
    unwanted_elem.append(j)
print(unwanted_elem)
for item in list:
    if item in unwanted_elem:
        list.remove(item)
print(list)'''
#remove empty lists & tuples
'''list1=[1,3,[],5,()]
print(list1)
new_list=[i for i in list1 if i!=()]
print(new_list)'''

'''#cloning
list1=[1,4,3,2]
list2=[i for i in list1 ]
print(list2)'''

'''#count of an element
list1=[20,3,2,3,5,5,6]
elem=int(input("Enter element"))
count=0
for i in list1:
    if i==elem:
        count+=1
print(count)'''

#display duplicates
'''list1=[1,4,3,3,2,2,1,1]
unique=[]
duplicate=[]
for i in list1:
    if i not in unique:
        unique.append(i)
    elif i not in duplicate:
        duplicate.append(i)
print(duplicate)
'''
'''
#cumulative sum
lit=[1,3,2,3,4]
new=[]
sum=0
for i in lit:
    sum+=i
    new.append(sum)
print(new)'''

'''#sum of integers
list=[17,45,32,33,66]
sum_elem=[]
for i in list:
    j=str(i)
    sum=0
    for k in j:
        sum+=int(k)
    sum_elem.append(sum)
print(sum_elem)'''

'''#sort list based on another list
list1=['a','h','j','g','r','q']
list2=[1,4,3,2,1,5]
combine=[]
#combining two lists
def sorting(list2,list1):
    for i in range(len(list1)):
        combine.append([list1[i],list2[i]])
    print("Combined list before sorting: ",combine)
    #sort combined
    for i in range(len(combine)):
        for j in range(0,len(combine)-i-1):
            if combine[j][0]>combine[j+1][0]:
                combine[j],combine[j+1]=combine[j+1],combine[j]
    print("Combined list after sorting: ",combine)
    #add sorted elements
    sorted=[]
    for i in range(len(combine)):
        sorted.append(combine[i][1])
    print(sorted)
sorting(list1,list2)'''


