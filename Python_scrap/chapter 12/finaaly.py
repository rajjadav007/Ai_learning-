try:
    a=int(input("enter the number"))
    print (a)

except Exception as e :
    print (e)

finally:
    print ("hello i am in finnaly block")