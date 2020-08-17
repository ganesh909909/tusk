# def damn(func):
#     def inner(a,b):
#         if a<b:
#             a,b=b,a
#             return (func(a,b))
#         else:
#             return (func(a,b))
#     return inner
# @damn
# def div(a,b):
#     return(a//b)
# a=div(2,4)
# print(a)

# def smart(func):
#     def inner(a,b):
#         if a==45 and b==3:
#             return 55
#         else:
#             return func(a,b)
#     return inner
# @smart
# def add(a,b):
#     return (a+b)
# a=add(44,3)
# print(a)

# def smart(func):
#     def concatenation(a,b):
#         if type(a)==type(b) and len(str(a))==len(str(b)):
#             return func(a,b)
#         elif type(a)!=type(b):
#             return('data type no match')
#         else:
#             return('length no match')
#     return concatenation
# @smart
# def add(a,b):
#     return (a+b)
# print(add(90,90))

# def outer():
#     print('outside function')
#     def inner():
#         print('inside function')
#     print('ganesh')
#     return inner()
# a=outer()
# a

def outer():
    print('outside function')
    def inner():
        print('inside function')
    print('ganesh')
    return inner
a=outer()
a()






