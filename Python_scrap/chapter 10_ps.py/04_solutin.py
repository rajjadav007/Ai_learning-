class calculator:
    def __init__(self,n):
        self.n=n

    def add(self):
        print (f"the squre of number  is {self.n*self.n}")
    def cube(self):
        print (f"the squre of number is {self.n*self.n*self.n}")
    def root(self):
        print (f"the squre of number is {self.n**1/2}")

    @staticmethod
    def hello():
        print ("Hello how are you all Good ")

a=calculator(4)
a.hello()
a.add()
a.hello()
a.cube()
a.root()
        