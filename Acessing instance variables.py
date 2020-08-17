#within the class by using self from outside of the class by using object reference

class student:
    def __init__(self,x,y):
        self.name=x
        self.age=y
    def info(self):
        print('hello my name is :',self.name)#(self)
        print('my age is :',self.age)
s1=student('ganesh',24)
s1.info()
print(s1.name,[s1.age])#(object reference)

