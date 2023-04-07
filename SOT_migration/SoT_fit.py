# @Author: Giovanni G. Baez Flores
# @Date:   2020-06-08T10:54:01-05:00
# @Email:  gbaez89@gmail.com
# @Last modified by:   Giovanni G. Baez Flores
# @Last modified time: 2020-07-10T23:22:16-05:00
import os
import sys
from itertools import accumulate,chain
from math import sqrt,sin,cos
import scipy as sp
from scipy import special
from scipy.misc import derivative
import numpy as np
import pandas as pd

"""The following is a list of subroutines for the fit of SOT calculationsto vector spherical harmonics"""
##################### the angles are contained here as to not export them
# every single calculation.
angles=pd.DataFrame([[1.107149, 0.0],[1.107149, 1.256637],[1.107149, 2.513274],[1.107149, -2.513274],[1.107149, -1.256637],[0.0, 0.0],[2.0344439999999997, 3.141593],[2.0344439999999997, -1.884956],[2.0344439999999997, -0.628319],[2.0344439999999997, 0.628319],[2.0344439999999997, 1.884956],[3.141593, 0.0],[0.652358, 0.628319],[0.652358, 1.884956],[0.652358, 3.141593],[0.652358, -1.884956],[0.652358, -0.628319],[2.489235, -2.513274],[2.489235, -1.256637],[2.489235, 0.0],[2.489235, 1.256637],[2.489235, 2.513274],[1.3820860000000001, 0.628319],[1.3820860000000001, 1.884956],[1.3820860000000001, 3.141593],[1.3820860000000001, -1.884956],[1.3820860000000001, -0.628319],[1.759507, -2.513274],[1.759507, -1.256637],[1.759507, 0.0],[1.759507, 1.256637],[1.759507, 2.513274],[0.553574, 0.0],[0.553574, 1.256637],[0.553574, 2.513274],[0.553574, -2.513274],[0.553574, -1.256637],[2.588018, 3.141593],[2.588018, -1.884956],[2.588018, -0.628319],[2.588018, 0.628319],[2.588018, 1.884956],[1.5707959999999999, 0.314159],[1.5707959999999999, 1.5707959999999999],[1.5707959999999999, 2.827433],[1.5707959999999999, -2.199115],[1.5707959999999999, -0.942478],[1.5707959999999999, -2.827433],[1.5707959999999999, -1.5707959999999999],[1.5707959999999999, -0.314159],[1.5707959999999999, 0.942478],[1.5707959999999999, 2.199115],[1.0172219999999998, 0.628319],[1.0172219999999998, 1.884956],[1.0172219999999998, 3.141593],[1.0172219999999998, -1.884956],[1.0172219999999998, -0.628319],[2.124371, -2.513274],[2.124371, -1.256637],[2.124371, 0.0],[2.124371, 1.256637],[2.124371, 2.513274],[0.350405, 0.0],[0.350405, 1.256637],[0.350405, 2.513274],[0.350405, -2.513274],[0.350405, -1.256637],[0.756743, 0.0],[1.029884, -0.39071300000000003],[1.398303, -0.206273],[1.398303, 0.206273],[1.029884, 0.39071300000000003],[0.756743, 1.256637],[1.029884, 0.865925],[1.398303, 1.0503639999999999],[1.398303, 1.46291],[1.029884, 1.64735],[0.756743, 2.513274],[1.029884, 2.122562],[1.398303, 2.3070009999999996],[1.398303, 2.719547],[1.029884, 2.903987],[0.756743, -2.513274],[1.029884, -2.903987],[1.398303, -2.719547],[1.398303, -2.3070009999999996],[1.029884, -2.122562],[0.756743, -1.256637],[1.029884, -1.64735],[1.398303, -1.46291],[1.398303, -1.0503639999999999],[1.029884, -0.865925],[2.111708, 2.275668],[1.7432900000000002, 2.0912290000000002],[1.7432900000000002, 1.678682],[2.111708, 1.494243],[2.384849, 1.884956],[2.111708, 1.019031],[1.7432900000000002, 0.834592],[1.7432900000000002, 0.422045],[2.111708, 0.23760599999999998],[2.384849, 0.628319],[2.111708, -0.23760599999999998],[1.7432900000000002, -0.422045],[1.7432900000000002, -0.834592],[2.111708, -1.019031],[2.384849, -0.628319],[2.111708, -1.494243],[1.7432900000000002, -1.678682],[1.7432900000000002, -2.0912290000000002],[2.111708, -2.275668],[2.384849, -1.884956],[2.111708, -2.75088],[1.7432900000000002, -2.935319],[1.7432900000000002, 2.935319],[2.111708, 2.75088],[2.384849, -3.141593],[2.791187, 1.884956],[2.791187, 0.628319],[2.791187, -0.628319],[2.791187, -1.884956],[2.791187, -3.141593],[1.5707959999999999, 0.0],[1.5707959999999999, 3.141593]],columns=['th','phi'])
angsz=angles.size
###############################################################################

