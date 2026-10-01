marks=int(input("enter the marks"))

if (marks<=100 and marks>=90):
    print ("your grade is EX")
elif(marks<90 and marks>=80):
    print ("your grade is A")
elif(marks<80 and marks>=70):
    print ("your grade is b")
elif(marks<70 and marks>=60):
    print ("your grade is c")
elif(marks<60 and marks>=50):
    print ("your grade is d")
elif(marks<50):
    print ("you are fail")