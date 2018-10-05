import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import os

style.use(style='fivethirtyeight')




fig=plt.figure()
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)
##ax1.clear()

def animate(r):
    graph_data=open(r'C:\Users\Crystal\Desktop\Programs\live_plots\real_time_data.txt','r').read()
    lines=graph_data.split('\n')
##    print (lines)
    xs=[]
    ys=[]
    for line in lines:
        if len(line)>1:
            x,y=line.split(',')
            xs.append(float(x))
            ys.append(float(y))

##            print(float(x),float(y))
            
##    ax1.set_ylim(-1,1)
    ax1.set_xlim(0,600)  
    ax1.plot(xs,ys, linewidth=1,color='b')
##    ax2.hist(ys,bins=50,color='blue')
    ax2.acorr(abs(ys),color='blue')

ax1.clear()
ax2.clear()
ani=animation.FuncAnimation(fig,animate,interval=1000)
plt.show()
