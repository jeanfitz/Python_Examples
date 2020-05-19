# moving average of Mass covid-19 daily deaths
# may 18, 2020
# JAF


import pandas as pd   # pandas text processing module
import numpy as np    # numerical module
import matplotlib.pyplot as plt  # plot module which mimics Matlab plotting

# from mass.gov website: Data from April 2 to may 16

data=pd.read_csv("death.txt",header=None)  # Read from Mass.gov public health

# 3 day moving average using pandas method
ma=data.rolling(3).mean()

# plot data and 3 day moving average

plt.plot(data,'.')
plt.plot(ma)
plt.title('Mass covid deaths')
plt.xlabel('Days since April 2')
plt.ylabel('Daily covid-19 deaths')
plt.show()

