def get_n_column(x,f,n):
    oldf=[]
    for i in range(len(f)):
        oldf.append(f[i])
    for i in range(n,len(x)):
        f[i]=(oldf[i]-oldf[i-1])/(x[i]-x[i-n])
    return f
x=float(input())

xi=[0.40,0.55,0.65,0.80,0.90]
fi=[0.41075,0.57815,0.69675,0.88811,1.02652]
for i in range(1,5):
      f =get_n_column(xi,fi,i)
sum=f[0]
for i in range(1,len(xi)):
    m=1.0
    for j in range(i):
        m*=(x-xi[j])
    sum+=(f[i]*m)
print("%.3f"%sum)