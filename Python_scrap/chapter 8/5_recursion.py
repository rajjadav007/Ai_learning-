def fectorial(n):
    if n==1 or   n==0:
            return 1
    return n*fectorial(n - 1)

n=int(input("enter the number: "))
print (f"the fectorila of number is :{fectorial(n)}")