def inv(n):
    th=angles.iloc[n,0]
    ph=angles.iloc[n,1]
    for i in range(0,angsz):
        thi=angles.iloc[i,0]
        phi=angles.iloc[i,1]
        if cos(th+thi)>-0.99999:
            continue
        elif abs(cos(th))<-0.99999 and cos(ph-phi)>-0.99999:
            continue
        return i
##torq has to be a panda dataframe##
#drop first counter and just use the DF number#
def sysasym(torq):
    df1=pd.DataFrame()
    df2=pd.DataFrame()
    for i in torque.size[0]:
        tx=(torq.iloc[i,1]+torq.iloc[inv(i),1])/2
        ty=(torq.iloc[i,2]+torq.iloc[inv(i),2])/2
        tz=(torq.iloc[i,3]+torq.iloc[inv(i),3])/2
        txa=(torq.iloc[i,1]-torq.iloc[inv(i),1])/2
        tya=(torq.iloc[i,2]-torq.iloc[inv(i),2])/2
        tza=(torq.iloc[i,3]-torq.iloc[inv(i),3])/2
        df1.append([tx,ty,tz])
        df2.append([txa,tya,tza])
    return (df1,df2)
##### define vector spherical harmonics #
def psilm(l,m,th,ph):
    if th==0:
        th=th + 1e-4
    if th==np.pi:
        th=th - 1e-4
    if ph==0:
        ph=ph + 1e-4
    if ph==np.pi:
        ph=ph - 1e-4
    def thsph(th2):
        y=sp.special.sph_harm(m, l, ph,th2)
        return y
    vec=np.array([0,derivative(thsph,th,dx=1e-7),complex(0,(1/np.sin(th))*m*sp.special.sph_harm(m, l, ph,th))])
    vec=vec/np.sqrt(l*(l+1))
    return vec
def philm(l,m,th,ph):
    if th==0:
        th=th + 1e-4
    if th==np.pi:
        th=th - 1e-4
    if ph==0:
        ph=ph + 1e-4
    if ph==np.pi:
        ph=ph - 1e-4
    def thsph(th2):
        y=sp.special.sph_harm(m, l, ph,th2)
        return y
    vec=np.array([0,-1*complex(0,(1/np.sin(th))*m*sp.special.sph_harm(m, l, ph,th)),derivative(thsph,th,dx=1e-7)])
    vec=vec/np.sqrt(l*(l+1))
    return vec

### function to clear small numbers ###
def chop(z):
    if (abs(z.real)<1e-3 and abs(z.imag)<1e-3):
        s=complex(0,0)
    elif abs(z.real) < 1e-3:
        s=complex(0,z.imag)
    elif abs(z.imag) < 1e-3:
        s=complex(z.real,0)
    return s

### Clear VSH of small numbers ###
def psilmr(l,m,th,ph):
    if m==0:
        vec=np.fromiter(map(chop, psilm(l,m,th,ph)),dtype=np.cdouble)
        return vec.real
    if m<0:
        vec= np.fromiter(map(chop,complex(0,1/np.sqrt(2))*(psilm(l,m,th,ph)-((-1)**m)*psilm(l,-m,th,ph))),dtype=np.cdouble)
        return vec.real
    if m>0:
        vec= np.fromiter(map(chop,complex(1/np.sqrt(2),0)*(psilm(l,-m,th,ph)+((-1)**m)*psilm(l,m,th,ph))),dtype=np.cdouble)
        return vec.real
def philmr(l,m,th,ph):
    if m==0:
        vec=np.fromiter(map(chop, philm(l,m,th,ph)),dtype=np.cdouble)
        return vec.real
    if m<0:
        vec=np.fromiter(map(chop,complex(0,1/np.sqrt(2))*(philm(l,m,th,ph)-((-1)**m)*philm(l,-m,th,ph))),dtype=np.cdouble)
        return vec.real
    if m>0:
        vec=np.fromiter(map(chop,complex(1/np.sqrt(2),0)*(philm(l,-m,th,ph)+((-1)**m)*philm(l,m,th,ph))),dtype=np.cdouble)
        return vec.real
################################################################################
#########  transformations to and from cartesian to spherical coordinates ######
def cartosp(th,ph):
    df=pd.DataFrame()
    x=[np.sin(th)*np.cos(ph),np.sin(th)*np.sin(ph),np.cos(th)]
    y=[np.cos(th)*np.cos(ph),np.cos(th)*np.sin(ph),-np.sin(th)]
    z=[-np.sin(ph),np.cos(ph),0]
    return np.array([x,y,z])
