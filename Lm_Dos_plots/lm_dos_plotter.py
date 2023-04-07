# @Author: Giovanni G. Baez Flores
# @Date:   2019-02-04T10:04:35-06:00
# @Email:  gbaez89@gmail.com
# @Last modified by:   Giovanni G. Baez Flores
# @Last modified time: 2019-02-04T18:39:42-06:00

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot  as plt
import subprocess
import re


#cdw='C:\\Users\\gbaez\\Box Sync\\Python Projects\\Lm_Dos_plots'
cdw="C:\\Users\\Gio's surface\\OneDrive - University of Nebraska-Lincoln\\BoxMigrationUNL\\Python Projects\\Lm_Dos_plots"
#cdw="C:\\Users\\Gio's surface\\Box\\Python Projects\\Lm_Dos_plots"
datadir=os.path.join(cdw,'3S')
plotdir=os.path.join(cdw,'CoO_plots')
os.chdir(cdw)
os.chdir(datadir)
# dat=np.loadtxt('dos_1.dat',skiprows=1)
# dat2=np.loadtxt('dos_2.dat',skiprows=1)
datadic={}
atomlist=[]
for file in os.listdir():
    split=re.findall(r"[\w]+",file)
    split[0]=split[0].split('_')
    flat_list=[]
    for list in split:
        for item in list:
            flat_list.append(item)
    string=flat_list[1]+' '+flat_list[2]
    datadic[string]=np.loadtxt(file,skiprows=1)
    if (flat_list[1]+' ' not in atomlist):
        atomlist.append(flat_list[1]+' ')
os.chdir(cdw)

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

vaspdict={}
indexmap={0:10,1:9,2:8,3:7,4:6,5:11,6:4}#,7:3,8:2,9:1,10:0,11:5}
for j in range(7):
    vaspdict[j]=pddict[j]

#os.chdir(plotdir)
#atomlist=["Co1","Co2","Co3","Co4","Co5","Co6","O"]
eflmgf=0
ind=0
for item in atomlist:
    itemlist=[]
    for key, value in datadic.items():
        if key.startswith(item):
            itemlist.append(key)
    dat=datadic[itemlist[0]]
    dat2=datadic[itemlist[1]]
    fig=plt.figure(figsize=(10,10))
    frplot = fig.add_subplot(1,1,1)
    frplot.set_ylabel("DOS")
    frplot.set_xlabel("eV")
    frplot.plot(dat[:,0]+(eflmgf*13.65),dat[:,1],color='red',alpha=0.7,label = 'lm spin 1')
    frplot.plot(vaspdict[ind]['Energy']-ef,vaspdict[ind]['Sum(up)'],color='green',linestyle='-.',alpha=0.7,label = 'vasp spin 1')
    frplot.plot(dat2[:,0]+(eflmgf*13.65),-dat2[:,1],color='blue',alpha=0.7,label = 'lm spin 2')
    frplot.plot(vaspdict[ind]['Energy']-ef,-vaspdict[ind]['Sum(dw)'],color='orange',linestyle='-.',alpha=0.7,label = 'vasp spin 2')
    frplot.legend(loc='best')
    frplot.set_facecolor('lightgray')
    frplot.set_title(item,fontdict ={'fontsize': 18})
    frplot.grid(which='both',axis='both',color='gray', linestyle='-', linewidth=1)
    plt.savefig(str(item)+"_dos.png")
    ind = ind + 1
