import numpy as np
import pandas as pd
import matplotlib.pyplot  as plt
from mpl_toolkits.mplot3d import Axes3D
import sys
sys.path.insert(0, 'Contcar_analysis')
from poscar_reader import POSCAR
import xlsxwriter

origbig= POSCAR('Contcar_analysis/poscar.p9c12')
orig66=POSCAR('Contcar_analysis/poscar.orig')
orig2 = POSCAR('Contcar_analysis/poscar.2x2')
p9c12 = POSCAR('Contcar_analysis/CONTCAR.pt9co12')
p25c27 = POSCAR('Contcar_analysis/contcar.pt25c27.txt')
p27c25 = POSCAR('Contcar_analysis/CONTCAR.pt27co25')
p26cc26 = POSCAR('Contcar_analysis/CONTCAR.co.pt26co26')
p26pc26 = POSCAR('Contcar_analysis/CONTCAR.pt.p26co26')
c6p6=POSCAR('Contcar_analysis/CONTCAR.pt6co6')

2.63665000000000*1.0139125298305809/0.529
original = orig66.cartesian(False)
original
relaxed = c6p6.cartesian(False)
relaxed
orig66.inter("z")/(np.sqrt(2/3))
c6p6.inter("z")/(np.sqrt(2/3))
c6p6.inter("z")[::-1][1::]/(np.sqrt(2/3))
c6p6.inter("z")[:4]/(np.sqrt(2/3))
c6p6.inter("z")[0]/(np.sqrt(2/3))
z=0
for i in range(4):
    y=c6p6.inter("z")[:4]/(np.sqrt(2/3))
    x=y[i]
    z=z+x
    print(x,z-c6p6.inter("z")[0]/(np.sqrt(2/3)))

original

avgo=np.full((int(struc.atoms/4)),0,'float64')
for j in range(0,struc.atoms,4):
    avgo[int(j/4)] = np.average(original[j:j+4,2])
for j in range(0,struc.atoms,4):
    avgo[int(j/4)] = np.average(original[j:j+4,2])

struclist = [p25c27,p26cc26,p27c25]
diff = np.full((3,struc.atoms,3),0,'float64')
for l in range(len(struclist)):
    struc=struclist[l]
    pc = struc.cartesian(True)
    averagez = np.full((int(struc.atoms/4)),0,'float64')

    for j in range(0,struc.atoms,4):
        averagez[int(j/4)] =  np.average(pc[j:j+4,2])

    for i in range(0,struc.atoms,4):
        for j in range(4):
            for z in range(3):
                if z == 2:
                    diff[l,i+j,z]=pc[i+j,z]-averagez[int(i/4)]
                else:
                    diff[l,i+j,z]=pc[i+j,z]-original[i+j,z]


def getlayer(l,df):
    res = np.full((1+2*l,4),0,'float64')
    mark = (6*4-l*4)/4
    for i in range(6*4-l*4,7*4+l*4,4):
        for j in range(4):
            res [int(i/4 - mark),j] = df[i+j]
    return res





c25zs=np.array([[-0.0009096 , -0.0009096 ,  0.0027288 , -0.0009096] ,[ -0.00394507,0.01183521, -0.00394507, -0.00394507], [ 0.01881844, -0.00627281,-0.00627281, -0.00627281], [ 0.00463697,  0.00463697, -0.0139109 ,0.00463697],[ -0.0054279 ,  0.0162837 , -0.0054279 , -0.0054279 ]])
c50zs=np.array([[-0.00148283, -0.00148283,  0.00148284,  0.00148283], [ 0.00813988,0.00813986, -0.00813987, -0.00813987],  [0.0116564 ,  0.01165637,-0.01165638, -0.01165638], [ 0.00929011,  0.00929011, -0.00929007,-0.00929014],  [0.0091072 ,  0.00910707, -0.00910713, -0.00910713]])
c75zs=np.array([[0.00116212, -0.00348648,  0.00116223,  0.00116212],  [0.00306116,0.00306175, -0.00918407,  0.00306116],  [0.00438492,  0.00438951,0.0043898 , -0.01316423], [-0.0048543 ,  0.01456456, -0.00485596,-0.0048543] ,  [0.00305991,  0.00305629, -0.00917611,  0.00305991]])

lnum=5
datshift=np.concatenate((getlayer(lnum,diff[0,:,2]),getlayer(lnum,diff[1,:,2]),getlayer(lnum,diff[2,:,2])))
datshift.shape
datshift=np.concatenate((np.array([['25%']*(2*lnum+1)+['50%']*(2*lnum+1)+['75%']*(2*lnum+1)]).T,np.array([(['Pt']*(lnum)+['Mix']+['Co']*(lnum))*3]).T,datshift),axis=1)
df2=pd.DataFrame(datshift,columns=['Pt%','Layer',"#1",'#2','#3','#4'])


indx=[]
col = ['alpha(Pt%)','beta(Co%)','Pt-Pt','Co-Co','Pt-I','I-Co']
data = [[0,0,0.9278372323388087,0.7371016664396011,0.8171479596953031,0.7306429123772595],[0.25,0.75,0.9254332432424821,0.734224412978192,0.8469532026335562,0.7502845401182849],[0.5,0.5,0.9232363233237457,0.7333136440446635,0.8753782580728702,0.7680434816890171],[0.75,0.25,0.9206675733469855,0.7320135254974515,0.9014457205806519,0.7868557847703697]]
df=pd.DataFrame(data,index=None,columns=col)

writer = pd.ExcelWriter('zshifts.xlsx', engine='xlsxwriter')
df.to_excel(writer,'Sheet1')
df2.to_excel(writer,'Sheet2')
writer.save()

df2



fig = plt.figure(figsize=(10,10))
avgplot = fig.add_subplot(1,1,1)
avgplot.plot(df.iloc[:,0],df.iloc[:,2],'g-', marker='o',label = 'Pt ILTD')
avgplot.plot(df.iloc[:,0],df.iloc[:,3],'b-',marker='o', label = 'Co ILTD')
avgplot.plot(df.iloc[:,0],df.iloc[:,4],'r-',marker='o', label = 'Pt-I ILTD')
avgplot.plot(df.iloc[:,0],df.iloc[:,5],'cyan',marker='o', label = 'Ideal')
avgplot.plot(df.iloc[:,0],np.full((4),np.sqrt(2/3)),'black',linestyle='-.', label = 'I-Co ILTD')
avgplot.set_ylabel("Interlayer distance [$a_{lat}^{-1}$]")
avgplot.set_xlabel("Pt concentration in mix layer")
avgplot.set_facecolor('lightgray')
avgplot.grid(which='both',axis='both',color='gray', linestyle='-', linewidth=1)
plt.legend(loc='best')
plt.savefig('average_ITLD.png')