def sptocart(th,ph):
    x=[np.sin(th)*np.cos(ph),np.cos(th)*np.cos(ph),-np.sin(th)]
    y=[np.sin(th)*np.sin(ph),np.cos(th)*np.sin(ph),np.cos(th)]
    z=[np.cos(ph),np.sin(ph),0]
    return (x,y,z)
###############################################################################
### Projection to VSH type=1(Psi_lm) type=2(Phi_lm)############################
###Data set must become a DataFrame
###############################################################################
def VSHproj(ds,type,l,m):
    w1=(5/(7*6))*np.pi
    w2=(9/(7*10))*np.pi
    vfield=ds[['tx','ty','tz']].copy()
    wangles=ds[['i','th','phi']].copy()
    wangles.loc[:,'weight']=0
    wangles.loc[:,'weight'] = np.where(wangles['i']<=12, w1, w2)
    transfo=wangles[['th','phi']].apply(lambda x:cartosp(x.th,x.phi),axis=1)
    vectorfield=[]
    for i in range(0,32):
        x=list(transfo[i].dot(vfield[['tx','ty','tz']].iloc[i]))
        vectorfield.append(x)
    vf=pd.DataFrame(vectorfield,columns=['tx','ty','tz'])
    if type==1:
        res=0
        for i in range(32):
            res=res+wangles.iloc[i,3]*vf.iloc[i].dot(psilmr(l,m,wangles.iloc[i,1],wangles.iloc[i,2]))
        return res
    elif type==2:
        res=0
        for i in range(32):
            res=res+wangles.iloc[i,3]*vf.iloc[i].dot(philmr(l,m,wangles.iloc[i,1],wangles.iloc[i,2]))
        return res
    else:
        print("Wrong input for VSHproj")
        exit()
###############################################################################
# Convert torques and rotate torques based on the crystalographic orientation #
def convtrq(set):
    ore=111
    newset=set.copy()
    newset.th=np.pi-set.th
    #### This bypasses a numerical from approaching 0 from the wrong side###
    if ore==111:
        newset.phi=-(np.pi+set.phi) + np.pi/6
    else:
        newset.phi=-(np.pi+set.phi)
    newset.ty=-set.ty
    newset.tz=-set.tz
    return newset
##### This is for 111 orientation #############################################
def trqrot(set):
    newset=set.copy()
    newset.tx=set.tx*cos(np.pi/6)+set.ty*sin(np.pi/6)
    newset.ty=set.ty*cos(np.pi/6)-set.tx*sin(np.pi/6)
    return newset

########## Fit torque function##############################

def fitTrq(set,set2,m,*args):
    ore=111
    if len(args)!=0:
        parset=args[0]
    else:
        parset=25
    if set.shape!=set2.shape:
        print('Warning, datasets of different sizes')
        exit
    if ore==111:
        tr=trqrot(set)
        tl=trqrot(set2)
    else:
        tr=set
        tl=set2
    setlist=[]
    for j in [tl,tr]:
        meanls=[]
        for i in range(32):
            ser=list(j[['tx','ty','tz']].iloc[i::32].mean())
            meanls.append(ser)
        fnl=pd.DataFrame(meanls)
        setlist.append(fnl)
    meantrqs=m*(setlist[0]-setlist[1])/2
    meantrqs.columns=['tx','ty','tz']
    trueangles=angles[['th','phi']].iloc[:32].reset_index()
    fsurfsets=pd.concat([trueangles,meantrqs],axis=1)
    fsurfsets['i']=fsurfsets.index +1
    fsurfsets=convtrq(fsurfsets)
    ########## make angles that are not exactly zero equal zero to avoid errors
    fsurfsets.loc[abs(fsurfsets['th'])<1e-6, 'th']=0
    fsurfsets.loc[abs(fsurfsets['phi'])<1e-6, 'phi']=0
    VSHsym =[VSHproj(fsurfsets,1,1,-1),VSHproj(fsurfsets,2,2,1), VSHproj(fsurfsets,1,3,-1),VSHproj(fsurfsets,2,4,1)]
    VSHas =[VSHproj(fsurfsets,2,1,-1),VSHproj(fsurfsets,1,2,1), VSHproj(fsurfsets,2,3,-1),VSHproj(fsurfsets,1,4,1)]
    return VSHsym,VSHas

