# @Author: Giovanni G. Baez Flores
# @Date:   2020-06-08T10:54:01-05:00
# @Email:  gbaez89@gmail.com
# @Last modified by:   Giovanni G. Baez Flores
# @Last modified time: 2020-07-16T14:45:42-05:00
import os
import sys
from itertools import accumulate,chain
from math import sqrt,sin,cos
import scipy as sp
from scipy import special
from scipy.misc import derivative
import numpy as np
import pandas as pd
pd.set_option("display.precision", 16)
np.set_printoptions(16)
#########################################################################################################
######### Set to 111 if using 111 crytalographic orientation ############################################
ore=111
#########################################################################################################
"""The following is a list of subroutines for the fit of SOT calculationsto vector spherical harmonics"""
##################### the angles are contained here as to not export them
# every single calculation.
angles=pd.DataFrame([[1.107149, 0.0],[1.107149, 1.256637],[1.107149, 2.513274],[1.107149, -2.513274],[1.107149, -1.256637],[0.0, 0.0],[2.0344439999999997, 3.141593],[2.0344439999999997, -1.884956],[2.0344439999999997, -0.628319],[2.0344439999999997, 0.628319],[2.0344439999999997, 1.884956],[3.141593, 0.0],[0.652358, 0.628319],[0.652358, 1.884956],[0.652358, 3.141593],[0.652358, -1.884956],[0.652358, -0.628319],[2.489235, -2.513274],[2.489235, -1.256637],[2.489235, 0.0],[2.489235, 1.256637],[2.489235, 2.513274],[1.3820860000000001, 0.628319],[1.3820860000000001, 1.884956],[1.3820860000000001, 3.141593],[1.3820860000000001, -1.884956],[1.3820860000000001, -0.628319],[1.759507, -2.513274],[1.759507, -1.256637],[1.759507, 0.0],[1.759507, 1.256637],[1.759507, 2.513274],[0.553574, 0.0],[0.553574, 1.256637],[0.553574, 2.513274],[0.553574, -2.513274],[0.553574, -1.256637],[2.588018, 3.141593],[2.588018, -1.884956],[2.588018, -0.628319],[2.588018, 0.628319],[2.588018, 1.884956],[1.5707959999999999, 0.314159],[1.5707959999999999, 1.5707959999999999],[1.5707959999999999, 2.827433],[1.5707959999999999, -2.199115],[1.5707959999999999, -0.942478],[1.5707959999999999, -2.827433],[1.5707959999999999, -1.5707959999999999],[1.5707959999999999, -0.314159],[1.5707959999999999, 0.942478],[1.5707959999999999, 2.199115],[1.0172219999999998, 0.628319],[1.0172219999999998, 1.884956],[1.0172219999999998, 3.141593],[1.0172219999999998, -1.884956],[1.0172219999999998, -0.628319],[2.124371, -2.513274],[2.124371, -1.256637],[2.124371, 0.0],[2.124371, 1.256637],[2.124371, 2.513274],[0.350405, 0.0],[0.350405, 1.256637],[0.350405, 2.513274],[0.350405, -2.513274],[0.350405, -1.256637],[0.756743, 0.0],[1.029884, -0.39071300000000003],[1.398303, -0.206273],[1.398303, 0.206273],[1.029884, 0.39071300000000003],[0.756743, 1.256637],[1.029884, 0.865925],[1.398303, 1.0503639999999999],[1.398303, 1.46291],[1.029884, 1.64735],[0.756743, 2.513274],[1.029884, 2.122562],[1.398303, 2.3070009999999996],[1.398303, 2.719547],[1.029884, 2.903987],[0.756743, -2.513274],[1.029884, -2.903987],[1.398303, -2.719547],[1.398303, -2.3070009999999996],[1.029884, -2.122562],[0.756743, -1.256637],[1.029884, -1.64735],[1.398303, -1.46291],[1.398303, -1.0503639999999999],[1.029884, -0.865925],[2.111708, 2.275668],[1.7432900000000002, 2.0912290000000002],[1.7432900000000002, 1.678682],[2.111708, 1.494243],[2.384849, 1.884956],[2.111708, 1.019031],[1.7432900000000002, 0.834592],[1.7432900000000002, 0.422045],[2.111708, 0.23760599999999998],[2.384849, 0.628319],[2.111708, -0.23760599999999998],[1.7432900000000002, -0.422045],[1.7432900000000002, -0.834592],[2.111708, -1.019031],[2.384849, -0.628319],[2.111708, -1.494243],[1.7432900000000002, -1.678682],[1.7432900000000002, -2.0912290000000002],[2.111708, -2.275668],[2.384849, -1.884956],[2.111708, -2.75088],[1.7432900000000002, -2.935319],[1.7432900000000002, 2.935319],[2.111708, 2.75088],[2.384849, -3.141593],[2.791187, 1.884956],[2.791187, 0.628319],[2.791187, -0.628319],[2.791187, -1.884956],[2.791187, -3.141593],[1.5707959999999999, 0.0],[1.5707959999999999, 3.141593]],columns=['th','phi'])
angsz=angles.size
###############################################################################
### Vector Spherical Harmonics
def vsh(type,l,m,th,phi):
    if type==1:
        if l==1 and m==-1:
            return np.array([0,0.5*(np.sqrt(3/(2*np.pi)))*np.cos(th)*np.sin(phi),0.5*(np.sqrt(3/(2*np.pi)))*np.cos(phi)])
        elif l==2 and m==1:
              return np.array([0,0.5*(np.sqrt(5/(2*np.pi)))*np.cos(phi)*np.cos(2*th),-0.5*(np.sqrt(5/(2*np.pi)))*np.cos(th)*np.sin(phi)])
        elif l==3 and m==-1:
              return np.array([0,(1/32)*(np.sqrt(7/(2*np.pi)))*(np.cos(th)+15*np.cos(3*th))*np.sin(phi),(1/16)*(np.sqrt(7/(2*np.pi)))*(3+5*np.cos(2*th))*np.cos(phi)])
        elif l==4 and m==1:
              return np.array([0,(3*(np.cos(2*th)+(7*np.cos(4*th)))*np.cos(phi))/(16*np.sqrt(2*np.pi)),-(3*np.cos(th)*(1+7*np.cos(2*th))*np.sin(phi))/(16*np.sqrt(2*np.pi))])
        elif l==2 and m==-2:
              return np.array([0,(np.sqrt(5/(2*np.pi)))*np.cos(phi)*np.cos(th)*np.sin(phi),0.5*(np.sqrt(5/(2*np.pi)))*np.cos(2*phi)*np.sin(th)])
        elif l==3 and m==2:
              return np.array([0,(1/16)*(np.sqrt(35/(np.pi)))*(1 + 3*np.cos(2*th))*np.cos(2*phi)*np.sin(th),-(1/8)*(np.sqrt(35/(np.pi)))*(np.sin(2*th))*np.sin(2*phi)])
        elif l==4 and m==-2:
              return np.array([0,(3/16)*(1/np.sqrt(np.pi))*(-1 + 7*np.cos(2*th))*np.sin(2*th)*np.sin(2*phi),(3/16)*(1/np.sqrt(np.pi))*(5+ 7*np.cos(2*th))*np.cos(2*phi)*np.sin(phi)])
        elif l==4 and m==-4:
              return np.array([0,(3/8)*(np.sqrt((7/np.pi)))*np.cos(th)*(np.sin(th)**3)*np.sin(4*phi),(3/8)*(np.sqrt((7/np.pi)))*np.cos(4*th)*(np.sin(th)**3)])
    elif type==2:
          if l==1 and m==-1:
              return np.array([0,-0.5*(np.sqrt(3/(2*np.pi)))*np.cos(phi),0.5*(np.sqrt(3/(2*np.pi)))*np.cos(th)*np.sin(phi)])
          elif l==2 and m==1:
                return np.array([0,0.5*(np.sqrt(5/(2*np.pi)))*np.cos(th)*np.sin(phi),0.5*(np.sqrt(5/(2*np.pi)))*np.cos(phi)*np.cos(2*th)])
          elif l==3 and m==-1:
                return np.array([0,-(1/16)*(np.sqrt(7/(2*np.pi)))*(3+5*np.cos(2*th))*np.cos(phi),(1/32)*(np.sqrt(7/(2*np.pi)))*(np.cos(th)+15*np.cos(3*th))*np.sin(phi)])
          elif l==4 and m==1:
                return np.array([0,(3*np.cos(th)*(1+7*np.cos(2*th))*np.sin(phi))/(16*np.sqrt(2*np.pi)),(3*(np.cos(2*th)+(7*np.cos(4*th)))*np.cos(phi))/(16*np.sqrt(2*np.pi))])
          elif l==2 and m==-2:
                return np.array([0,-0.5*(np.sqrt(5/(2*np.pi)))*np.cos(2*phi)*np.sin(th),(np.sqrt(5/(2*np.pi)))*np.cos(phi)*np.cos(th)*np.sin(phi)])
          elif l==3 and m==2:
                return np.array([0,(1/8)*(np.sqrt(35/(np.pi)))*(np.sin(2*th))*np.sin(2*phi),(1/16)*(np.sqrt(35/(np.pi)))*(1 + 3*np.cos(2*th))*np.cos(2*phi)*np.sin(th)])
          elif l==4 and m==-2:
                return np.array([0,-1*(3/16)*(1/np.sqrt(np.pi))*(5+ 7*np.cos(2*th))*np.cos(2*phi)*np.sin(phi),(3/16)*(1/np.sqrt(np.pi))*(-1 + 7*np.cos(2*th))*np.sin(2*th)*np.sin(2*phi)])
          elif l==4 and m==-4:
                return np.array([0,-(3/8)*(np.sqrt((7/np.pi)))*np.cos(4*th)*(np.sin(th)**3),(3/8)*(np.sqrt((7/np.pi)))*np.cos(th)*(np.sin(th)**3)*np.sin(4*phi)])
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
            #res=res+wangles.iloc[i,3]*vf.iloc[i].dot(psilmr(l,m,wangles.iloc[i,1],wangles.iloc[i,2]))
            res=res+wangles.iloc[i,3]*vf.iloc[i].dot(vsh(type,l,m,wangles.iloc[i,1],wangles.iloc[i,2]))
        return res
    elif type==2:
        res=0
        for i in range(32):
            #res=res+wangles.iloc[i,3]*vf.iloc[i].dot(philmr(l,m,wangles.iloc[i,1],wangles.iloc[i,2]))
            res=res+wangles.iloc[i,3]*vf.iloc[i].dot(vsh(type,l,m,wangles.iloc[i,1],wangles.iloc[i,2]))
        return res
    else:
        print("Wrong input for VSHproj")
        exit()
