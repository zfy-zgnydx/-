import math

inp = input().split(' ')
a = float(inp[0])
b = float(inp[1])
n = int(inp[2])

def fx(x):
        return math.sqrt(4-math.sin(x)**2)

h=(b-a)/n
sum=fx(a)+fx(b)
for i in range(1,n):
    sum+=(fx(a+i*h))*2
for i in range(n):
    sum+=(fx(a+i*h+h/2))*4
sum*=h/6
print("%.5f"%sum)