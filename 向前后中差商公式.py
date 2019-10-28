import math

def f(x):
    if x==0:
        return 1;
    else:
        return math.sin(x)/x

def g(x1,x2):
    return (f(x2)-f(x1))/(x2-x1)

def fr(x):
    h=1
    t1=g(x,x+h)
    h*=0.5
    t2=g(x,x+h)
    while(math.fabs(t2-t1)>=0.001):
        t1=t2
        h*=0.5
        t2=g(x,x+h)
    return t1

def la(x):
    h=1
    t1=g(x-h,x)
    h*=0.5
    t2=g(x-h,x)
    while(math.fabs(t2-t1)>=0.001):
        t1=t2
        h*=0.5
        t2=g(x-h,x)
    return t1

def mid(x):
    h=1
    t1=g(x-h,x+h)
    h*=0.5
    t2=g(x-h,x+h)
    while(math.fabs(t2-t1)>=0.001):
        t1=t2
        h*=0.5
        t2=g(x-h,x+h)
    return t1

x=float(input())
print("%.3f"%fr(x),end=" ")
print("%.3f"%la(x),end=" ")
print("%.3f"%mid(x))