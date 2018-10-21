
# coding: utf-8

# In[69]:


# GENERATES A REAL-TIME STREAM OF DATA FOR TESTING THE MATPLOTLIB ANIMATION. 
# THIS STREAM SIMULATES THE DATA COMING FROM THE ARDUINO. 


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import os
import sys
import time
import datetime
import math
import plot_animation
import subprocess


# initialize values
x=0
xvalues,yvalues=0,0
t=0

# set the starttime, delta. The stop time is the now+delta
dt=datetime.datetime.now()
my_delta=30
delta=datetime.timedelta(seconds=my_delta)
stoptime=dt+delta

# set the current working directory for the data file
path=os.getcwd()
file='real_time_data.txt'
filename=path+'\\real_time_data.txt'

# genetate data for the specified delta time.
print('start: ',dt)

# plot_animation.the_animator()
# os.system("py plot_animation.py")
# subprocess.Popen("py plot_animation.py",shell=True)


while datetime.datetime.now()<=stoptime:
    
    noise=(np.random.random(1)*2-1)*1
    xvalues=x
#     yvalues=(5*noise)
    t+=0.01
    yvalues=np.asarray(np.sin(2*t*np.pi))*np.ones(1)
    
    file_object=open(filename, 'a')
    file_object.write(str(xvalues)+','+str(yvalues[0])+'\n')
    file_object.close()

    print(xvalues,yvalues[0])
    plot_animation.the_animator(my_delta)
    time.sleep(.5)
    x=x+1
    

print('stop: ',stoptime)

xstr=str(xvalues)
ystr=str(yvalues)

# clearing the values 
del xvalues
del yvalues
del xstr
del ystr

# clearing the file for the next run
open(filename, 'w').close()

