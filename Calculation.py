# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 23:50:33 2023

@author: User
"""

from DFA import Tools
from DFA import DFA

import pandas as pd
import time

start_time = time.time()

tags = ['twotofourkeV', 'fourtotenkeV']
#Nowstarname = 'white_noise_blank'
Nowstarname = 'LMC X-3'
period = ''#'1day'
data = pd.read_csv("C:/Users/User/Desktop/arstro/data/{} data from MAXI.csv".format(Nowstarname))
#data = Tools().testing_data()[Nowstarname]

#DFA(data, tag).plotDFA(Nowstarname, period, tag, avg=True)
for tag in tags:
    DFA(data, tag).plotDFA(Nowstarname, period)


end_time = time.time()
print('It took ', (end_time - start_time)/60, ' minutes!!!')
