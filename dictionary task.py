# d1={1:10,2:20}
# d2={3:30,4:40}
# d3={5:50,6:60}
# d={}
# for d4 in (d1,d2,d3):d.update(d4)
# print(d)

# d1={1:10,2:20}
# d2={3:30,4:40}
# d3={5:50,6:60}
# d1.update(d2)
# d1.update(d3)
# print(d1)

# n=int(9)
# d={1:10,2:20,3:30,4:40}
# if n in d:
#     print('key is present')
# else:
#     print('not')

# d={1:20,2:30,4:78}
# for d,v in d.items():
#     print(d,v)

# d={x:x*x for x in range(1,6)}
# print(d)

# a={1:10,2:20,3:30}
# result=1
# for x in a.values():
#     result=result*x
# print(result)

# x={'a':10,'d':45,'r':78,'j':89}
# x.pop('j')
# print(x)

# k=[1,2,3,4,5,9]
# v=[23,45,67,89,9,78]
# l={}
# for a in k:
#     for b in v:
#         l[a]=b
#         v.remove((b))
#         break
# print(l)

# k=[1,2,3,4,5,9]
# v=[23,45,67,89,9,78]
# print(dict(zip(k,v)))

# k=[1,2,3,4,5,9]
# v=[23,45,67,89,9,78]
# d={k[i]:v[i] for i in range(len(k))}
# print(d)

# k=[1,2,3,4,5,9]
# v=[23,45,67,89,9,78]
# c={}
# for i in range(len(k)):
#     c[k[i]]=v[i]
# print(c)

# d={'a':100,'k':35,'p':45}
# f={'a':100,'k':35,'o':45}
# o={}
# for k in d:
#     if k in f:
#         d[k]=d[k]+f[k]
# f.update(d)
# print(f)

# z=[{'v':'s001'},{'v':'s002'},{'vi':'s001'},{'vi':'s005'},{'vii':'s005'},{'v':'s009'},{'viii':'s007'}]
# s=set()
# for i in z:
#     for k in i.values():
#         s.add(k)
# print(s)


# from heapq import nlargest
# k={'a':500,'o':345,'k':456,'h':34,'i':98,'l':87}
# l=nlargest(2,k,key=k.get)
# print(l)

# from collections import Counter
# l=[{'item':'item1','amount':400},{'item':'item2','amount':300},{'item':'item1','amount':750}]
# r=Counter()
# for d in l:
#     r[d['item']]=r[d['item']]+d['amount']
# print(r)


# k={'item1':45.5,'item2':35,'item3':41.30,'item4':55,'item5':24,'item6':96}

from collections import defaultdict,Counter
# str1='pythonandpython'
# k={}
# for letter in str1:
#     k[letter]=k.get(letter,0)+1
# print(k)

# str1='hyderabad'
# l=str1.strip()
# u=0
# d=dict.fromkeys(l,u)
# for i in l:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)
#
# o='hyderabad'
# l=o.strip()
# d1=dict([i,l.count(i)]for i in l)
# print(d1)

# k={'a':10,'b':20,'c':34,'r':45}
# j={'a':10,'b':29,'c':4,'r':45}
# for key,value in set(k.items())&set(j.items()):
#     print(key,value)

# from collections import Counter
# l={'math':81,'c':4,'p':21}
# x=Counter(l)
# print(x.most_common())

# d={1:10,2:20,3:30,4:40,5:50,6:60}
# print('key value count')
# for count,(key,value) in enumerate(d.items(),7):
#     print(key,'  ',value,'  ',count)


# j={'c2':[1,3,4,5],'c1':[5,6,7],'c3':[9,10,11]}
# for row in zip (*([key]+(value)for key,value in sorted(j.items()))):
#     print(*row)

# n=[1,2,3,4,6]
# h=c={}
# for g in n:
#     c[g]={}
#     c=c[g]
# print(h)

# t=['ganesh',101,'rahul',102,'yeswanth',89,'sunday',67,'monday',890,'piperazine',90]
# k=['name','id']
# d=[{k[0]:t[x],k[1]:t[x+1]}for x in range(0,len(t),2)]
# print(d)


# l=[{'gfg':3},{'is':8},{'gfg':18},{'best':33},{'best':78}]
# r={}
# for x in l:
#     for key,value in x.items():
#         r.setdefault(key,[]).append(value)
# print(r)


























