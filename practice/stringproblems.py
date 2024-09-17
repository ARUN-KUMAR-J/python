'''#reverse string without for loop
str1="Arun"
length=len(str1)
def reverse(str1,len):
    if len>0:
        print(str1[len-1],end='')
        reverse(str1,len-1)
reverse(str1,length)
'''
'''#remove letters
str2="greek21hel5466lo"
new=""
for i in str2:
    flag=True
    try:
        int(i)
    except:
        flag=False
        new=new+i
print(new)'''


'''str1="Hi This is arun"
str2="this"
if str2.casefold() in str1.casefold():
    print("yes")
else:
    print("No")
'''

'''#count of words in string

str1="Hello this is is arun"

for i in str1.split():
    
    count=0
    for j in str1.split():
        if i==j:
            count+=1
    
    print(i,end=' ')
    print(count)
'''

'''#print even or odd lengthed words in a string
str1="hello iam arun"
str2=""
for i in str1.split():
    if len(i)%2!=0:
        str2=str2+" "+i    
print(str2)'''

'''#return string which contains all vowels
str1="hello iam"
vowel={'a','e','i','0','u'}
new=set()
for i in str1:
    if i in vowel:
        new.add(i)
print(new)
if new==vowel:
    print("Yes")
else:
    print("no")'''

#maximum frequency of a character in a string
'''
def frequency(str1):
    freq={}
    for char in str1:
        if char!= ' ':
            if char in freq:
                freq[char]+=1
            else:
                freq[char]=1
    max_freq=float('inf')
    max_char=''
    for char in freq:
        if freq[char]<max_freq:
            max_freq=freq[char]
            max_char=char
    return max_char,max_freq
string="hheelppploo iiamm arun "
x,y=frequency(string)
print(f'"{x}" {y}')
'''
#find special character

'''import re
str="hello#$ i am arun kumar"
x=re.findall("[^a-z A-Z 1-9]",str)
print(x)'''

#maximum length of words in a string

'''Str1="Hello Iam arfjfun kumar"
max=0
for word in Str1.split():
   print(word)
   if len(word)>max:
        max=len(word)
print(max)'''
'''
str1="heallo"
def freq(str):
    dict={}
    for i in str1:
        if i in ['a','e','i','o','u']:
            if i in dict:
                dict[i]+=1
            else:
                dict[i]=1
    return dict
dict=freq(str1)
for i,count in freq("hello").items():
    print(f'{i} {count}')
'''
'''str1=input()
str2=""
for i in str1:
    str2=i+str2
print(str2)'''

'''str1=input()
s=str1.split()
lenght=0
character=0
for i in s:
    if len(i)>lenght:
        lenght=len(i)
        character=i
print(character,"",lenght)'''

'''a="This is arun kumar J"
list1=[]
str1=""
for i in a:
    if i==" ":
        list1.append(str1)
        str1=""
    else:
        str1=str1+i
#print(list1)
for i in list1:
    if len(i)%2==0:
        print(i,end=" ")'''

'''#indexex of number that occurs more than half of length of the list

list1=[3,3,3,4,3,3,5,3]
dict1={}
for i in list1:
    if i in dict1:
        dict1[i]+=1
    else:
        dict1[i]=1
for i,j in dict1.items():
    #print(i,j)
    if j>(len(list1)//2):
        for k in range(len(list1)-1):
            #print(k)
            if i==list1[k]:
                print(k,end=" ")'''
  
#Kaprekar number
#n=55
m=3
for n in range(1,1001):
    j=n**2
    #print("number",n)
    j=str(j)
    #print(j)
    mid=len(str(n))
    #print(mid)
    left1=j[:-mid]
    right1=j[-mid:]
    left=int(left1) if left1 else 0
    right=int(right1) if right1 else 0
    #print("left",left)
    #print("right",right)
    sum=left+right
    #print(sum)
    if sum==n:
        if j[0]==str(m):
            print(n)
        #print("yes",n,"is a kaphrekar number")
