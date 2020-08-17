for i in range(10001):
    num=i
    r=0
    l=(len(str(i)))
    while(i!=0):
        dig=i%10
        r=r+dig**l
        i=i//10
    if num==r:
        print(num)
#
# n='8208'
# k=[]
# l=len(n)
# for i in n:
#     k.append(int(i)**l)
# if sum(k)==int(n):
#     print(n,'armstrong')
# else:
#     print('not')
#
# n='372'
# l=len(n)
# y=[(int(m)**l) for m in str(n)]
# if sum(y)==int(n):
#     print('armstrong')
# else:
#     print('not')





