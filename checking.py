# l=[12,67,98,56,5,9]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if l[i]<l[j]:
#             l[i],l[j]=l[j],l[i]
# print(l[0])
# print(l[len(l)-1])


# n=[1,2,3,4,6,7,8,10]
# k=[]
# l=set(n)
# for i in range(min(n),max(n)+1):
#     k.append(i)
# u=set(k)
# j=u.difference(l)
# print(list(j))

# n=[1,2,3,4,6,7,8,10]
# h=[x for x in range(n[0],n[-1]+1)]
# i=set(n)
# r=set(h)
# y=(list(i^r))
# print(y)

# t=0
# for i in range(1,1000):
#     if(i%3==0 or i%5==0):
#         t=t+i
# print(t)
#
# n=set(range(0,1000,3))
# m=set(range(0,1000,5))
# j=list(n|m)
# print(sum(j))

# a=0
# b=1
# x=20000
# k=[]
# while a<=x:
#     k.append(a)
#     a,b=b,a+b
# for i in k:
#     if i%2==0:
#         print(i)

# def fac(n):
#     if n==0:
#         return 1
#     else:
#         return (n*fac(n-1))
# a=fac(100)
# r=0
# while(a!=0):
#     t=a%10
#     r=r+t
#     a=a//10
# print(r)

# n=int(input('enter the number:'))
# if n%2==0:
#     print(int((n*(n/2))+n/2))
# else:
#     print(int(n*(n/2+0.5)))

# n=int(16)
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
#     if sum==n:
#         print(i)
# else:
#     if sum>n:
#         print('invalid input')
# n=int(11)
# sum=0
# for i in range(1,n+1):
#     sum=sum+i
# print(sum)

# str='gane sh'
# w=str[2:]
# print(w)
# a=['1','2','3','hello456','hai123','welcome123']
# for i in a:
#     for j in i:
#         if j.isdigit():
#             print(j,end='')
#     print()




























































































































































































































