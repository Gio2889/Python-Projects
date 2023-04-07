# @Author: Giovanni G. Baez Flores
# @Date:   2021-11-14T15:07:22-06:00
# @Email:  gbaez89@gmail.com
# @Last modified by:   Giovanni G. Baez Flores
# @Last modified time: 2021-11-14T16:33:41-06:00



import os
import pandas as pd
import numpy as np
import datetime as dt

rawdat=pd.read_csv("Members_5671779.csv")
data=rawdat[['Name','Tier','Access Expiration']]
data=data.loc[data['Tier'] != "Sidekick"]
data=data.loc[data['Tier'] != "Hero in Training"]
today=  dt.date.today()
month=today.strftime("%m")
year=today.strftime("%Y")
if month == 12:
    nextmonth=1
else:
    nextmonth= int(month) + 1

firstdmonth = year+"-"+str(nextmonth)+"-01"
data['Access Expiration']=data['Access Expiration'].fillna(0)
dates=data.loc[data['Access Expiration'] != 0 ].iloc[:,2].str.split(" ")
dates=dates.str[0]
olddates=data.loc[data['Access Expiration'] != 0 ].iloc[:,2]
strdic=dict(zip(olddates,dates))
data['Access Expiration'].replace(strdic,inplace=True)
finaldata=data.loc[data['Access Expiration'] != firstdmonth ]
numpeople=finaldata.shape[0]
rmvplp=data.loc[data['Access Expiration'] == firstdmonth ].shape[0]
print("Total number of people in the list: " + str(numpeople))
print("People removed this month : " + str(rmvplp))
finaldata.to_csv("Filter_data_for_"+month+"_"+year+".csv")
