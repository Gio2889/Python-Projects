import numpy as np

earr=np.linspace(-0.147,0.147,501)
earr[-30:]
:qj=earr[::50]
m=earr[1::50]
j.shape
m.shape
j
m
earr[:51]

a=earr[:50]
b=earr[50:100]
c=earr[100:150]
d=earr[150:200]
e=earr[200:250]
f=earr[250:301]
g=earr[301:351]
h=earr[351:401]
i=earr[401:451]
j=earr[451:501]
-0.147 -0.11818799999999999
-0.1176 -0.08878799999999999
-0.0882 -0.059387999999999996
-0.05879999999999999 -0.029988
-0.029399999999999996 -0.0005880000000000052
0.0 0.02940000000000001
0.029988000000000015 0.05879999999999999
0.059387999999999996 0.0882
0.088788 0.11760000000000001
0.11818799999999999 0.147
fulllist=np.array([a,b,c,d,e,f,g,h,i,j])
for item in fulllist:
    print(item[0],item[-1])


vi ctr  delta=earr[:500]-earr[1:501]
delta
earr[180:200]


block1=earr[:182]
block2=earr[182+137:]
block1.shape
block2.shape
middle=earr[182:(182+137)]
middle.shape
block1[0]
block1[-1]
middle[0]
middle[-1]
block2[0]
block2[-1]
182*delta[0]-0.147
blocktest1=np.linspace(-0.147,-0.040572,182)
blocktest1[:20]
block1[:20]
