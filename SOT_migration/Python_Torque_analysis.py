# @Author: Giovanni G. Baez Flores
# @Date:   2020-07-22T14:29:37-05:00
# @Email:  gbaez89@gmail.com
# @Last modified by:   Giovanni G. Baez Flores
# @Last modified time: 2020-11-20T16:16:30-06:00



import os
import sys
from itertools import accumulate,chain
from math import sqrt,sin,cos
import scipy as sp
from scipy import special
from scipy.misc import derivative
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
###############################################################################

for i in range(1,14):
    datacmp=pd.read_csv('CoMPt_Harm_zlayer_'+str(i)+'.out',names=['A1','A2','A3','A4','B1','B2','B3','B4'],delimiter=' ')
    if i==1:
        arrcmp=datacmp.mean().to_numpy()
    elif i==2:
        arrcmp=np.concatenate(([arrcmp],[datacmp.mean().to_numpy()]),axis=0)
    else:
        arrcmp=np.concatenate((arrcmp,[datacmp.mean().to_numpy()]),axis=0)
for i in range(1,17):
    datacpp=pd.read_csv('Harm_zlayer_'+str(i)+'.out',names=['A1','A2','A3','A4','B1','B2','B3','B4'],delimiter=' ')
    if i==1:
        arrcpp=datacpp.mean().to_numpy()
    elif i==2:
        arrcpp=np.concatenate(([arrcpp],[datacpp.mean().to_numpy()]),axis=0)
    else:
        arrcpp=np.concatenate((arrcpp,[datacpp.mean().to_numpy()]),axis=0)
df=pd.DataFrame(arrcmp,columns=['A1','A2','A3','A4','B1','B2','B3','B4'])
df['Z']=df.index +1
df2=pd.DataFrame(arrcpp,columns=['A1','A2','A3','A4','B1','B2','B3','B4'])
df2['Z']=df2.index +1

df
df.to_csv('cmp_70_2.out',index=False)
df2.to_csv('cpp_70_2.out',index=False)



df.plot(style=['+-','o-','.--','s:'])


pl1 = df.plot(x='Z',y='A1', kind='scatter',c='blue', label="A1 CMP",style=['+-'],s=150,zorder=1)
pl1.set_yticks(np.linspace(-0.001,0.0015,6), minor=True )
pl1.grid('on', which='minor', axis='y' )
pl1.grid('off', which='major', axis='y' )
df2.plot(x='Z',y='A1', kind='scatter',ax=pl1,c='Green', label="A1 CPP",marker='>',s=150, zorder=2)
df.plot(x='Z',y='B1', kind='scatter',ax=pl1,c='red', label="B1 CMP",marker='s',s=100, zorder=2)
df2.plot(x='Z',y='B2', kind='scatter',ax=pl1,c='purple', label="B1 CPP",marker='s',s=100, zorder=2)
plt.show()
