import pandas as pd
import numpy as np

class vector():
    def __init__(self,*arg):
        self.len = len(arg)
        self.values = arg

    def __getitem__(self, key):
        """Sets ability to call lists parts"""
        return self.values[key]

    def __iter__(self):
        """Sets ability to iterate over items"""
        return self.values.__iter__()
        
    def __abs__(self):
        return np.sqrt( sum( val**2 for val in self) )

a = vector(1,2,3,4)
a.len
a[0]
abs(a)
