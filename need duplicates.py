mat=[]
c=[1, 3, 6, 5, 4, 8, 9, 5, 2, 2, 3, 3, 6, 58, 9, 6, 32, 3, 9, 6]
for i in c:
    if c.count(i)>1:
        mat.append(i)
print(set(mat))