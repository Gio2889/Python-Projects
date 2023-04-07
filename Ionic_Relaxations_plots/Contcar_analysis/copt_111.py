# @Author: Giovanni G. Baez Flores <gbaez>
# @Date:   2018-12-11T12:10:39-06:00
# @Email:  gbaez89@gmail.com
# @Last modified by:   Giovanni G. Baez Flores
# @Last modified time: 2019-02-11T15:52:18-06:00


import numpy as np
import pandas as pd
import matplotlib.pyplot  as plt
from mpl_toolkits.mplot3d import Axes3D
from poscar_reader import POSCAR

orig = POSCAR('poscar.orig')
origbig= POSCAR('poscar.p9c12')
p6c6 = POSCAR('CONTCAR.pt6co6')
p6c4 = POSCAR('CONTCAR.pt6co4')
p9c12 = POSCAR('CONTCAR.pt9co12')
orig2 = POSCAR('poscar.2x2')
p25c27 = POSCAR('contcar.pt25c27.txt')
p27c25 = POSCAR('CONTCAR.pt27co25')
#forp26c26 co is ribbons pt is chekered
p26cc26 = POSCAR('CONTCAR.co.pt26co26')
p26pc26 = POSCAR('CONTCAR.pt.p26co26')
#labels = 25*["Pt"]+27*["Co"]
#labels = ['Pt','Pt','Pt','Pt','Pt','Pt','Pt','Pt','Pt','Co','Co','Co','Co','Co','Co','Co','Co','Co','Co','Co','Co']
labels = ['Pt','Pt','Pt','Pt','Pt','Pt','Co','Co','Co','Co','Co','Co','Co']
labelmix = ['Pt','Pt','Pt','Pt','Pt','Pt','Mix','Co','Co','Co','Co','Co','Co']
#labels = ['Pt','Pt','Pt','Pt','Pt','Pt','Co','Co','Co','Co']
#xc=np.linspace(0.0,12,12)
xc=np.linspace(0.0,13,13)

#distances = p9c12.inter()-np.array((9+11)*[0.81649659]+[0.0])
struc = p6c6

alatnew = struc.nalat()

alatnew/.529




#For checkered patern only
#t1=orig2.atomiccoord[6*4:6*4+4][1].copy()
#t2=orig2.atomiccoord[6*4:6*4+4][3].copy()
#orig2.atomiccoord[6*4:6*4+4][1]=t2
#orig2.atomiccoord[6*4:6*4+4][3]=t1

original = orig.cartesian(False)
pc = struc.cartesian(True)

zeroed=pc[:,2]-pc[:,2][0]
zeroed
pt=zeroed[:6]/np.sqrt(2/3)
co=zeroed[6:]/np.sqrt(2/3)-(zeroed[6:][0])/np.sqrt(2/3)
pt
co
zeroed[6]-zeroed[5]
d=(zeroed[6]-zeroed[5])/np.sqrt(2/3)

ptplus =co[5]+d+pt
ptplus


np.concatenate((co,ptplus),axis=0)


co[1:5]-co[0:4]
ptplus[1:5]-ptplus[0:4]
np.average(co[1:5]-co[0:4])
d
pta=np.average(ptplus[1:5]-ptplus[0:4])
pta
co
ptstart=co[5]+d
ptstart
ptstart+pta
shiftso = np.full((orig2.atoms-4,3),0,'float64')
shiftspc = np.full((orig2.atoms-4,3),0,'float64')
shiftdiff =  np.full((orig2.atoms-4,3),0,'float64')


for j in range(0,struc.atoms-4,4):
    for i in range(4):
        for z in range(3):
            shiftso[j+i,z] = original[j+i+4,z] - original[j+i,z]
            shiftspc[j+i,z] = pc[j+i+4,z] - pc[j+i,z]
            shiftdiff[j+i,z] = shiftspc[j+i,z] - shiftso[j+i,z]



shiftdiff2 = np.concatenate((shiftdiff,np.full((4,3),0,'float64')))
#np.nditer(shiftso)
#np.ndindex(shiftso.shape)


atoms=struc.atoms
averagez = np.full((int(struc.atoms/4)),0,'float64')
avgo = averagez.copy()


