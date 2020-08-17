y=int(108)
if y%4==0 and y%100!=0 or y%400==0 and y%100==0:
    print(y,'leap year')
else:
    print(y,'usual year')