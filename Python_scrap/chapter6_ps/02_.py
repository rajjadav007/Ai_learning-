subject1=int(input("enter the subject 1: "))
subject2=int(input("enter the subject 2: "))
subject3=int(input("enter the subject 3: "))

total=(subject1+subject2+subject3)/3

if (total>=40 and subject1>=33 and subject2>=33 and subject3>=33):
    print ("you are pass",total)
else:
    print ("you are fail ",total)