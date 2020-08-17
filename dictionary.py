# count duplicates
# dict={0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'a', 5: 'b', 6: 'c', 7: 'd', 8: 'e', 9: 'i', 10: 'j', 11: 'k', 12: 'l', 13: 'm', 14: 'a', 15: 'n', 16: 'p', 17: 'v', 18: 'd', 19: 'f', 20: 'j', 21: 'b', 22: 's', 23: 'd', 24: 'f', 25: 'n', 26: 'd', 27: 'c', 28: 'n', 29: 'd', 30: 'j', 31: 's', 32: 'b', 33: 'c', 34: 's', 35: 'd'}
# list=dict.values()
# temp={}
# for elem in list:
#     if elem in temp:
#       temp[elem]=temp[elem]+1
#     else:
#         temp[elem]=1
# print(temp)

# d='the lazy frog is gone and the lazy dog is came'
# x=d.split()
# d={}
# for i in x:
#     if i in d:
#         d[i]=d[i]-1
#     else:
#         d[i]=1
# print(d)


# l1=[12,45,67,56,4,34,3]
# l2=['a','b','c','y','t','e','h']
# re={}
# for key in l1:
#     for value in l2:
#         re[key]=value
#         l2.remove(value)
#         break
# print(re)


# l1=[1,2,3,4,5,6]
# l2=['a','b','c','d','e','f']
# c={}
# for i in range(len(l1)):
#     c[l2[i]]= l1[i]
# print(c)

# l1=[1,2,3,4]
# l2=['ganesh','yuva','rahul','mital']
# res={l1[i]:l2[i] for i in range(len(l1))}
# print(res)

# l1=[1,2,3,4]
# l2=['ganesh','yuva','rahul','mital']
# res=dict(zip(l1,l2))
# print(res)


# p='hi welcome to python dictionary example'
# r=p.split()
# print(r)
# o=''.join(r)
# print(o)
# d={}
# for i in o:
#     if i in d:
#         d[i]=d[i]+1
#     else:
#         d[i]=1
# print(d)

# x={'asia':['india','japan','germany','pakistan']}
# y={'africa':['korea','afghanistan','africa','china']}
# n=('korea')
# e=x.values()
# f=y.values()
# for i in e:
#     for j in f:
#         if n in i:
#             print('asia')
#         elif n in j:
#             print('africa')
#         else:
#             print('none')


# d={x:x**2 for x in range(1,51)}
# print(d)

# from collections import Counter
# d={'a':300,'b':400,'c':500,'d':430,'w':321}
# e={'a':300,'b':400,'c':500,'f':450,'h':876}
# d1=Counter(d)+Counter(e)
# print(d1)

# d={'a':300,'b':400,'c':500,'d':430,'w':321}
# e={'a':30,'b':800,'c':590,'f':450,'h':876}
# d1={}
# for key in d:
#     if key in e:
#         d1[key]=d[key]+e[key]
# e.update(d1)
# d.update(e)
# print(d)

# d={'a':300,'b':400,'c':500,'d':430,'w':321}
# e={'a':30,'b':800,'c':590,'f':450,'h':876}
# d1={}
# for key in d:
#     if key in e:
#         d1[key]=d[key]+e[key]
# c={**e,**d,**d1}
# print(c)


# from itertools import product
# a={1:['a','b'],2:['c','d'],3:['e','f']}
# for combo in product(*[a[k] for k in sorted(a.keys())]):
#     print(''.join(combo))


# a={1:['a','b'],2:['c','d'],3:['e','f']}
# p=[]
# for i in a:
#     for j in a[i]:
#         for k in a:
#             if i!=k:
#                 for l in a[k]:
#                     d=str(j)+str(l)
#                     p.append(d)
# print(p)


# nested dictionary
# d={k:{k1:k1*k1 for k1 in range(1,7)}for k in range(1,7)}
# print(d)

# a={'m':1.02,'n':1.89,'o':3.67}
# f=2.34
# h={s:d*f for s,d in a.items()}
# print(h)

# x={0:1,1:2,8:3,5:9,6:4,3:7}
# d=({k:v for k,v in sorted(x.items())})
# print(d)


# x={0:2,1:1,8:6,5:5,6:4,3:3}
# d={k:v for k,v in sorted(x.items(),key=lambda item:item[1],reverse=True)}
# print(d)

# x={0:2,1:1,8:6,5:5,6:4,3:3}
# d={k:v for v,k in(x.items())}
# s={h:i for h,i in sorted(d.items(),reverse=True)}
# e={r:t for t,r in (s.items())}
# print(e)


# s={'a':101,'j':345,'k':234,'w':None,'m':'ganesh','f':'fg'}
# u={k:v for k,v in s.items() if v is not None and v is not 'fg'}
# print(u)








