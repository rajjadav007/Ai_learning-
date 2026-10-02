import random

computer=random.choice([-1,1,0])
str=input("enter the choice: ")
youdict={"s":1,"w":-1,"g":0}
reversedict={1:"snake",-1:"water",0:"gun"}

you=youdict[str]

print (f"you choose {reversedict[you]}\n Computer choose {reversedict[computer]}")

if (computer==you):
    print ("its draw")
else:
    if (computer==-1 and you==1):
        print ("you win")
    elif(computer==-1 and you==0):
        print ("you lose")
    elif(computer==1 and you==-1):
        print ("you lose")
    elif(computer==1 and you==0):
        print ("you win")
    elif(computer==0 and you==1):
        print ("you win")
    elif(computer==0 and you==-1):
        print ("you lose")
    else:
        print ("something wron")