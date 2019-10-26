
import math

inp = input().split(' ')
a = float(inp[0])
b = float(inp[1])

def fx(x):
    return x*x*math.exp(x)

ya=fx(a)
yb=fx(b)
y0=fx((a+b)/2)

s=(ya+yb+4*y0)*(b-a)/6
print("%.5f"%s)