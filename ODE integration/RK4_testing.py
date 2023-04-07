import numpy as np
import math as m
import matplotlib.pyplot as plt
import pandas as pd
from RK4_optimized import rk4
from Euler_Method import make1darray

np.set_printoptions(precision=64,floatmode='maxprec')

""""
First test Harmonice oscillator
Analytical Sol.
 x(t) = A*Sin(om*t)
 v(t) = om*A*Cos(om*t)
 testing three cases
Case A:
 x(0)=0m
 v(0)=1m/s
Case B:
 x(0)= 0 m
 v(0)= 3 m/5
Case C:
  x(0)=5 m
  v(0)=-2 m/s
  """
  
""""Case A
uncommet to solve
om=0.5
def acc(x):
    return -(om**2)*x[1]
#    return 0.9*(1 - x[1]*x[1])*x[0] - x[1] + m.sin(om*x[2])
def vel(x):
    return x[0]
def time(x):
    return 1
f=[acc,vel,time]
bc=[1,0,0]
steps=10000
xmax=100
hs=xmax/steps
d=3
sol=np.empty([steps,d])
sol[0]=bc
sl=bc
for i in range(steps):
    sol[i]=sl
    sl=rk4(sol[i],f,d,hs)

"""
"""
Case B
Un comment to solve
om=0.5
def acc(x):
    return -(om**2)*x[1]
#    return 0.9*(1 - x[1]*x[1])*x[0] - x[1] + m.sin(om*x[2])
def vel(x):
    return x[0]
def time(x):
    return 1
f=[acc,vel,time]
bc=[3,0,0]
steps=10000
xmax=100
hs=xmax/steps
d=3
sol=np.empty([steps,d])
sol[0]=bc
sl=bc
for i in range(steps):
    sol[i]=sl
    sl=rk4(sol[i],f,d,hs)
df=pd.DataFrame(sol,columns=['v(t)','x(t)','t'])
x=np.array(bc[:1])
amp=x[0]/om
tarray =make1darray(0,xmax,steps)

solx=amp*np.sin(om*tarray)
solv=amp*om*np.cos((om)*tarray)
"""

"""
Case C:
"""

om=0.5
def acc(x):
    return -(om**2)*x[1]
#    return 0.9*(1 - x[1]*x[1])*x[0] - x[1] + m.sin(om*x[2])
def vel(x):
    return x[0]
def time(x):
    return 1
f=[acc,vel,time]
bc=[-2,5,0]
steps=10000
xmax=100
hs=xmax/steps
d=3
sol=np.empty([steps,d])
sol[0]=bc
sl=bc
for i in range(steps):
    sol[i]=sl
    sl=rk4(sol[i],f,d,hs)
df=pd.DataFrame(sol,columns=['v(t)','x(t)','t'])
x=np.array(bc[:2])
amp1=x[1]
amp2=x[0]/om
tarray =make1darray(0,xmax,steps)
solx=amp1*np.cos(om*tarray)+amp2*np.sin(om*tarray)
solv=om*(-amp1*np.sin(om*tarray)+amp2*np.cos(om*tarray))
df['t arr']=tarray
df['Sol x(t)']=solx
df['Sol v(t)']=solv
plt.plot(df.iloc[:,2],df.iloc[:,1],'g-',label='RK4')
plt.plot(df.iloc[:,3],df.iloc[:,4],'r-',linestyle='-.',label='Analytical')
plt.legend(loc='upper right')
plt.xlabel('time')
plt.ylabel('x(m)')
plt.grid(True)
plt.show()
plt.plot(df.iloc[:,2],df.iloc[:,0],'g-',label='RK4')
plt.plot(df.iloc[:,3],df.iloc[:,5],'r-',linestyle='-.',label='Analytical')
plt.legend(loc='upper right')
plt.xlabel('time')
plt.ylabel('v(m/s)')
plt.grid(True)
plt.show()
