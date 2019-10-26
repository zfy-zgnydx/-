import math

inp = input().split(' ')
a = float(inp[0])
b = float(inp[1])

def fx(x):
    if x!=0:
        return math.sin(x)/x
    else:
        return 1

h=(b-a)/4
ya=fx(a)
yb=fx(b)
y1=fx(a+h)
y2=fx(a+h*2)
y3=fx(a+h*3)

s=(7*ya+32*y1+12*y2+32*y3+7*yb)*(b-a)/90
print("%.5f"%s)