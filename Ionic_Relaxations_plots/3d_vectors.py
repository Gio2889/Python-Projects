import numpy as np
import pandas as pd
import matplotlib.pyplot  as plt
from mpl_toolkits.mplot3d import Axes3D
from poscar_reader import POSCAR
from Arrow3dclass import Arrow3D


orig2 = POSCAR('poscar.2x2')
p25c27 = POSCAR('contcar.pt25c27.txt')
p27c25 = POSCAR('CONTCAR.pt27co25')
#forp26c26 co is ribbons pt is chekered
p26cc26 =POSCAR('CONTCAR.co.pt26co26')
p26pc26 = POSCAR('CONTCAR.pt.p26co26')
labels = ['Pt','Pt','Pt','Pt','Pt','Pt','Mixed','Co','Co','Co','Co','Co','Co']
xc=np.linspace(0.0,13,13)

struc=p26pc26;

#For checkered patern only
t1=orig2.atomiccoord[6*4:6*4+4][1].copy()
t2=orig2.atomiccoord[6*4:6*4+4][3].copy()
orig2.atomiccoord[6*4:6*4+4][1]=t2
orig2.atomiccoord[6*4:6*4+4][3]=t1


original = orig2.cartesian()
pc = struc.cartesian(True)

pc
fig = plt.figure(figsize=(15,15))
ax = fig.add_subplot(111, projection='3d')


ax.plot(orig2.atomiccoord[:6*4+2,0],orig2.atomiccoord[:6*4+2,1],orig2.atomiccoord[:6*4+2,2], 'o', markersize=10, color='g', alpha=0.2)
ax.plot(orig2.atomiccoord[6*4+2:,0],orig2.atomiccoord[6*4+2:,1],orig2.atomiccoord[6*4+2:,2], 'o', markersize=10, color='b', alpha=0.2)
ax.plot(struc.atomiccoord[:6*4+2,0],struc.atomiccoord[:6*4+2,1],struc.atomiccoord[:6*4+2,2], 'o', markersize=10, color='g', alpha=1)
ax.plot(struc.atomiccoord[6*4+2:,0],struc.atomiccoord[6*4+2:,1],struc.atomiccoord[6*4+2:,2], 'o', markersize=10, color='b', alpha=1)
for i in range(52):
    a = Arrow3D([orig2.atomiccoord[i][0],struc.atomiccoord[i][0]],[orig2.atomiccoord[i][1],struc.atomiccoord[i][1]],[orig2.atomiccoord[i][2],struc.atomiccoord[i][2]], mutation_scale=20,lw=3, arrowstyle="-", color="r")
    ax.add_artist(a)
ax.set_zticks(original[:13*4:4,2])
ax.set_zticklabels(labels)
ax.set_xlabel(r'$\hat{x}$')
ax.set_ylabel(r'$\hat{y}$')
plt.title('Pt(6)/M(1)/Co(6) 111 2x2')
forceAspect(ax,aspect=1)
plt.draw()
plt.show()
#ax.plot([1,0,0],[0,1,0],[0,0,1],[1,1,1], 'o', markersize=10, color='g', alpha=0.2)
#ax.plot([0],[0],[0], 'o', markersize=10, color='red', alpha=0.5)
#a = Arrow3D([1, 1],[0, 1],[1, 1], mutation_scale=20,lw=3, arrowstyle="-|>", color="r")
#ax.add_artist(a)
