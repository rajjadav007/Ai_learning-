class employee:
    comney="ITC"
    def show(self):
        print(f"the compney name is {self.comney}")

class coder:
    language="python"
    def programming(self):
        print (f"the language is {self.language}")

class programmer(employee,coder):
    comney="ITC infotech"
    def showlanguage(self):
        print (f"the compney name is {self.comney}")

a=employee()
b=programmer()
b.show()
b.programming()
b.showlanguage()

print (a.comney,b.comney)