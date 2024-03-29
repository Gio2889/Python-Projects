# @Author: Giovanni G. Baez Flores
# @Date:   2020-06-12T13:25:14-05:00
# @Email:  gbaez89@gmail.com
# @Last modified by:   Giovanni G. Baez Flores
# @Last modified time: 2020-06-24T16:18:37-05:00

from time import process_time
import pandas as pd
import numpy as np
import os
import sys
###############################################################################
### Data Frame creator, can work for single angle if provided same starting point
### Create a datafram of Tx Ty Tz index by PL, Angle, and Z layer index
###############################################################################

def ang_lay_df_maker(idis,ang,ln,wid,nspec,dr,flnm):
#    tmstp=10 #time step in minutes
    for side in ['R','L']:
        for s in range(ang[0],ang[-1]+1):
            res=np.array([])
            cnfgcnt=0
            for l in range(idis[0],idis[-1]+1):
                if side=='L':
                    path='Flip/'+dr+'/'+str(l)+'/'+str(s)+'/z1/384/'
                    exit()
                else:
                    #path=dr+'/'+str(l)+'/'+str(s)+'/z1/384/'
                    path=str(l)+'/'+str(s)+'/z1/384/'
                    #path='1/1/z1/384/'
                if (not(os.path.exists(path+'completed'))):
                    print('lmpg time in config '+str(l)+', angle '+str(s)+' is incomplete.')
                    print('Calculation might not have finished')
                    print('Skiping calculation')
                    continue
                else:
                    cnfgcnt+=1
                    num_lines = sum(1 for line in open(path+'lmpg.out'))-nspec*wid*ln*4-3
                    #num_lines
                    ds=pd.read_csv(path+'lmpg.out',skiprows=num_lines,header=None,names=['i'],delimiter='\t',dtype='str')
                    ds=ds.loc[3::4]=ds.loc[3::4].astype(str)
                    ds=ds['i'].astype('str').str.split(expand=True)
                    ds=ds.reset_index().iloc[:,[2,3,4]].rename(columns={1:"tx", 2:"ty",3:"tz"}).astype('float64')
                    npa=ds.to_numpy()
                    for i in range(ln):
                        pl=npa[i*(nspec*wid):i*(nspec*wid)+nspec*wid-1]
                        for j in range(0,nspec):
                            if j==0:
                                ar=pl[j::nspec].sum(axis=0)/wid
                            elif j==1:
                                carr=pl[j::nspec].sum(axis=0)/wid
                                ar=np.concatenate(([ar],[carr]),axis=0)
                            else:
                                carr=pl[j::nspec].sum(axis=0)/wid
                                ar=np.concatenate((ar,[carr]),axis=0)
                        ar=np.c_[ar,np.full(ar.shape[0],int(i+1))]
                        ar=np.c_[ar,np.array(list(range(1,nspecls -l+1)))]
                        if i==0:
                            fdf=ar
                        else:
                            fdf=np.concatenate((fdf,ar),axis=0)
                    fdf=np.c_[fdf,np.full(fdf.shape[0],s)]
                    if cnfgcnt==1:
                        res=fdf
                    else:
                        res[:,:3]=res[:,:3]+fdf[:,:3]
            res[:,:3]=res[:,:3]/(cnfgcnt)
            if s==ang[0]:
                res2=res
            else:
                res2=np.concatenate((res2,res),axis=0)
            print('Angle '+str(s)+' complete for side '+side)
        fndf=pd.DataFrame(res2,columns=['tx','ty','tz','PL','Zlayer','angle'])
        print(fndf.info())
        fndf[['PL','Zlayer','angle']]=fndf[['PL','Zlayer','angle']].astype('int32')
        print(fndf.info())
        #pd.options.display.float_format = "{:,.6f}".format
        print(fndf.head())
        flnm2=flnm+'_'+side+'.csv'
        fndf.to_csv(flnm2,float_format='%.6f')
        #np.savetxt(flnm2, res2, delimiter=",")
###############################################################################
#set up directories
cwd=os.getcwd()
os.chdir(cwd)
arguments=sys.argv
inputs=arguments[1:]
inputs=[1,3,1,3,70,2,21,'x1.0','numpy_test']
ids=[int(inputs[0]),int(inputs[1])] # list of disorder configurations
ang=[int(inputs[2]),int(inputs[3])] # list of angles to collect
ln=int(inputs[4]) # lenght of the system
yl=int(inputs[5]) # width of the system
ns=int(inputs[6]) # number of z layers
dr=inputs[7] # directory where the runs are.
name=inputs[8] # name of the output file
print('Creating DF for layer resolve torque harmonics')
t1_start=process_time()
ang_lay_df_maker(ids,ang,ln,yl,ns,dr,name)
print('Master file '+name+' finished.\n This file contains torque data for '+str(ang[1]-ang[0]+1)+' angles, '+str(ln)+' PL, and '+str(ns)+' layer in the z direction.\n The data is averaged over '+str(ids[1]-ids[0]+1)+' disorder configurations and '+ str(yl) +' lateral stacks.')
# Stop the stopwatch / counter
t1_stop = process_time()
print("Elapsed time:", t1_stop/60, t1_start/60)
print("Elapsed time during the whole program in seconds:", (t1_stop-t1_start)/60)

#dkbr=pd.read_csv('KDB_master_180_20dis_R.csv')
#for i in range(1,5):
#    if i==1:
#        ty=dkbr.loc[((dkbr['angle']==6) & (dkbr['Zlayer']==i))]['ty'].to_frame().reset_index()
#    else:
#        ty=ty+dkbr.loc[((dkbr['angle']==6)  & (dkbr['Zlayer']==i))]['ty'].to_frame().reset_index()
#dkbr.loc[((dkbr['angle']==6) & (dkbr['PL']==1) &(dkbr['Zlayer']<5))]
#ty
