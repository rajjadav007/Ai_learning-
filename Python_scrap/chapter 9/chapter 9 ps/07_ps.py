with open ("og.txt")as f:
    readlines=f.readlines()

lineno=1
for line in readlines:
    if ("python" in line):
        print (f"yes python is line on the {lineno}")
        break
    lineno+=1
else:
    print ("no not python in any lines ")
