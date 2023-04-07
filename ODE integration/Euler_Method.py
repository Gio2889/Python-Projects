import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import pandas as pd
np.set_printoptions(precision=64,floatmode='maxprec')
step_size=20000
kappa=2
t1=0
t2=100
x0=0
v0=1

def make1darray(x1,x2,dx):
    min = dx*x1
    max = dx*x2
    list = [t for t in range(min,max,x2)]
    nplist = np.array(list)/dx
    return nplist

tarray = make1darray(t1,t2,step_size)

xarray=np.array([x0])
varray=np.array([v0])



""""Euler_Solver"""
for i in range(1,(len(tarray))):
    varray=np.append(varray,varray[i-1]-(tarray[i]-tarray[i-1])*kappa*xarray[i-1])
    xarray=np.append(xarray,xarray[i-1]+(tarray[i]-tarray[i-1])*varray[i-1])

sol=np.sin(sqrt(kappa)*tarray)

df=pd.DataFrame({'time':tarray,'Sin(wt)':sol,'x(t)':xarray,'v(t)':varray,'err':(xarray-sol)})
df[:10]
#plt.plot(tarray,xarray)
plt.plot(df.iloc[:,0],df.iloc[:,1],'b-', label = 'Analytic')
plt.plot(df.iloc[:,0],df.iloc[:,2],'g-', label = 'Euler')
#plt.plot(df.iloc[:,0],df.iloc[:,3],'r-', label = ' v(t): Euler')
plt.legend(loc='upper left')
plt.xlabel('time')
plt.ylabel('x(m),v(m/s)')
plt.show()
plt.plot(df.iloc[:,0],df.iloc[:,4],'r-', label = ' Error')
plt.xlabel('time')
plt.ylabel('Error')
plt.show()
