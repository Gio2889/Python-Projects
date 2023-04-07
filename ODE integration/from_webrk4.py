import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
def rKN(x, fx, n, hs):
    k1 = []
    k2 = []
    k3 = []
    k4 = []
    xk = []
    for i in range(n):
        k1.append(fx[i](x)*hs)
    for i in range(n):
        xk.append(x[i] + k1[i]*0.5)
    for i in range(n):
        k2.append(fx[i](xk)*hs)
    for i in range(n):
        xk[i] = x[i] + k2[i]*0.5
    for i in range(n):
        k3.append(fx[i](xk)*hs)
    for i in range(n):
        xk[i] = x[i] + k3[i]
    for i in range(n):
        k4.append(fx[i](xk)*hs)
    for i in range(n):
        x[i] = x[i] + (k1[i] + 2*(k2[i] + k3[i]) + k4[i])/6
    return x
def fa1(x):
    return 0.9*(1 - x[1]*x[1])*x[0] - x[1] + math.sin(0.5*x[2])

def fb1(x):
    return x[0]

def fc1(x):
    return 1

f = [fa1, fb1, fc1]
x = [1, 1, 0]
hs = 20/1000
xarray=np.empty([1000,3])
xarray[0]=x
xarray[0]
for i in range(1000):
    xarray[i]=x
    x = rKN(x, f, 3, hs)

df=pd.DataFrame(xarray,columns=['v(t)','x(t)','t'])
df[:10]

plt.plot(df.iloc[:,2],df.iloc[:,1],'g-')
plt.xlabel('time')
plt.ylabel('x(m)')
plt.grid(True)
plt.show()
