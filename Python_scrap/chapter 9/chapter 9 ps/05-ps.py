with open("donkey.txt")as f:
    content=f.read()
if ("pythons"in content):
    print ("python word on the file")
else:
    print ("python is not in the file")