a=int(input("enter the number 1 "))
b=int(input("enter the number 2"))
c=int(input("enter the number 3"))
d=int(input("enter the number 4"))

if (a>b and a>c and a>d):
    print ("a is bigger number")
elif (b>a and b>c and a>d):
    print ("b is bigger number ")
elif (c>a and c>b and c>d):
    print ("c is bigger ")
else:
    print ("d is bigger ")