class student:
    cname='Ganesh'
    def __init__(self,x,y):
        self.name=x
        self.rollno=y
    def display(self):
        print('hello myself is:',self.name)
        print('my roll no is:',self.rollno)
    @classmethod
    def getcollegename(cls):
        print('College Name:',cls.cname)

s1=student('ganesh',100)
s2=student('shiva',101)
s3=student('rahul',234)
s1.display()
s2.display()
student.getcollegename()