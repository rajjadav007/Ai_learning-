class employee:
    comney="ITC"
    def show(self):
        print(f"the compney name is {self.comney}")

class programmer(employee):
    comney="ITC infotech"
    def showlanguage(self):
        print (f"the compney name is {self.comney}")

a=employee()
b=programmer()

print (a.comney,b.comney)