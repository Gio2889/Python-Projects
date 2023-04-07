# @Author: Giovanni G. Baez Flores
# @Date:   2018-12-12T10:45:43-06:00
# @Email:  gbaez89@gmail.com
# @Last modified by:   Giovanni G. Baez Flores
# @Last modified time: 2018-12-12T10:46:05-06:00



import numpy as np
from math import sin
import pandas as pd
import matplotlib.pyplot as plt
np.set_printoptions(precision=64,floatmode='maxprec')

def rk4(arr,func,dim,step):
    """" Takes an n-dim arrays x0 and func, calculates k(1-4),
    then output x+1 term. The func array determines the ODE
    to be solved"""
    k1=np.empty(dim)
    k2=np.empty(dim)
    k3=np.empty(dim)
    k4=np.empty(dim)
    xk=np.empty(dim)
    for i in range(dim):
        k1[i]=func[i](arr)*step
    xk = arr + k1*0.5
    for i in range(dim):
        k2[i]=func[i](xk)*step
    xk = arr + k2*0.5
    for i in range(dim):
        k3[i]=func[i](xk)*step
    xk = arr + k3
    for i in range(dim):
        k4[i]=func[i](xk)*step
    arr = arr + ( k1 + 2*(k2+k3) + k4 )/6
    return arr

""""There a way to circumven the for loops with np.vectorize
     like this:
     def build(a,b):
         return a(b)
     vecbuild = np.vectorize(build)

     then call like k1=vecbuild(func,arr)
"""
