# @Author: Giovanni G. Baez Flores
# @Date:   2019-02-01T12:42:01-06:00
# @Email:  gbaez89@gmail.com
# @Last modified by:   Giovanni G. Baez Flores
# @Last modified time: 2019-02-04T19:28:14-06:00

import numpy as np
import pandas as pd
import matplotlib.pyplot  as plt
from mpl_toolkits.mplot3d import Axes3D

filename='DOSCAR'

reader = open(filename,"r")
data=[]
for i, line in enumerate(reader.readlines()):
    splitted = line.split()
    if i !=3 and i !=4:
        for item in range(len(splitted)):
            splitted[item] = float(splitted[item])
    data.append(splitted)
reader.close()
atoms = int(data[0][1])
ef=data[5][3]
ne=int(data[5][2])
dos=pd.DataFrame(data[6:6+ne],columns=['Energy','DOS(up)','DOS(dw)','iDOS(up)','iDOS(dw)'])
linecount=6+ne+1
pddict={}
for i in range(atoms):
    df = pd.DataFrame(data[linecount:linecount+ne],columns=['Energy','DOS_S_(up)','DOS_S_(dw)','DOS_Py_(up)','DOS_Py_(dw)','DOS_Pz_(up)','DOS_Pz_(dw)','DOS_Px_(up)','DOS_Px_(dw)','DOS_Dxy_(up)','DOS_Dxy_(dw)','DOS_Dyz_(up)','DOS_Dyz_(dw)','DOS_Dz2-r2_(up)','DOS_Dz2-r2_(dw)','DOS_Dxz_(up)','DOS_Dxz_(dw)','DOS_D_x2-y2(up)','DOS_D_x2-y2(dw)'])
    df['Sum(up)']=df.iloc[:,1::2].sum(axis=1)
    df['Sum(dw)']=df.iloc[:,2:18:2].sum(axis=1)
    pddict[i]=df
    linecount = linecount+ne+1



for i in range(atoms):
    if i <=5:
        atom='Pt'
        num = 6 - i
    elif i > 5:
        atom = 'Co'
        num = i - 5
    name = atom + ' ' + str(num)
    fig=plt.figure(figsize=(10,10))
    frplot = fig.add_subplot(1,1,1)
    frplot.set_ylabel("DOS")
    frplot.set_xlabel("eV")
    frplot.plot(pddict[i]['Energy'],pddict[i]['Sum(up)'],color='red')
    frplot.plot(pddict[i]['Energy'],-pddict[i]['Sum(dw)'],color='blue')
    frplot.set_facecolor('lightgray')
    frplot.set_title(name,fontdict ={'fontsize': 18})
    frplot.grid(which='both',axis='both',color='gray', linestyle='-', linewidth=1)
    plt.savefig('dosplots_vasp/'+name+"_dos.png")
