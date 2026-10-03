with open ("donkey.txt","r")as f:
    content=f.read()

with open ("rename_by_text","w")as f:
    f.write(content)