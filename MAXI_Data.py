# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:49:01 2023

@author: User
"""

import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import numpy as np
import fathon
from fathon import fathonUtils as fu
import pandas as pd
# LEDA 138501 J0209+524
lmxb_dic = {'Her X-1':'J1657+353/J1657+353','Cyg X-2':'J2144+383/J2144+383',
            'SCO X-1':'J1619-156/J1619-156','LMC X-2':'J0520-719/J0520-719',
            'EXO 0748-676':'J0748-677/J0748-677','GRS 1747-312':'J1750-312/J1750-312',
            'GX 339-4':'J1702-487/J1702-487','GX 354-0':'J1731-338/J1731-338',
            'SS 433':'J1911+049/J1911+049'}
hmxb_dic = {'Cen X-3':'J1121-606/J1121-606','Cyg X-1':'J1958+352/J1958+352',
            'LMC X-3':'J0538-640/J0538-640','LMC X-4':'J0532-663/J0532-663',
            'SMC X-1':'J0117-734/J0117-734'}
lmxb_list = ['Her X-1','Cyg X-2','SCO X-1','LMC X-2',
             'EXO 0748-676','GRS 1747-312','GX 339-4','GX 354-0','SS 433']
hmxb_list = ['Cen X-3','Cyg X-1','LMC X-3','LMC X-4','SMC X-1']
ncxb_dic = {'M 31':'J0042+411/J0042+411','Abell 262':'J0152+361/J0152+361',
            '4U 1543-624':'J1547-625/J1547-625'}
ncxb_list = ['M 31','Abell 262','4U 1543-624']
period = ['1day','1orb'] 

#現在要抓的星星
N = 2

#p = 0:1day，1:1orbit
p = 0 

Nowstarname =hmxb_list[N]

Nowstar = hmxb_dic[hmxb_list[N]]

#將數據抓下來
url='http://maxi.riken.jp/star_data/{}_g_lc_{}_all.dat'.format(Nowstar,period[p])
#url = 'http://maxi.riken.jp/star_data/J1839+050/J1839+050_g_lc_1day_all.dat'

html=requests.get(url)
html.encoding='UTF-8' #utf-8 Unicode的可變長度字元編碼
sp=BeautifulSoup(html.text,'lxml') #將網頁內容用BeautifulSoup，解析lxml則是用來解析處理requests取得的數據
#sp for split
sp=str(sp) #將整串數據分割成各個數字
sp=sp.split() 
lengthofsp = len(sp) 
lengthofsp = int((lengthofsp-10)/9)
#print(lengthofsp)
''
#把各個數據建成列表
Howmanydata = lengthofsp #決定要輸入多少數據
#Sampling = 5    #多少點取一個樣
#print('-----')
date=[]
twototwentykeV=[]
errtot=[]
twotofourkeV=[]
err4=[]
fourtotenkeV=[]
err10=[]
tentotwentykeV=[]
err20=[]

#print(n)

for a in range(0,Howmanydata):
#時間
    a += 8*a + 9
    date.append(float(sp[a])- float(sp[9]))
    date=list(map(int,date)) #將列表中的元素換成浮點，所以可以進行浮點運算

    #print(len(date))
#不同的能量區間
    a += 1
    twototwentykeV.append(float(sp[a]))
    
    a += 1
    errtot.append(float(sp[a]))
    
    a += 1
    twotofourkeV.append(float(sp[a]))
    
    a += 1
    err4.append(float(sp[a]))

    a += 1
    fourtotenkeV.append(float(sp[a]))
    
    a += 1
    err10.append(float(sp[a]))

    a += 1
    tentotwentykeV.append(float(sp[a]))
    
    a += 1
    err20.append(float(sp[a]))
    

Dataframe = pd.DataFrame([date, twototwentykeV, errtot, twotofourkeV, err4, fourtotenkeV, err10, tentotwentykeV, err20], 
                         ['date', 'twototwentykeV', 'errtot', 'twotofourkeV', 'err4', 'fourtotenkeV', 'err10', 'tentotwentykeV', 'err20']).T
print(Dataframe)
Dataframe.to_csv('C:/Users/User/Desktop/天文專題/data/{} data from MAXI.csv'.format(Nowstarname))
