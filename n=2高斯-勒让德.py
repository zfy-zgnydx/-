import math 

def f(x):
    return math.sqrt(x+1.5)

def Guess_Legendre(a,b):
    x=(b-a)/2
    y=(a+b)/2
    sum=5/9*f(y+x*((-1)*math.sqrt(15)/5))+8/9*f(y)+5/9*f((math.sqrt(15)/5)*x+y)
    sum*=(b-a)/2
    return sum

a,b=input().split()
a=float(a)
b=float(b)
print("%.5f"%Guess_Legendre(a,b))


