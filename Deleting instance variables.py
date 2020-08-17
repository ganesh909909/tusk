#within the class :del self.variable name
#outside the class:del object reference .variable name

# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=30
#     def delete(self):
#         del self.b
#         del self.c
# t1=test()
# t1.delete()
# del t1.a
# print(t1.__dict__)
# class test:
#     def __init__(self):
#         self.a=10
#         self.b=20
#         self.c=40
# t1=test()
# t2=test()
# del t1.a
# del t2.b
# print(t1.__dict__)
# print(t2.__dict__)
