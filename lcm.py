n=int(56)
m=int(96)
k=[]
l=[]
for i in range(1,m+1):
    k.append(i*n)
for j in range(1,n+1):
    l.append(j*m)
print(min(list((set(k)&set(l)))))