import pandas as pd
import numpy as np
import json
mandi=json.loads(open('mandi_profile.json').read())

l=[]
for k in mandi['0']['area_info'].keys():
    l.append(k.split(" ",1)[-1])
    
Area_info= pd.DataFrame(columns=l)
p=0
for q in mandi.keys():
    m=[]
    for r in mandi[q]['area_info'].values():
        m.append(r)
     
    Area_info.loc[p]=m
    p=p+1

l=[]
for i in mandi['0']['general_info'].keys():
    l.append(i.split(" ",1)[-1])
General_info= pd.DataFrame(columns=l)

p=0
for q in mandi.keys():
    m=[]
    for r in mandi[q]['general_info'].values():
        m.append(r)
     
    General_info.loc[p]=m
    p=p+1
l=[]
for i in mandi['0']['admin_info'].keys():
    l.append(i.split(" ",1)[-1])
Admin_info= pd.DataFrame(columns=l)
p=0
for q in mandi.keys():
    m=[]
    for r in mandi[q]['admin_info'].values():
        m.append(r)
     
    Admin_info.loc[p]=m
    p=p+1
l=[]
for i in mandi['0']['connectivity_info'].keys():
    l.append(i.split(" ",1)[-1])
Connectivity_info= pd.DataFrame(columns=l)
p=0
for q in mandi.keys():
    m=[]
    for r in mandi[q]['connectivity_info'].values():
        m.append(r)
     
    Connectivity_info.loc[p]=m
    p=p+1
l=[]
j=0
for i in mandi['0'].keys():
    if j<3:
        l.append(i)
    else:
        break
    j=j+1

info=pd.DataFrame(columns=l)
p=0
for q in mandi.keys():
    j=0
    m=[]
    for i in mandi[q].values():
        if j<3:
            m.append(i) 
           
        else:
            break
        j=j+1
    info.loc[p]=m
    p=p+1

dfnew = pd.concat(
    [
        info,General_info,Admin_info,Connectivity_info
    ], axis=1
)

l=[]
for i in mandi['0']['commodities_info']['0'].keys():
    l.append(i)

    
commodities_info=pd.DataFrame(columns=l)

p=0
for q in mandi.keys():
    
    for a in mandi[q]['commodities_info'].keys():
        m=[]
        for r in mandi[q]['commodities_info'][a].values():
            m.append(r)
        commodities_info.loc[p]=m
        p=p+1   


        
col=[]
for i in  dfnew.columns:
    col.append(i)
      
Repeat=pd.DataFrame(columns=col)
p=0
i=0
for q in mandi.keys():
    for a in mandi[q]['commodities_info'].keys():
        Repeat.loc[p]=dfnew.loc[i]
        p=p+1
    i=i+1

    
p=0
i=0
for q in mandi.keys():
    if len(mandi[q]['commodities_info'].keys())>0: 
        for a in mandi[q]['commodities_info'].keys():
            repeat.loc[p]=dfnew.loc[i]
            p=p+1
        i=i+1
    else:
        repeat.loc[p]=dfnew.loc[i]
        p=p+1
        i=i+1
#Connectivity_info,Admin_info
mandi_Data = pd.concat(
    [
        Repeat,commodities_info
    ], axis=1
)
