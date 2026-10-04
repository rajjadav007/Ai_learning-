from functools import reduce

a=[1,2,3,4,5,6,7,8,9,0,55,66,100]

def greate(a,b):
    if (a>b):
        return a 
    return b

print (reduce(greate,a))