###############################################################################
# Convert torques and rotate torques based on the crystalographic orientation #
def convtrq(set1):
    newset=set1.copy()
    #newset.th=set1.th
    newset.th=np.pi-set1.th
    #### This bypasses a numerical error from approaching 0 from the wrong side###
    if ore==111:
        #print('111 orientation detected, rotating phi angle')
        #newset.phi=-(np.pi+set1.phi) + np.pi/6
        newset.phi=-(set1.phi) + np.pi/6
    else:
        newset.phi=-(set1.phi)
        #newset.phi=set1.phi
    newset.ty=-set1.ty
    newset.tz=-set1.tz
    #newset.ty=set1.ty
    #newset.tz=set1.tz
    return newset
##### This is for 111 orientation #############################################
def trqrot(set):
    newset=set.copy()
    newset.tx=set.tx*cos(np.pi/6)+set.ty*sin(np.pi/6)
    newset.ty=set.ty*cos(np.pi/6)-set.tx*sin(np.pi/6)
    return newset

########## Fit torque function##############################

def fitTrq(set1,set2,m,*args):
    if len(args)!=0:
        parset=args[0]
    else:
        parset=25
    if set1.shape!=set2.shape:
        print('Warning, datasets of different sizes')
        exit
    if ore==111:
        #print('111 orientation detected, rotating torques')
        tr=trqrot(set1)
        tl=trqrot(set2)
    else:
        tr=set1
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
    VSHT1 =[VSHproj(fsurfsets,1,2,-2),VSHproj(fsurfsets,1,3,2), VSHproj(fsurfsets,1,4,-2),VSHproj(fsurfsets,1,4,-4)]
    VSHT2 =[VSHproj(fsurfsets,2,2,-2),VSHproj(fsurfsets,2,3,2), VSHproj(fsurfsets,2,4,-2),VSHproj(fsurfsets,2,4,-4)]
    return VSHsym,VSHas,VSHT1,VSHT2
