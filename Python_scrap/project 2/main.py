import random
n=random.randint(1,100)
a=-1
guesses=0

while(a!=n):
    a=int(input("guess number"))
    if(a>n):
        print ("lower number please")
        guesses +=1
    elif(a<n):
        print ("high number please")
    guesses +=1

print (f"you have gueess the number of attempt is {guesses}")