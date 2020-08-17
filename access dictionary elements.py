# def func(*args):
#     return(args)
# print(func(1,2,3,4,5,6,7))

def fun(name,age,profession):
    print('name:',name)
    print('age:',age)
    print('profession:',profession)
kwargs={'name':'anne','age':26,'profession':'developer'}
(fun(**kwargs))