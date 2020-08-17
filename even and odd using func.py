def get_numbers(type,n):
    type=type.upper()
    if type=='EVEN':
        return(list(range(0,n,2)))
    elif type=='ODD':
        return(list(range(1,n,2)))
y=get_numbers('Even',100)
print(y)