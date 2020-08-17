def power(x,y):
    while(x%y==0):
        x=x//y
    if x==1:
        return('power of 2')
    else:
        return('no')
print(power(64,2))