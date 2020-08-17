n=[9,1,3,5,6,30,13,18,16,14.5]
u=max(n)//2
k=[]
for y in n:
    d=abs(u-y)
    r=k.append(d)
z=k.index(min(k))
i=n[z]
print(i)
