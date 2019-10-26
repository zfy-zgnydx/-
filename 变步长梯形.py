import math

x=[]
n=1
a,b,e=input().split()
x.append(float(a))
x.append(float(b))
e=float(e)
def f(x):
    return math.sin(x)/x
def t(a,b):
    return (b-a)*(f(a)+f(b))/2
def T(a,b,n):
    h=(b-a)/n
    sum=0
    for i in range(n):
        sum+=t(a+i*h,a+i*h+h)
    return sum
T1=T(x[0],x[1],n)
n*=2
T2=T(x[0],x[1],n)
while(abs(T2-T1)>e):
    T1=T2
    n*=2
    T2=T(x[0],x[1],n)
print("%.6f"%T2)