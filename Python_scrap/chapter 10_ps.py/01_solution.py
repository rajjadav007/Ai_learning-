class employee:
    compney="microsoft"
    def __init__(self,name,salary,pin):
        self.name=name
        self.salary=salary
        self.pin=pin

p=employee(name="raj",salary=10000,pin=360004)
print (f"the name of is {p.name} salary is {p.salary} and pin is {p.pin}")
p=employee(name="harsh",salary=12000,pin=360009)
print (f"the name of is {p.name} salary is {p.salary} and pin is {p.pin}")