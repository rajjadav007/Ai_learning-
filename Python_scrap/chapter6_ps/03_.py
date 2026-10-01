p1="Make a lot ofmoney" 
p2="buy now" 
p3="subscribe this"
p4="click this"

message=input("enter your commant")

if (p1 in message or p2 in message or p3 in message or p4 in message):
    print ("this is spam message")
else:
    print ("this is not spam ")