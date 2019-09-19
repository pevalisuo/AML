#!/usr/bin/python

import pandas as pd
import numpy as np

#A=np.random.normal(2,2,100)
A=np.random.weibull(0.5,100)+1
B=np.random.normal(5,0.5,50)
C=np.random.normal(9,1.5,50)

a=np.ones(100)
b=np.zeros(100)

D=pd.DataFrame({'X': np.hstack((A,B,C)), 'Y': np.hstack((a,b))})

D.to_csv('croctestdata.csv', index=False)

#D2=pd.read_csv('croctestdata.csv')
