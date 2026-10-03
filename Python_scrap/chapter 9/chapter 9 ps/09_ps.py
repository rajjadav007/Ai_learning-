with open ("donkey.txt","r")as f:
    content1=f.read()

with open ("donkey1.txt","r")as f:
    content2=f.read()

if (content1==content2):
    print("yes both file are same")
else:
    print ("not both file are not same")