#    return VSHsym,VSHas

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
    maxpl=dsl.iloc[-1,3]
    for a in range(1,33):
        for p in range(pls[0],pls[-1]+1):
	    #######
            lp=maxpl+1-p
            #cpl=dsl.loc[((dsl['PL']==lp) & (dsl['angle']==a))][zl[0]-1:zl[-1]][['tx','ty','tz']]
            #cpl.to_csv('left_first_'+str(a)+'_'+str(p)+'.csv')
            cpl=dsl.loc[((dsl['PL']==p) & (dsl['angle']==a))][zl[0]-1:zl[-1]][['tx','ty','tz']].sum().to_frame().transpose()
            ###########################################
	    #cpl=dsl.loc[((dsl['PL']==p) & (dsl['angle']==a))][zl[0]-1:zl[-1]][['tx','ty','tz']].sum().to_frame().transpose() 
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
    #dffl.to_csv('left_df.csv')
    #dffr.to_csv('right_df.csv')
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
        #if p==1:
        #    lsftl.to_csv('mode_left_'+str(p)+'.csv')
        #sftr.to_csv('mode_right_'+str(p)+'.csv')
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


##############################################################################
# MODE: 1 (Takes full SOT file and calculates SOT coefficient [Similar to mathematica script])####
# MODE: 2 Uses csv file from Master Maker to calculate layer resolved Harmonics
# MODE: 3 Averages
##############################################################################