for j in range(0,struc.atoms,4):
    avgo[int(j/4)] = np.average(original[j:j+4,2])

for j in range(0,struc.atoms,4):
    averagez[int(j/4)] =  np.average(pc[j:j+4,2])

avgshiftz = (averagez - avgo)
zdistances = (avgshiftz[:12]-avgshiftz[1:13])
ptavg = np.average(avgshiftz[:5]-avgshiftz[1:6])
coavg = np.average(avgshiftz[7:12]-avgshiftz[8:13])
diff = np.full((struc.atoms,3),0,'float64')



for i in range(0,52,4):
    for j in range(4):
        for z in range(3):
            if z == 2:
                diff[i+j,z]=pc[i+j,z]-averagez[int(i/4)]
            else:
                diff[i+j,z]=pc[i+j,z]-original[i+j,z]

averagez
np.average(averagez[1:6]-averagez[:5])
np.average(averagez[8:]-averagez[7:12])
averagez[6]-averagez[5]
averagez[7]-averagez[6]

avgo
avgshiftz
diff[:,2]
diff[16:36,2]

def itld(x,y,z,w):
    if w == 1:
        return x[y::4,z][6]-x[y::4,z][5]
    elif w == 2:
        return x[y::4,z][7]-x[y::4,z][6]


averagez
avgo

avgshiftz



















fig=plt.figure(figsize=(13,13))
frplot = fig.add_subplot(1,1,1)
frplot.bar(np.linspace(0,12,12),diff[6*4:9*4,2],width=0.6,color=['forestgreen']*4+['red']*4+['navy']*4)
frplot.set_facecolor('lightgray')
frplot.set_xticks(np.linspace(0,13,13))
frplot.set_xticklabels(labelmix)
frplot.set_title('Position#'+str(plot))
frplot.grid(which='both',axis='both',color='gray', linestyle='-', linewidth=1)
plt.show()

fig=plt.figure(figsize=(10,10))
frplot = fig.add_subplot(1,1,1)
frplot.set_xticks(xc)
frplot.set_ylabel("Avg. layer Shifts [$a_{lat}^{-1}$]")
frplot.set_xticklabels(labelmix)
frplot.bar(xc,avgshiftz,width=0.6,color=['forestgreen']*6+['red']*1+['navy']*6)
frplot.bar(np.linspace(0.5,12.5,12),zdistances,width=0.3,color=['mediumspringgreen']*5+['gold']+['darkviolet']+['cyan']*6,alpha=0.9)
frplot.plot(np.linspace(0.0,6,100),np.full((100),ptavg,'float64'),'red')
frplot.plot(np.linspace(08.0,13,100),np.full((100),coavg,'float64'),'red')
frplot.set_facecolor('lightgray')
frplot.set_title('Average layer shift and distance Pt(26)/Pt(26)_lines_100',fontdict ={'fontsize': 18})
frplot.grid(which='both',axis='both',color='gray', linestyle='-', linewidth=1)
boxstr = '\n'.join((
    'Average Pt layer dis. change='r'$%.6f$' % (ptavg, ),
    ))
props = dict(boxstyle='round', facecolor='white', alpha=1.0)
frplot.text(0.175, 0.25, boxstr, transform=frplot.transAxes, fontsize=16,
        verticalalignment='top', bbox=props)
boxstr = '\n'.join((
    'Average Co layer dis. change='r'$ %.3f$' % (coavg, ),
    ))
props = dict(boxstyle='round', facecolor='lightgray', alpha=1.0)
frplot.text(0.45, 0.70, boxstr, transform=frplot.transAxes, fontsize=16,
        verticalalignment='top', bbox=props)
plt.show()
#itld(pc,0,2,2)
#origitld  = orig.iltd()
#origitldx1 = 0.0
#origitldx2 = 0.5
#origitldx1 = -0.5773502686122760
#origitldx2 = 0.2886751351721640

#r'$d_0=%.6f$' % (origitld, ),
#r'$d_{0_pt-mix}=%.6f$' % (origitldx1, ),
#r'$d_{0_mix-co}=%.6f$' % (origitldx2, ),



#plt.savefig('P26C26_111_avg_z_110.png')
#plt.savefig('P26C26_111_avg_ribbons_z.png')
#plt.savefig('P26C26_111_checkered_X.png')
