from zipfile import BadZipfile
from sqlalchemy import create_engine
from pandas.io import sql
import pymysql
import string,re
import xlrd
import  pandas as pd
import numpy as np
import glob
p=0
badfile=[]
all_data = pd.DataFrame()
for f in glob.glob('/home/farmguide/myproject/soil_health_card_for_all_india/NutrientStatusFarmerWise_*.xlsx'):
    p=p+1
    try:
        DFF = pd.read_excel(f,header=None)
        a=[]
        a.append(DFF[1].iloc[2])
        a.append(DFF[4].iloc[1])
        a.append(DFF[0].iloc[7].split(':')[-1]) # extracting useful names from different cell in excel


        DFF.drop(DFF.columns[[1,3,4,7,9,18,23]],axis=1,inplace=True) #deleting coloumn containing na values

        l=[]
        j=0
        for i in DFF.iloc[6]:
            if j>0:
                l.append(i)     #extracting column names from table

            j=j+1

        b='Village'
        DFF['village']=DFF[2].apply(lambda x: x.split(':')[-1] if (b in str(x))==True else np.nan)
        DFF['village']=DFF['village'].ffill() #extracting village and creating another column of village name

        DFF.drop(DFF.index[0:9],inplace=True)  #deleting starting rows with no data

        c=DFF[DFF[2].str.contains('Village')==True].index.tolist()
        for i in c:
            DFF.drop(i,inplace=True)   

        DFF=DFF[pd.to_numeric(DFF[0], errors='coerce').notnull()] #deleting text at the bottom in each table

        vill=DFF['village']
        DFF.drop([0,'village'],axis=1,inplace=True)

        li=[]
        for i in DFF.columns:
            li.append(i)

        DFF.rename(columns={i:j for i,j in zip(li,l)}, inplace=True)

        DFF.insert(0,'State',a[0])
        DFF.insert(1,'District',a[1])
        DFF.insert(2,'Sub District',a[2])
        DFF.insert(3,'Village',vill)
        DFF.columns = [x.lower() for x in DFF.columns]
        DFF.columns=[re.sub('[/,?!\t\n ]+', '_', s) for s in DFF.columns]
        DFF.columns=[re.sub('[.]+', '', s) for s in DFF.columns]

        all_data = all_data.append(DFF,ignore_index=True)
        engine = create_engine('mysql://root:farmguide@localhost:3306/testdb?charset=utf8mb4',pool_size=10, max_overflow=20)
            
        with engine.connect() as conn, conn.begin():
            DFF[DFF.columns].to_sql('soil_health_card', conn, if_exists='append',index=False, chunksize=100, dtype=None)
        print(p)
    except BadZipFile as e:
        print('e')
        badfile.append(f)
        continue




all_data.to_csv('all_india_soil_health.csv',index=False)  #saving dataframe to csv