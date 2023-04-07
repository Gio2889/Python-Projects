import numpy as np
import pandas as pd
from math import sqrt,sin,cos
import matplotlib.pyplot  as plt
from mpl_toolkits.mplot3d import Axes3D

PR=4.0
PW=2.0
MR=1.0
MW=14.0

parr=np.linspace(0,3.14,200,endpoint=True)
pdf=pd.DataFrame(parr,columns=['time (s)'])
pdf['mx']=PR*np.cos(PW*pdf.iloc[:,0])+MR*np.cos(MW*pdf.iloc[:,0])
pdf['my']=PR*np.sin(PW*pdf.iloc[:,0])+MR*np.sin(MW*pdf.iloc[:,0])
pdf['px']=PR*np.cos(PW*pdf.iloc[:,0])
pdf['py']=PR*np.sin(PW*pdf.iloc[:,0])

fig=plt.figure(figsize=(10,10))
orbit = fig.add_subplot(1,1,1)
orbit.plot(pdf['px'],pdf['py'],'bo')
orbit.plot(pdf['mx'],pdf['my'],'r-o')
orbit.grid( which='both',axis='both',color='gray', linestyle='-', linewidth=1)
orbit.set_aspect('equal')
plt.show()
