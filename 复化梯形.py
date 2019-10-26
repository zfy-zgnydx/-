import math

inp = input().split(' ')
a = float(inp[0])
b = float(inp[1])
n = int(inp[2])

def fx(x):
        return math.log(x)

h=(b-a)/n
sum=fx(a)+fx(b)
for i in range(1,n):
    sum+=(fx(a+i*h))*2
sum*=h/2
print("%.5f"%sum)