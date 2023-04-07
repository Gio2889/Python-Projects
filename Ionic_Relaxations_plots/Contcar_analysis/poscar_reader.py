# @Author: Giovanni G. Baez Flores <gbaez>
# @Date:   2018-12-10T11:11:47-06:00
# @Email:  gbaez89@gmail.com
# @Last modified by:   Giovanni G. Baez Flores
# @Last modified time: 2019-01-03T17:35:10-06:00



import pandas as pd
import numpy as np

class POSCAR():
    def __init__(self,file):
        """"Reads VASP POSCAR/CONTCAR files"""
        """COntains methods to extract alat,a(1-3) and atomic coordinates"""
        df = pd.read_fwf(file)
        self.alat = float(df.iloc[0,0])
        rawlat = list(df.iloc[1:4,0])
        lattice = []
        for item in rawlat:
            x = list(map(float,item.split()))
            lattice.append(x)
        self.a1 = np.array(lattice[0])
        self.a2 = np.array(lattice[1])
        self.a3 = np.array(lattice[2])
        self.atoms = sum(list(map(int,df.iloc[5,0].split())))
        atmc = list(df.iloc[8:8+self.atoms,0])
        atomicc = []
        for item in atmc:
            y = list(map(float,item.split()[:3]))
            atomicc.append(y)
        self.atomiccoord = np.array(atomicc)

    def nalat(self):
        return self.alat*self.a1[0]

    def iltd(self):
        mid = int(self.atoms/2)
        d = self.a3[2]*(self.atomiccoord[mid,2]-self.atomiccoord[mid-1,2])
        return d

    def inter(self,*args):
        if len(args) == 0 or args[0] == "z":
            res = []
            for  i in range(self.atoms-1):
                d = self.a3[2]*(self.atomiccoord[i+1,2]-self.atomiccoord[i,2])
                res.append(d)
            res.append(0.0)
            return np.array(res)
        elif args[0] == "x":
            res = []
            for  i in range(self.atoms-1):
                d1 = self.a1[0]*(self.atomiccoord[i+1,0]-self.atomiccoord[i,0])
                d2 = self.a2[0]*(self.atomiccoord[i+1,0]-self.atomiccoord[i,0])
                res.append(d1+d2)
            res.append(0.0)
            return np.array(res)
        elif args[0] == "y":
            res = []
            for  i in range(self.atoms-1):
                d1 = self.a1[1]*(self.atomiccoord[i+1,1]-self.atomiccoord[i,1])
                d2 = self.a2[1]*(self.atomiccoord[i+1,1]-self.atomiccoord[i,1])
                res.append(d1+d2)
            res.append(0.0)
            return np.array(res)
        elif len(args) > 1:
            return "Arguments must be x,y,z or none "
        else:
            return "Arguments must be x,y,z or none "

    def cartesian(self,*args):
        if len(args) == 0:
            check = False
        else:
            check = args[0]
        x=self.atomiccoord[:,0]
        y=self.atomiccoord[:,1]
        z=self.atomiccoord[:,2]
        if check == True:
            for i in range(self.atoms):
                if 0.9 < z[i] < 1.1:
                    z[i] = z[i] - 1

            for i in range(self.atoms):
                if 0.9 < x[i] < 1.1:
                    x[i] = x[i] - 1

            for i in range(self.atoms):
                if 0.9 < y[i] < 1.1:
                    y[i] = y[i] - 1
        xp=x*self.a1[0]+y*self.a2[0]+z*self.a3[0]
        yp=x*self.a1[1]+y*self.a2[1]+z*self.a3[1]
        zp=x*self.a1[2]+y*self.a2[2]+z*self.a3[2]
        res = np.full((self.atoms,3),0,'float64')
        res[:,0], res[:,1], res[:,2] = xp , yp, zp
        return res

    def avg(self,*args):
        avgarr = np.full((int(self.atoms/4)),0,'float64')
        for j in range(0,self.atoms,4):
            avgarr[int(j/4)] =  np.average(original[j:j+4,2])
        return agvarr
