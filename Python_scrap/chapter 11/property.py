class employee:
    a=1
    @classmethod
    def show (cls):
        
        print (f"the class decorater value is {cls.a}")
    
b=employee()
b.a=44
b.show()