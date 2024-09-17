'''#add 2 matrix
a=[[1,2,3],[4,5,6],[1,2,4]]
b=[[1,2,3],[4,5,6],[1,2,4]]
c=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j]=a[i][j]+a[i][j]
for r in c:
    print(r)'''

'''#multiply matrix
a=[[1,7,3],[3,5,6],[6,8,9]]
b=[[1,1,1,2],[6,7,3,0],[4,5,9,1]]
row_a=len(a)
col_a=len(a[0])
col_b=len(b[0])
c=[]
for i in range(row_a):
    c.append([0]*col_b)
for i in range(row_a):
    for j in range(col_b):
        for k in range(col_a):
            c[i][j]+=a[i][k]*b[k][j]

for i in c:
    print(i)'''
'''#multiply

lit=[[1, 4, 5], [7, 3], [4], [46, 7, 3]]
mul=1
for i in lit:
    if isinstance(i,list):
        for j in i:
            mul*=j
    else:
        mul*=i
print(mul)
'''

