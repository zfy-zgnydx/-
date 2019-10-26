import math

x=[math.pi/6,math.pi/4,math.pi/3]
y=[1/2,math.sqrt(2)/2,math.sqrt(3)/2] 
p00=len(x)
p01=0
p11=0
p12=0
p22=0
q0=0
q1=0
q2=0
for i in range(len(x)):
    p01+=x[i]
    p11+=x[i]*x[i]
    p12+=x[i]*x[i]*x[i]
    p22+=x[i]*x[i]*x[i]*x[i]
    q0+=y[i]
    q1+=x[i]*y[i]
    q2+=x[i]*y[i]*x[i]
a1=p00-p11*p11/p22
a2=p01-p11*p12/p22
b1=a2
b2=p11-p12*p12/p22
m=q0-p11*q2/p22
n=q1-p12*q2/p22
a=(m-b1*n/b2)/(a1-a2*b1/b2)
b=(n-a2*a)/b2
c=(q2-p11*a-p12*b)/p22
k=float(input())
f=a+b*k+c*k*k
print("%.5f"%f)