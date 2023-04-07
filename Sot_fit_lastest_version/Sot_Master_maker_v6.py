# @Author: Giovanni G. Baez Flores
# @Date:   2020-06-12T13:25:14-05:00
# @Email:  gbaez89@gmail.com
# @Last modified by:   Giovanni G. Baez Flores
# @Last modified time: 2020-12-23T11:00:00-05:00

from time import process_time
import pandas as pd
import numpy as np
import os
import sys
pd.set_option("display.precision", 16)
np.set_printoptions(16)
###############################################################################
### Data Frame creator, can work for single angle if provided same starting point
### Create a datafram of Tx Ty Tz index by PL, Angle, and Z layer index
###############################################################################

def ang_lay_df_maker(mode,idis,ang,ln,wid,nspec,dr,flnm):
    #############  this is a special addition to the path ################
    ### Set the use of k-points as for labeling the path #################
    ### Set variable kpt to 'yes'
    kpt='yes'
    kp=int(768/wid)
    #######################################################################
    if mode==1:
        print('Creating master files for torque data')
        procs=[1]
    elif mode==2:
        print('Creating master files for spin densities')
        procs=[2]
    elif mode==3:
        print('Creating master files for torque data & spin densities')
        procs=[1,2]
    elif mode==4
        print('Creating master files for torque data averaging over PLs')
        procs=[1]
    else:
        print('No valid mode selected. Exiting')
        exit()
    #    tmstp=10 #time step in minutes
    for p in procs:
        if p==1:
            datlocs=3
            datcols=[2,3,4]
            datcoldict={1:"tx", 2:"ty",3:"tz"}
            datcolnames=['tx','ty','tz','PL','Zlayer','angle']
            filesufx='_trq'
            if mode == 3:
                print ('Gathering data for torques')
        elif p==2:
            datlocs=1
            datcols=[4,5,6]
            datcoldict={3:"sx", 4:"sy",5:"sz"}
            datcolnames=['sx','sy','sz','PL','Zlayer','angle']
            filesufx='_spn_dens'
            if mode == 3 :
                print ('Gathering data for spin densities')
        for side in ['R','L']:
            for s in range(ang[0],ang[-1]+1):
                res=np.array([])
                cnfgcnt=0
                for l in range(idis[0],idis[-1]+1):
                    if side=='L':
                        path='Flip/'+dr+'/'+str(l)+'/'+str(s)+'/z1/'
                        if kpt=='yes':
                            path=path+str(kp)+'/'
                        #exit()
                    else:
                        #path=str(l)+'/'+str(s)+'/z1/'
                        path=dr+'/'+str(l)+'/'+str(s)+'/z1/'
                        if kpt=='yes':
                            path=path+str(kp)+'/'
                            #path='1/1/z1/384/'
                    if (not(os.path.exists(path+'completed'))):
                        print('lmpg file in config '+str(l)+', angle '+str(s)+' is incomplete; skipping')
                        continue
                    elif not((os.path.exists(path+'lmpg.out'))):
                        print('lmpg file in cofig '+str(l)+', angle '+str(s)+' is missing; skipping')
                        continue
                    else:
                        lines=sum(1 for line in open(path+'lmpg.out'))
                        num_lines = lines - nspec*wid*ln*4 -3
                        with open(path+'lmpg.out') as fp:
                            for i, line in enumerate(fp):
                                if i == lines-2:
                                    exitcode= line.split()[1]
                                    break
                        if exitcode != '0':
                            print('lmpg file in cofig '+str(l)+', angle '+str(s)+' did not exit correctly; skipping')
                            continue
                        cnfgcnt+=1
                        ds=pd.read_csv(path+'lmpg.out',skiprows=num_lines,header=None,names=['i'],delimiter='\t',dtype='str')
                        ds=ds.loc[datlocs::4].astype(str)
                        if p == 2:
                            ds.drop(ds.tail(1).index,inplace=True)
                        ds=ds['i'].astype('str').str.split(expand=True)
                        ds=ds.reset_index().iloc[:,datcols].rename(columns=datcoldict).astype('float64')
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
                            ar=np.c_[ar,np.array(list(range(1,nspec+1)))]
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
            fndf=pd.DataFrame(res2,columns=datcolnames)
            if side=='L':
                maxpl=fndf['PL'].max()
                fndf['PL']=(maxpl - (fndf['PL'] -1))
            fndf[['PL','Zlayer','angle']]=fndf[['PL','Zlayer','angle']].astype('int32')
            #print(fndf.head())
            #print(fndf.info())
            #pd.options.display.float_format = "{:,.6f}".format
            flnm2=flnm+'_'+side+filesufx+'.csv'
            fndf.to_csv(flnm2,float_format='%.6f')
            #np.savetxt(flnm2, res2, delimiter=",")


###############################################################################
#set up directories
cwd=os.getcwd()
os.chdir(cwd)
arguments=sys.argv
inputs=arguments[1:]
#inputs=[2,1,3,1,3,70,2,21,'x1.0','numpy_test']
#inputs=['--usage']
if ((len(inputs)==1) and (inputs[0]=='--usage')):
    print('Sot_Master_maker_v5.py takes 10 araguments')
    print('[mode] [1st config] [final config] [1st ang.] [final ang.] [lenght] [width] [z layers] [directory] [file name]')
    exit()
elif len(inputs)!=10 :
    print('Not enough arguments provided, exiting')
    print('Use "Sot_Master_maker_v5.py --usage" to see the requiered arguments')
    exit()
mode=int(inputs[0])
ids=[int(inputs[1]),int(inputs[2])] # list of disorder configurations
ang=[int(inputs[3]),int(inputs[4])] # list of angles to collect
ln=int(inputs[5]) # lenght of the system
yl=int(inputs[6]) # width of the system
ns=int(inputs[7]) # number of z layers
dr=inputs[8] # directory where the runs are.
name=inputs[9] # name of the output file
print('-------- Starting Master file creation---------')
t1_start=process_time()
ang_lay_df_maker(mode,ids,ang,ln,yl,ns,dr,name)
print('Master file '+name+' finished.\n This file contains torque data for '+str(ang[1]-ang[0]+1)+' angles, '+str(ln)+' PL, and '+str(ns)+' layer in the z direction.\n The data is averaged over '+str(ids[1]-ids[0]+1)+' disorder configurations and '+ str(yl) +' lateral stacks.')
# Stop the stopwatch / counter
t1_stop = process_time()
#print("Elapsed time:", t1_stop/60, t1_start/60)
print("Elapsed time during the whole program in minutes:", (t1_stop-t1_start)/60)

#dkbr=pd.read_csv('KDB_master_180_20dis_R.csv')
#for i in range(1,5):
#    if i==1:
#        ty=dkbr.loc[((dkbr['angle']==6) & (dkbr['Zlayer']==i))]['ty'].to_frame().reset_index()
#    else:
#        ty=ty+dkbr.loc[((dkbr['angle']==6)  & (dkbr['Zlayer']==i))]['ty'].to_frame().reset_index()
#dkbr.loc[((dkbr['angle']==6) & (dkbr['PL']==1) &(dkbr['Zlayer']<5))]
#ty
