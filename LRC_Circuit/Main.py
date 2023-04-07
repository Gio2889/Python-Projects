# @Author: Giovanni G. Baez Flores
# @Date:   2018-12-12T10:45:43-06:00
# @Email:  gbaez89@gmail.com
# @Last modified by:   Giovanni G. Baez Flores
# @Last modified time: 2018-12-12T10:46:02-06:00



import numpy as np
from RK4_optimized import rk4
from Euler_Method import make1darray
from math import sqrt,atan
import pandas as pd
import matplotlib.pyplot  as plt
from mpl_toolkits.mplot3d import Axes3D

"""Solves the differential equation:
d2 I/dt2 =  dI/dt(1/LC) + I/LRC  - V0/LRC Sin(omega*t) """

"""The analytical solution is given by:
i(t)=(V0/|Z|) exp(-i (omega t +theta))
Z=(R2 + (1/omega*C - omega*L)^2)^1/2
theta= arctan( (1/omega*C - omega*L)/R )
"""
#constants array (R,L,C,om,V,(Z),(thet))
def absZ(R,L,C,om):
    res=np.sqrt(R**2 - ((1/(C*om)) - (L*om))**2)
    return res
def thet(R,L,C,om):
    res=atan(((1/(C*om)) - (L*om))/R)
    return res
c=np.array([900,10,6,0.5,20])
c=np.append(c,absZ(c[0],c[1],c[2],c[3]))
c=np.append(c, thet(c[0],c[1],c[2],c[3]))

"""Printing Analytical Sol"""

t=np.linspace(0,100,1000)
rei=(c[4]/c[5])*(np.cos(c[3]*t + c[6]))
imi=(c[4]/c[5])*(np.sin(c[3]*t + c[6]))
dfan=pd.DataFrame({'t':t,'Re i(t)':rei,'Im i(t)':imi})

#plt.plot(dfan.iloc[:,0],dfan.iloc[:,1],'b-', label = 'Re I(t)')
#plt.plot(dfan.iloc[:,0],dfan.iloc[:,2],'r-', label = 'Im I(t)')
#plt.legend(loc='upper left')
#plt.show()

r=np.linspace(0.001,1000,100)
l=np.linspace(0,20,100)
carr=np.linspace(0,6,100)
om=np.linspace(0.01,2,100)
zarr=np.empty([100,100])
theta=np.empty([100,100])
reI=np.empty([100,100])
imI=np.empty([100,100])
for i in range(100):
    for j in range(100):
        zarr[i,j]=absZ(r[i],1,1,om[j])
        theta[i,j]=thet(r[i],1,1,om[j])

#        zarr[i,j]=np.sqrt(r[i]**2 - ((1/(carr[99]*om[j])) - (l[99]*om[j]))**2)

r,om = np.meshgrid(r,om)
#zarr=np.sqrt(r**2 - ((1/(carr[99]*om)) - (l[99]*om))**2)
"""
ax1 = fig.add_subplot(111,projection='3d')
ax2 = fig.gca(projection='3d')
type(ax1)
type(ax2)
make the same type of object
"""
v0=10

fig = plt.figure()
ax = fig.add_subplot(111,projection='3d')
ax.plot_surface(r,om,v0/zarr,label='Abs(Z)')
ax.set_ylabel('omega')
ax.set_xlabel('resistance')
plt.show()
