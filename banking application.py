import sys
class customer:
    bankname='Indian bank'
    def __init__(self,name,balance=0):
        self.name=name
        self.balance=balance
    def deposit(self,amt):
        self.balance=self.balance+amt
        print('after deposit the balance is:',self.balance)
    def withdraw(self,amt):
        if amt>self.balance:
            print('insufficient funds')
            sys.exit()
        self.balance=self.balance-amt
        print('after withdraw the balance is:',self.balance)
print('welcome to',customer.bankname)
name=input('enter your name:')
c=customer(name)
while True:
    print('d-deposit\nw-withdraw\ne-exit')
    option=input('choose your option:')
    if option.lower()=='d':
        amt=float(input('enter the amount to deposit:'))
        c.deposit(amt)
    elif option.lower()=='w':
        amt=float(input('enter the amount to withdraw:'))
        c.withdraw(amt)
    elif option.lower()=='e':
        print('thanks for banking')
        sys.exit()
    else:
        print('choose valid option')