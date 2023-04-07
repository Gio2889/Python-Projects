import numpy as np
import pandas as pd
import itertools as iter
coord=np.array([[0,0],[0.5,0.5773502691896260],[1.0,0.2886751345948130]])
tvec = np.array([[0.0,0.0],[1.0,0.0],[-0.5,0.8660254037844390]])

def scbuild(crd,tvectors):
    layer=[]
    for pos in crd:
        layer.append(pos)
        for vector in list(iter.combinations(tvectors,2)):
            y = sum(vector)
            layer.append(pos + y)
    return np.array(layer)

df=pd.DataFrame(scbuild(coord,tvec))

filepath ='2x2main.xlsx'
df.to_excel(filepath, index=False)
