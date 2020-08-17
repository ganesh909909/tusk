# logic behind these is subtract '1' from the input
# put & operator between given input and subtracted output
# if the result is '0' then it is power of 2

n=int(68)
j=n-1
h=n&j
if h==0:
    print('power of 2')
else:
    print('no')
