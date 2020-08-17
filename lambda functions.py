# x=lambda a:a+10
# print(x(5))

def myfun(n):
    return lambda a:a*n
mydoubler=myfun(2)
print(mydoubler(11))

# o=[12,34,13,15,17,18,12,13,45,65,34,76,86,96,98,97,90]
# y=list(filter(lambda x:x%2==0,o))
# print(y)

# o=[12,34,13,15,17,18,12,13,45,65,34,76,86,96,98,97,90]
# y=list(map(lambda x:x*5,o))
# print(y)

import functools as re
o=[12,34,13,15,17,18,12,13,45,65,34,76,86,96,98,97,90]
d=(re.reduce(lambda x,y:x+y,o))
print(d)

# from functools import reduce
# a=[13,26,39,52,65,34,23,56,54,57,58,59,40]
# b=reduce(lambda x,y:x+y,a)
# print(b)

# p=['madam','rotor','malayalam','reverse','ganesh']
# o=list(filter(lambda x:x==x[::-1],p))
# print(o)


# m=[12,65,54,39,102,339,221,50,70]
# h=set(filter(lambda x:x%13==0,m))
# print(h)

l=['geeks','geeg','keegs','practice','aa']
s='eegsk'
k=list(filter(lambda x:sorted(s)==sorted(x),l))
print(k)

def fib(count):
    fiblist=[0,1]
    list(map(lambda x:fiblist.append(sum(fiblist[-2:])),range(2,count)))
    return(fiblist[:count])
print(fib(8))







