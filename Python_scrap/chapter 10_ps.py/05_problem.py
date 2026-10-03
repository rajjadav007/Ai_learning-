class train:
    
    def __init__(self,trainno):
        self.trainno=trainno
    
    def book(self,fro,to):
        print (f"the train number is {self.trainno} and from {fro} to {to} this ")
    def getstatus(self,fro,to):
        print (f"the train number is {self.trainno} on time  ")
    def fare(self,fro,to):
        print (f"the train number is {self.trainno} and from the{fro} to {to} this ")

a=train(12345)
a.book("rajkot","banglore")
a.getstatus("rajkot","banglore")
a.fare("rajkot","banglore")