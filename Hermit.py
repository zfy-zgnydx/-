xi=float(input())

x=[1,2]
y=[0,0.693147]
yi=[1,0.5]

h=x[1]-x[0]

def f0(x):
    return (1-x)*(1-x)*(1+2*x)
def f1(x):
    return x*(1-x)*(1-x)

h00=f0((xi-x[0])/(x[1]-x[0]))
h10=f0((x[1]-xi)/(x[1]-x[0]))
h01=h*f1((xi-x[0])/(x[1]-x[0]))
h11=(-1)*h*f1((x[1]-xi)/(x[1]-x[0]))

h=y[0]*h00+y[1]*h10+yi[0]*h01+yi[1]*h11
print("%.5f"%h)