# -*- coding: utf-8 -*-
"""
Created on Tue Apr 11 14:28:43 2023

@author: User
"""
### DFA
# Define interpolation
# Check the DFA of data has some blanks and DFA of a full data are the same?(Use white noise)
# If the same I can interpolate with histogramic choosing data
# histogram (Monte-Carlo simulation)
# How to piecewise each segment

class Tools:
    def Moving_avg(self, data, decrease_weight, resolution):
        import pandas as pd
        # Convert array of integers to pandas series
        data = pd.Series(data)
        # Get the moving averages of series
        # of observations till the current time
        moving_averages = round(data.ewm(alpha=decrease_weight, adjust=False).mean(), resolution)
          
        # Convert pandas series back to list
        moving_averages_list = moving_averages.tolist()
          
        return moving_averages_list
    
    def testing_data(self):
        import numpy as np
        number = 3000
        blanc_number = 100
        
        white_noise = np.random.rand(number)
        red_noise = np.cumsum(white_noise)
        
        remove_idx = np.random.choice(number, blanc_number, replace=False)
        
        white_noise_blank = [0 if i in remove_idx else white_noise[i] for i in range(number)]
        red_noise_blank = [0 if i in remove_idx else red_noise[i] for i in range(number)]
        
        return {'white_noise':white_noise, 'red_noise':red_noise, 
                'white_noise_blank':white_noise_blank, 'red_noise_blank':red_noise_blank}

class DFA:
    def __init__(self, data, tag, avg=False, test=False):
        self.data = data
        self.tag = tag
        self.avg = avg
        self.test = test
        
    def calculateDFA(self):
        import pandas as pd
        import fathon
        from fathon import fathonUtils as fu
        
        #data_tag = self.data[self.tag]
        
        data = self.data[self.tag] if self.test==False else self.data
        
        data = Tools().Moving_avg(data, 0.5, 10) if self.avg==True else data
        
        data_DFA = fathon.DFA(fu.toAggregated(data))
        winSizes = fu.linRangeByStep(3,len(data))  
        
        # window size: the time resolution (time scale)
        # True: F will recalculate from the tail of this time series
        revSeg = True # False   
        # Calculate to which order
        polOrd = 1  
        
        # n: window size
        n, Fluctuation = data_DFA.computeFlucVec(winSizes, revSeg=revSeg, polOrd=polOrd)
        
        ## Fitting the figure of log(n)-log(H)
        # Hurst: Hurst exponent
        # H_intercept: The intercept of the line
        Hurst, H_intercept = data_DFA.fitFlucVec()
        
        # Aggregate n and Fluctuation data
        DFAinfo = pd.DataFrame([n, Fluctuation], 
                               ['n', 'Fluctuation']).T
        
        return {'DFAinfo': DFAinfo, 'Hurst': Hurst, 'H_intercept': H_intercept}
    
    def plotDFA(self, Nowstarname, period):
        import matplotlib.pyplot as plt
        import numpy as np
        
        dfa = DFA(self.data, self.tag, self.avg, self.test)
        
        tag = self.tag if self.test==False else Nowstarname 
        
        n = dfa.calculateDFA()['DFAinfo']['n']
        Fluctuation = dfa.calculateDFA()['DFAinfo']['Fluctuation']
        Hurst = dfa.calculateDFA()['Hurst']
        H_intercept = dfa.calculateDFA()['H_intercept']

        plt.scatter(np.log(n), np.log(Fluctuation),s = 10)
        plt.plot(np.log(n), H_intercept + Hurst*np.log(n), linewidth=2, linestyle="-",
                 label='Hurst exponent of {} = {:.2f}, avg={}'.format(tag, Hurst, self.avg))
        
        plt.grid()
        plt.xlabel('ln(n)', fontsize=14)
        plt.ylabel('ln(F(n))', fontsize=14)
        plt.title('DFA of {} ({}) '.format(Nowstarname,period), fontsize=14)
        plt.legend(loc=0, fontsize=14)
        plt.show()
        
    def hist(self):
        import matplotlib.pyplot as plt
        n, bins, patches = plt.hist(x=self.data, bins='auto', density = 1, color='#0504aa',alpha=0.7, rwidth=0.85)
        plt.grid(axis='y', alpha=0.75)
        plt.xlabel('Value')
        plt.ylabel('Frequency')
        plt.title('My Very Own Histogram')
        plt.text(-2, 0.35, r'$\mu=15, b=3$')
        #maxfreq = n.max()


    