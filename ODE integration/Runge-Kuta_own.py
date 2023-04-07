import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import pandas as pd
from Euler_Method import make1darray
np.set_printoptions(precision=64,floatmode='maxprec')
step_size=10000
kappa=2
t1=0
t2=40
x0=0.
v0=1.

tlist = make1darray(t1,t2,step_size)
tarray=np.array(tlist)
tarray=tarray/step_size
xarray=np.array([x0])
varray=np.array([v0])




def x(l,arr):
    s = arr[l]
    return s

def v(l,arr):
    s = (-kappa*arr[l])
    return s

def k1(i,f,h,arr):
    res=h*f(i,arr)
    return res

def  k2(i,f,h,arr):
    res=h*(f(i,arr) + k1(i,f,h,arr)/2 )
    return res

def  k3(i,f,h,arr):
    res=h*(f(i,arr) + k2(i,f,h,arr)/2)
    return res

def  k4(i,f,h,arr):
    res=h*(f(i,arr) + k3(i,f,h,arr))
    return res

def rk4(xr,yr,yr2,f,g):
    for j in range(1,len(xr)):
        dx=(xr[j]-xr[j-1])
        yp=yr[j-1]+(k1(j-1,f,dx,yr2)/6)+(k2(j-1,f,dx,yr2)/3)+(k3(j-1,f,dx,yr2)/3)+(k4(j-1,f,dx,yr2)/6)
        yp2=yr2[j-1]+(k1(j-1,g,dx,yr)/6)+(k2(j-1,g,dx,yr)/3)+(k3(j-1,g,dx,yr)/3)+(k4(j-1,g,dx,yr)/6)
        yr=np.append(yr,yp)
        yr2=np.append(yr2,yp2)
    return (yr,yr2)
numsol=rk4(tarray,varray,xarray,v,x)
solx=(1/sqrt(kappa))*np.sin(sqrt(kappa)*tarray)
solv=np.cos(sqrt(kappa)*tarray)
numsol[1][:10]

df=pd.DataFrame({'time':tarray,'Sol x(t)':solx,'x(t)':numsol[1],'Sol v(t)':solv,'v(t)':numsol[0],'err x':(solx-numsol[1]),'err v':(solv-numsol[0])})
df[:10]

plt.plot(df.iloc[:,0],df.iloc[:,1],'b-', label = 'Analytic')
plt.plot(df.iloc[:,0],df.iloc[:,2],'g-', label = 'RK4')
plt.legend(loc='upper left')
plt.xlabel('time [s]')
plt.ylabel('x(t) [m]')
plt.show()

plt.plot(df.iloc[:,0],df.iloc[:,3],'b-', label = 'Analytic')
plt.plot(df.iloc[:,0],df.iloc[:,4],'g-', label = 'RK4')
plt.legend(loc='upper left')
plt.xlabel('time [s]')
plt.ylabel('v(t) [m/t]')
plt.show()

plt.plot(df.iloc[:,0],df.iloc[:,5],'g-', label = ' Error x(t)')
plt.plot(df.iloc[:,0],df.iloc[:,6],'r-', label = ' Error v(t)')
plt.legend(loc='upper left')
plt.xlabel('time')
plt.ylabel('Error')
plt.show()
