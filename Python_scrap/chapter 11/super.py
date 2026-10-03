class employee:
    def __init__(self):
        print ("this is empoyee construcore")
    comney="ITC"
    def show(self):
        print(f"the compney name is {self.comney}")

class coder:
    def __init__(self):
        print ("this is coder construcore")
        super().__init__()
    language="python"
    def programming(self):
        print (f"the language is {self.language}")

class programmer(employee,coder):
    def __init__(self):
        print ("this is programmer construcore")
        super().__init__()
    comney="ITC infotech"
    def showlanguage(self):
        print (f"the compney name is {self.comney}")

a=employee()
b=programmer()
b.show()
b.programming()
b.showlanguage()

print (a.comney,b.comney)   