a=int(input("enter the first number"))
b=int(input("enter the first number"))

if (b==0):
    raise ZeroDivisionError ("sorry you can devided number in to zero this is zerodeivision error")
else:
    print (f"number divided is {a/b}")