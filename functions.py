def fun(a,b=[]):
    b.append(a)
    return(b)
print(fun(10,[4]))
print(fun(20,[]))
print(fun(30,[12,43]))
print(fun(40))

