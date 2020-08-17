# class student:
#     '''this code is written by ganesh'''
# print(student.__doc__)
# class student:
#     ''' this is designed by Ganesh'''
# help(student)

class myclass:
    def __init__(self):
        print(id(self))
s=myclass()
print(id(s))

class myclass:
    def __init__(self,name,age):
        self.name=name
        self.age=age

s=myclass('ganesh',24)
print(s.age)
print(s.name)

class student:
    def __init__(self,name,age,marks):
        self.name=name
        self.age=age
        self.marks=marks
    def talk(self):
        print('my name is',self.name)
        print('my age is', self.age)
        print('my marks are', self.marks)
s=student('ganesh',24,100)
s.talk()


