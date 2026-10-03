class calculator:
    def __init__(self,n):
        self.n=n

    def add(self):
        print (f"the squre of number  is {self.n*self.n}")
    def cube(self):
        print (f"the squre of number is {self.n*self.n*self.n}")
    def root(self):
        print (f"the squre of number is {self.n**1/2}")

a=calculator(4)
a.add()
a.cube()
a.root()
        