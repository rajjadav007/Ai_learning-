def divisible(n):
    if (n%5==0):
        return True
    return False

a=[1,2,3,4,5,6,7,8,9,0,55,66,100]

f=list(filter(divisible,a))
print (f)