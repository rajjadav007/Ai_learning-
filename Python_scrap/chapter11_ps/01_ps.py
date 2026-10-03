class twodvector:
    def __init__(self,j,i):
        self.i=i
        self.j=j
    def show(self):
        print (f"the twodvectore value is {self.i}i and {self.j}j")

class threedvector(twodvector):
    def __init__(self,j,i,k):
        super().__init__(i,j)
        self.k=k
    def show (self):
        print (f"the twodvectore value is {self.i}i and {self.j}j and {self.k}k")
a=twodvector(1,2)
b=threedvector(1,2,3)
a.show()
b.show()