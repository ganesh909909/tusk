# g=(x*x for x in range(2,19))
# while True:
#     print(next(g))

# import time
# def countdown(n):
#     while n>0:
#         yield n
#         n=n-1
# x=countdown(10)
# for y in x:
#     print(y)
#     time.sleep(3)

# # def first(num):
# #     n=1
# #     while n<=num:
# #         yield n
# #         n=n+1
# # x=first(10)
# # for y in x:
# #     print(y)
#
# def fib():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
# for n in fib():
#     if n>10:
#         break
#     print(n)

g=(x**2 for x in range(12))
print(next(g))
print(next(g))
print(next(g))


