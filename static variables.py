# class student:
#     cname='CMR Institute'
#     def __init__(self,name,rollno):
#         self.name=name
#         self.rollno=rollno
# s1=student('rahul',101)
# s2=student('pavan',102)
# print(s1.name,s1.rollno,student.cname)
# print(s2.name,s2.rollno,s1.cname)


# what are various places are there to declare static variables
# within the class directly but from outside of any method
# ex class test
# x=10
# inside constructor by using class name
# ex def__ init__(self):
# test.y=20
# inside instance method by using class name
# ex def m1(self):
# test.c=70
# inside class method by using cls variable or class name
# ex@classmethod
# def m2(cls):
# cls.d=34
# test.e=50
# inside static method by using class name
# @static method
# def m3():
# test.f=60
# from outside of the class by using class name
# test.g=70


#how to access static variables
#we can acess static variables either by class name (or) by object reference
#within the class
#classname,self,cls
#outside of the class
#object reference,classname
# class test:
#     a=10
#     def __init__(self):
#         print('inside constructor')
#         print(test.a)
#         print(self.a)
#     def m1(self):
#         print('inside instance method')
#         print(test.a)
#         print(self.a)
#     @classmethod
#     def m2(cls):
#         print('inside class method')
#         print(test.a)
#         print(cls.a)
# t=test()
# t.m1()
# t.m2()
# print('outside of the class')
# print(test.a)
# print(t.a)

# #declaring static variables
# class test:
#     x=10
#     def __init__(self):
#         test.a=40
#     def m1(self):
#         test.b=78
#     @classmethod
#     def m2(cls):
#         cls.c=56
#         test.l=67
#     @staticmethod
#     def m3():
#         test.o=90
# t=test()
# t.m1()
# t.m2()
# t.m3()
# test.u=43
# print(test.__dict__)

#how to modify static variables
#within the class we should use class name,cls variable
#from outside of the class only class name
# class student:
#     x=10
#     def __init__(self):
#         student.x=20
#     def m1(self):
#         student.x=30
#     @classmethod
#     def m2(cls):
#         cls.x=40
#         student.x=50
#     @staticmethod
#     def m3():
#         student.x=60
#
# t=student()
# t.m1()
# t.m2()
# t.m3()
# student.x=80
# print(student.x)

#How to delete static variabes
#within the class
#class name,cls variable
#outside of the class
#only class name
# class test:
#     x=10
#     def __init__(self):
#         del test.x
# print(test.__dict__)
# t=test()
# print(test.__dict__)









