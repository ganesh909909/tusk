# n = int(365214)
# if n > 0:
#     g = n - 1
#     j = g % 9 + 1
#     print(j)
# else:
#     print(0)

# n=('2345')
# while len(str(n)) > 1:
#     y=[int(l) for l in str(n)]
#     n=sum(y)
# print(n)

# n=int(input('enter the number:'))
# if n==0:
#     print(0)
# elif (n%9==0):
#     print(9)
# else:
#     print(n%9)

n=('23456567845')
k=[]
while len(str(n))>1:
    for i in str(n):
        k.append(int(i))
    n=sum(k)
    k.clear()
print(n)

