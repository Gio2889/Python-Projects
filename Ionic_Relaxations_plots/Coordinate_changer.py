# @Author: Giovanni G. Baez Flores
# @Date:   2018-12-19T11:31:11-06:00
# @Email:  gbaez89@gmail.com
# @Last modified by:   Giovanni G. Baez Flores
# @Last modified time: 2018-12-19T15:51:25-06:00



import pandas as pd
import numpy as np

class vector():
    def __init__(self,vec):
        self.x = vec[0]
        self.y = vec[1]
        self.z = vec[2]
        self.len = len(vec)

    def mag(self):
        return np.sqrt(self.x**2 + self.y**2 + self.z**2)

    def sum(self,other):
        return vector(self.x+other.x,self.y+other.y,self.z+other.z)

    def dot(self,other):
        res = (self.x*other.x + self.y*other.y + self.z*other.z)
        return res

latcat=np.array([vector([1.0,0.0,0.0]),vector([-0.5,np.sqrt(3)/2,0.0]),vector([0.0,0.0,10])])

a=vector([1.0,0.0,0.0])
b=vector([-0.5,np.sqrt(3)/2,0.0])

a.sum()


def dot(vec1,vec2):
    res = (vec1.x*vec2.x + vec1.y*vec2.y + vec1.z*vec2.z)
    return res

def sum(vec1,vec2):
    sum = 0
    for i in vec1.len:
        sum = vec1[]

np.cos(120)
np.sin(120)


np.sin(gamma)
def CtoF(lat):
    """Takes an array of vector objects and array of coordinates in cartesian. Transforms the cartesian coordinates to fractionals coord."""
    alpha = np.arccos(dot(lat[0],lat[2])/(lat[0].mag()*lat[2].mag()))
    beta = np.arccos(dot(lat[1],lat[2])/(lat[1].mag()*lat[2].mag()))
    gamma = np.arccos(dot(lat[0],lat[1])/(lat[0].mag()*lat[1].mag()))
    omg = dot(lat[0],lat[2])*lat[1].
    a = lat[0].mag()
    b = lat[1].mag()
    c = lat[2].mag()
    m = np.zeros((3,3))
    m[0,0] = 1/a
    m[0,1] = -( np.cos(gamma)/ (a*np.sin(gamma) ) )
    m[0,2] = b*c*(/)
