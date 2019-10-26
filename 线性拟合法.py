x1=float(input())

x=[0.4,1.0,2.0,4.0,10]
y=[0.4053,1.0071,2.0167,3.9963,10.0165]

p00=len(x)
p01=0
p11=0
q0=0
q1=0
for i in range(len(x)):
    p01+=x[i]
    p11+=x[i]*x[i]
    q0+=y[i]
    q1+=x[i]*y[i]

b=(p00*q1-p01*q0)/(p00*p11-p01*p01)
a=(q0-p01*b)/p00

c=a+b*x1
print("%.2f"%c)