arguments=sys.argv
inputs=arguments[1:]
#### Testing parameters #######################################################
#inputs=[1,'x2_trq_com1pt_l_x1.0_384.dat','x2_trq_com1pt_r_x1.0_384.dat',1]
#inputs=['trq_CoMPt_x2_l_x1.0sres1_25.dat','trq_CoMPt_x2_r_x1.0sres1_25.dat',1]
#inputs=[23,'CoMPt_master',1,70,1,18,0.258*100000*0.012043]
#inputs=[3,'Harm.out',10,60]
#,0.258*100000*0.012043
#inputs=['--usage']
###############################################################################
if ((len(inputs)==1) and (inputs[0]=='--usage')):
    print('SoT_fit_v2.py')
    print('This sript uses various arguments based on the given mode')
    print('Basic use is "python SoT_fit_v3.py [mode] [required arguments] {optional arguments}  "')
    print('Mode 1: Calculates coefficients using legacy files')
    print('Arguments: [file for L] [file for R] [magnetization of PL]')
    print('Mode 2: Calculates SOT coefficients for each PL for the given z layers outputs them to Harm.out')
    print('Arguments: [Master files prefix] [1st PL] [final PL] [1st zlayer] [final zlayer] {scaling}')
    print('Mode 3: Calculates SOT coefficients averaged over the number of PL in a "Harm.out" file')
    print('Arguments: ["Harm.out" file] {itial PL} {final PL} {sacaling} ')
    print('Mode 32: Combination of modes 2 & 3 creates "harm.out" files and displays average results' )
    print('Arguments: [Master files prefix] [1st PL] [final PL] [1st zlayer] [final zlayer] {scaling}')
    exit()
