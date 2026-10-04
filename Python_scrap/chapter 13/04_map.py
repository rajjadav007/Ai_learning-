from functools import reduce

l=[1,2,3,4]

square=lambda x:x*x
sqllist=map(square,l)
print (list(sqllist))


def even(n):
    if (n%2==0):
        return True
    return False
onlyeven=filter(even,l)
print(list(onlyeven))


def sum(a,b):
    return a+b
print (reduce(sum,l))