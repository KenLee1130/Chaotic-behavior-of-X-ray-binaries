# -*- coding: utf-8 -*-
"""
Created on Thu Apr 20 00:07:56 2023

@author: User
"""

from DFA import DFA
import numpy as np
import matplotlib.pyplot as plt
import time

def Comparing(type='Hurst'):
    if type == 'Hurst':
        number = 1000
        randn = np.random.rand(number)
        cum_randn = np.cumsum(randn)
        
        remove_idx = set(np.random.randint(number, size=100))
        
        randn_blank = [0 if i in remove_idx else randn[i] for i in range(number)]
        cum_randn_blank = [0 if i in remove_idx else cum_randn[i] for i in range(number)]

        #Hurst_rand = DFA(randn, tag= 'White noise').calculateDFA()['Hurst']
        DFA(randn, 'White noise').plotDFA('White noise', 0, 'White noise', True)
        DFA(randn_blank, 'White noise with blanks').plotDFA('White noise comparing', 0, 'White noise with blanks', True)
        
        #Hurst_cum_rand = DFA(cum_randn, tag= 'Red noise').calculateDFA()['Hurst']
        DFA(cum_randn, 'Red noise').plotDFA('Red noise', 0, 'Red noise', True)
        DFA(cum_randn_blank, 'Red noise with blanks').plotDFA('Red noise comparing', 0, 'Red noise with blanks', True)
    
        
starting_time = time.time()
Comparing()
ending_time = time.time()
print(f'Cost: {ending_time - starting_time} sec')
