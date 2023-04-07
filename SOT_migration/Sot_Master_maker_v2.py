# @Author: Giovanni G. Baez Flores
# @Date:   2020-06-12T13:25:14-05:00
# @Email:  gbaez89@gmail.com
# @Last modified by:   Giovanni G. Baez Flores
# @Last modified time: 2020-06-23T08:59:21-05:00

from time import process_time
import pandas as pd
import os
import sys
###############################################################################
### Data Frame creator, can work for single angle if provided same starting point
### Create a datafram of Tx Ty Tz index by PL, Angle, and Z layer index
###############################################################################

def ang_lay_df_maker(idis,ang,ln,wid,nspec,dr,flnm):
    tmstp=10 #time step in minutes
    for side in ['R','L']:
        for s in range(ang[0],ang[-1]+1):
            skpcnt=0
            for l in range(idis[0],idis[-1]+1):
                if side=='L':
                    path='Flip/'+dr+'/'+str(l)+'/'+str(s)+'/z1/384/lmpg.out'
                else:
                    path=dr+'/'+str(l)+'/'+str(s)+'/z1/384/lmpg.out'
                with open(path, 'rb') as f:
                    f.seek(-2, os.SEEK_END)
                    while f.read(1) != b'\n':
                        f.seek(-2, os.SEEK_CUR)
                    last_line = f.readline().decode()
                    cputime=last_line.split()[2]
                    if cputime.find('m')==-1:
                        cputime=float(cputime.split('s')[0])/60
                    elif cputime.find('s')==-1:
                        cputime=float(cputime.split('m')[0])
                print(cputime)
                if cputime<tmstp:
                    print('lmpg time in config '+str(l)+', angle '+str(s)+' is below the given time step or missing.')
                    print('Calculation might not have finished')
                    print('Skiping calculation')
                    skpcnt+=1
                    continue
                else:
                    num_lines = sum(1 for line in open(path))-nspec*wid*ln*4-3
                    num_lines
                    ds=pd.read_csv(path,skiprows=num_lines,header=None,names=['i'],delimiter='\t',dtype='str')
                    ds=ds.loc[3::4]=ds.loc[3::4].astype(str)
                    ds=ds['i'].astype('str').str.split(expand=True)
                    ds=ds.reset_index().iloc[:,[2,3,4]].rename(columns={1:"tx", 2:"ty",3:"tz"}).astype('float64')
                    for i in range(ln):
                        pl=ds.loc[i*(nspec*wid):i*(nspec*wid)+nspec*wid-1]
                        for j in range(0,nspec):
                            if j==0:
                                df=pl[j::nspec].sum().to_frame().transpose()

                            else:
                                df=df.append(pl[j::nspec].sum().to_frame().transpose()/wid)
                        df=df.reset_index(drop=True)
                        df['PL']=i+1
                        df['Zlayer']=df.index+1
                        if i==0:
                            fdf=df
                        else:
                            fdf=fdf.append(df)
                    fdf['angle']=s
                    if l==1:
                        res=fdf
                    else:
                        res[['tx','ty','tz']]=res[['tx','ty','tz']]+fdf[['tx','ty','tz']]
            res[['tx','ty','tz']]=res[['tx','ty','tz']].div(len(list(range(idis[0],idis[-1]+1)))-skpcnt)
            res[['tx','ty','tz']]=res[['tx','ty','tz']].round(6)
            if s==ang[0]:
                res2=res
            else:
                res2=pd.concat([res2,res],ignore_index=True)
            print('Angle '+str(s)+'complete for side '+side)
        flnm2=flnm+'_'+side+'.csv'
        res2.to_csv(flnm2)
###############################################################################
#set up directories
cwd=os.getcwd()
os.chdir(cwd)
arguments=sys.argv
inputs=arguments[1:]
#inputs=[1,3,1,3,70,2,18,'x1.0','name']
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
