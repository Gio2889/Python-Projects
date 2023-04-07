import numpy as np
import pandas as pd
from math import sqrt,sin,cos
import matplotlib.pyplot  as plt
from mpl_toolkits.mplot3d import Axes3D

class Planet:
    def __init__(self,Rad,pw,t,stp):
        self.prad = Rad
        self.pom = pw
        self.time = t
        self.steps = stp
        self.tarr = np.linspace(0,self.time,self.steps,endpoint=True)

    def getX(self):
        return self.prad*np.cos(self.pom*self.tarr)

    def getY(self):
        return self.prad*np.sin(self.pom*self.tarr)


    def scenario(self,time,steps,plott,xt,yt,size,x,y):
        fig=plt.figure(figsize=(size,size))
        orbit = fig.add_subplot(1,1,1)
        orbit.grid( which='both',axis='both',color='gray', linestyle='-', linewidth=1)
        orbit.set_aspect('equal')
        orbit.set_xlabel(xt)
        orbit.set_ylabel(yt)
        orbit.set_title(plott)
        orbit.plot(x,y,'b-o')
        plt.show()

class Moon(Planet):
    def __init__(self, Rad, pw, rad, mw,time,steps):
        Planet.__init__(self,Rad,pw,time,steps)
        self.mrad = rad
        self.mom = mw
    def getx(self):
        return self.getX() + self.mrad*np.cos(self.mom*self.tarr)

    def gety(self):
        return self.getY() + self.mrad*np.sin(self.mom*self.tarr)


planet= Planet(4.0,2.0,3.3,100)
planet.scenario(3.2,100,'Planet orbit','time','au',8,planet.getX(),planet.getY())
moon = Moon(4.0,2.0,1.0,14.0,3.2,100)
moon.scenario(3.2,100,'Satelite orbit','time','au',8,moon.getx(),moon.gety())
