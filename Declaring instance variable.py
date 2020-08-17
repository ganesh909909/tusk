#inside constructor by using self
#inside instance method by using self
#from outside of the class by using object reference

class student:
    def __init__(self,name,age):
        self.name=name #1
        self.age=age
    def info(self):
        print('hello my name:',self.name)
        print('my age is:',self.age)
        self.marks=60 #2
s1=student('ganesh',24)
s1.info()
s1.rollno=20 #3
print(s1.__dict__)
print(s1.name,s1.age)