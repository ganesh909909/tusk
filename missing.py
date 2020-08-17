x=[150,100,110,113,115]
y=[]
q=len(x)
t=x.sort()
for i in range(x[0],x[q-1]):
    y.append(i)
d=set(y)
r=set(x)
u=d.difference(r)
print(list(u))