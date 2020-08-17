class task:
    def __init__(self,q):
        self.q=q
    def even(self):
        print(list(range(0,self.q,2)))
    def odd(self):
        print(list(range(1,self.q,2)))
    def prime(self):
        for i in range(self.q):
            if i>1:
                for j in range(2,i):
                    if i%j==0:
                        print(i,'not prime')
                        break
                else:
                    print(i,'prime')
y=task(50)
y.even()
y.odd()
y.prime()


