import math

e=2.71828
def f0(x):
    return math.pow(e,(x*x-1))
x=[float(i) for i in input().split()]
y=[]
a=[]
for i in range(5):
    y.append(f0(x[i]))
m=float(input())
for i in range(4):
    sum=0
    for j in range(i+2):
        p=1
        for k in range(i+2):
            if k!=j:
                p*=((m-x[k])/(x[j]-x[k]))
        sum+=p*y[j]
    print("%.4f"%(sum),end=' ')