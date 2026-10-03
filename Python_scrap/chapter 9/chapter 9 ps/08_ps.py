with open ("donkey.txt","r")as f:
    content=f.read()

with open("donkey1.txt","w")as f:
    f.write(content)