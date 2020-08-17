n=int(1184)
m=int(1210)
k=[]
l=[]
for i in range(1,n):
    if n%i==0:
        k.append(i)
for j in range(1,m):
    if m%j==0:
        l.append(j)
print(sum(k))
print(sum(l))