############## Data frame creator from mathematic output MODE= 1 ###############
def df_create(set):
    data=pd.read_csv(set,skiprows=1,header=None,names=['i','tx','ty','tz'],delimiter=",")
    data=data.drop([0]).dropna().reset_index()
    data['i']=data['i'].map(lambda x: x.lstrip('{')).astype('int64')
    data['tz']=data['tz'].map(lambda x: x.rstrip('};')).astype('float64')
    return data
##############################################################################
##############################################################################
##############################################################################
##############################################################################
def harm_fit(ds1,ds2,pls,zl,mag):
    dsl=pd.read_csv(ds1)
    dsl=dsl.drop('Unnamed: 0',axis=1)
    dsr=pd.read_csv(ds2)
    dsr=dsr.drop('Unnamed: 0',axis=1)
    for a in range(1,33):
        for p in range(pls[0],pls[-1]+1):
            cpl=dsl.loc[((dsl['PL']==p) & (dsl['angle']==a))][zl[0]-1:zl[-1]][['tx','ty','tz']].sum().to_frame().transpose()
            cpl['PL']=p
            cpl2=dsr.loc[((dsr['PL']==p) & (dsr['angle']==a))][zl[0]-1:zl[-1]][['tx','ty','tz']].sum().to_frame().transpose()
            cpl2['PL']=p
            if p==pls[0]:
                dfl=cpl
                dfr=cpl2
            else:
                dfl=dfl.append(cpl)
                dfr=dfr.append(cpl2)
        dfl['angle']=a
        dfr['angle']=a
        if a==1:
            dffl=dfl
            dffr=dfr
        else:
            dffl=dffl.append(dfl)
            dffr=dffr.append(dfr)
    orig_stdout = sys.stdout
    f = open('Harm.out', 'w')
    sys.stdout = f
    for p in range(pls[0],pls[-1]+1):
        lsftl=dffl.loc[dffl['PL']==p]
        lsftl=lsftl.rename(columns={'angle':'i'})
        lsftl=lsftl[['i','tx','ty','tz']]
        lsftr=dffr.loc[dffr['PL']==p]
        lsftr=lsftr.rename(columns={'angle':'i'})
        lsftr=lsftr[['i','tx','ty','tz']]
        res=list(fitTrq(lsftl,lsftr,mag))
        res=list(chain.from_iterable(res))
        res.insert(0,p)
        for x in res:
            if x==res[-1]:
                print(x)
            else:
                print(x, end=" ")
    f.close()
    sys.stdout = orig_stdout
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################
##############################################################################



# MODE: 1 (Takes full SOT file and calculates SOT coefficient [Similar to mathematica script])####
## MODE: 2 Uses csv file from Master Maker to calculate layer resolved Harmonics
##############################################################################

#arguments=sys.argv
#mode=int(arguments[1])
#inputs=arguments[2:]
#### Testing parameters #######################################################
#inputs=['x2_trq_com1pt_l_x1.0_384.dat','x2_trq_com1pt_r_x1.0_384.dat',1]
#inputs=['trq_CoMPt_x2_l_x1.0sres1_25.dat','trq_CoMPt_x2_r_x1.0sres1_25.dat',1]
inputs=['CoMPt_master_v3_L.csv','CoMPt_master_v3_R.csv',1,70,1,6,1.0]
len(inputs)
mode=2
###############################################################################
if mode==1:
    print('Calculating coefficients for SOT')
    if (len(inputs))%3!=0:
        print('even number of files\n Files must be in (L R mag) triplets')
        exit
    inputls=[]
    for i in range(0,len(inputs),3):
        ds1=inputs[0+i:i+3][0]
        ds2=inputs[0+i:i+3][1]
        m=float(inputs[0+i:i+3][2])
        datal=df_create(ds1)
        datar=df_create(ds2)
        ##################### Setting coefficient for data set ########################
        #mult = input('Magnetization of the system? (default 11.2ub)')
        if m==1.0:
            print('Using default mag 11.2, multiplier is 2.58e5')
            m=0.258*100000*0.012043
        else:
            m=0.258*100000*(11.2/m)*0.012043
        ###############################################################################
    print(fitTrq(datal,datar,m))
elif mode==2:

    filel=inputs[0]
    filer=inputs[1]
    pls=[int(inputs[2]),int(inputs[3])]
    zl=[int(inputs[4]),int(inputs[5])]
    m=float(inputs[6])
    ##################### Setting coefficient for data set ########################
    #mult = input('Magnetization of the system? (default 11.2ub)')
    if m==1.0:
        print('Using default mag 11.2, multiplier is 2.58e5')
        m=1
    else:
        m=1
        #m=0.258*100000*(11.2/m)*0.012043
    ###############################################################################
    harm_fit(filel,filer,pls,zl,m)
    print('Harmonics out to file Harm.out')
else:
    print('No mode selected, aborting')
    exit()
