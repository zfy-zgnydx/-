import math 

def f(x):
    return math.exp(x)

def Guess_Chebyshev(n):
    x=[]
    sum=0
    for i in range(n+1):
        x.append(math.cos((2*i+1)*math.pi/(2*n+2)))
    for i in range(len(x)):
        sum+=f(x[i])
    sum*=math.pi/(n+1)
    return sum

n=int(input())
print("%.6f"%Guess_Chebyshev(n))