else:
    mode=int(inputs[0])
    if mode==1:
        print('Calculating coefficients for SOT from legacy file')
        if (len(inputs[1:]))%3!=0:
            print('even number of files\n Files must be in (L R mag) triplets for mode=1')
            print('use "python SoT_fit_v3.py --usage" to see specifics')
            exit()
        inputls=[]
        for i in range(0,len(inputs)-1,3):
            ds1=inputs[1+i:i+4][0]
            ds2=inputs[1+i:i+4][1]
            m=float(inputs[1+i:i+4][2])
            datal=df_create(ds1)
            datar=df_create(ds2)
            #datal.to_csv('mode_left.csv')
            #datar.to_csv('mode_right.csv') 
            ##################### Setting coefficient for data set ########################
            #mult = input('Magnetization of the system? (default 11.2ub)')
            if m==1.0:
                print('Using default mag 11.2, multiplier is 2.58e5')
                m=0.258*100000*0.012043
            elif m==0:
                 print('m set to 0, multiplier is now 1')
                 m=1
            else:
                m=0.258*100000*(11.2/m)*0.012043
            ###############################################################################
        print(fitTrq(datal,datar,m))
    elif mode==2:
        print('Calculating vector spherical harmonics for each PL')
        if len(inputs)<2:
            print('Not enough arguments provided.')
            print('use "python SoT_fit_v3.py --usage" to see specifics')
            exit()
        elif len(inputs)>8:
            print('Too many arguments given. Exiting')
            print('use "python SoT_fit_v3.py --usage" to see specifics')
            exit()
        else:
            filename=inputs[1]
            filel=filename+'_L_trq.csv'
            filer=filename+'_R_trq.csv'
            pls=[int(inputs[2]),int(inputs[3])]
            zl=[int(inputs[4]),int(inputs[5])]
            if len(inputs)<7:
                print('No scaling provided, coefficients will be in dimensionless units.')
                scl=1
            else:
                scl=float(inputs[6])
            harm_fit(filel,filer,pls,zl,scl)
            print('Harmonics out to file Harm.out')
    elif mode==3:
        if len(inputs)<2:
            print('No file given. Exiting')
            print('use "python SoT_fit_v3.py --usage" to see specifics')
            exit()
        elif len(inputs)>5:
            print('To many arguments given. Exiting.')
            print('use "python SoT_fit_v3.py --usage" to see specifics')
            exit()
        else:
            fileh=inputs[1]
            print('Averaging over PL harmonics in '+str(fileh)+' file')
            if ((len(inputs)==2) or (len(inputs)==4)):
                print('No scaling provided')
                scale=1
            elif ((len(inputs)==3) or (len(inputs)==5)):
                scale=float(inputs[-1])
                print('Scaling torques by '+str(scale))
            if len(inputs)>3:
                spl=int(inputs[2])-1
                fpl=int(inputs[3])
                print('Averaging over PL starting from '+str(spl+1)+' to '+str(fpl))
                df=pd.read_csv(fileh,names=['A1','A2','A3','A4','B1','B2','B3','B4','T11','T12','T13','T14','T21','T22','T23','T24'],delimiter=' ')
                df.iloc[0:20]
                df=df.iloc[spl:fpl]
            else:
                print('Averaging over all PL')
                df=pd.read_csv(fileh,names=['A1','A2','A3','A4','B1','B2','B3','B4','T11','T12','T13','T14','T21','T22','T23','T24'],delimiter=' ')
                print(df.head())
            print(scale)
            df=df*scale
            print(df.mean().to_frame().transpose().to_string(index=False))
    elif mode==23:
        print('Calculating vector spherical harmonics for each PL')
        if len(inputs)<2:
            print('Not enough arguments provided.')
            print('use "python SoT_fit_v3.py --usage" to see specifics')
            exit()
        elif len(inputs)>8:
            print('Too many arguments given. Exiting')
            print('use "python SoT_fit_v3.py --usage" to see specifics')
            exit()
        else:
            filename=inputs[1]
            filel=filename+'_L_trq.csv'
            filer=filename+'_R_trq.csv'
            pls=[int(inputs[2]),int(inputs[3])]
            zl=[int(inputs[4]),int(inputs[5])]
            if len(inputs)<7:
                print('No scaling provided, coefficients will be in dimensionless units.')
                scl=1
            else:
                scl=float(inputs[6])
            harm_fit(filel,filer,pls,zl,scl)
            df=pd.read_csv('Harm.out',names=['A1','A2','A3','A4','B1','B2','B3','B4'],delimiter=' ')
            print('SOT coefficients averaged over all PL in the harmonics files' )
            print(df.mean().to_frame().transpose().to_string(index=False))
    else:
        print('No mode selected, aborting')
        exit()
