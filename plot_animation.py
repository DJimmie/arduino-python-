import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import os



style.use(style='fivethirtyeight')

def animate(r):
    global x_range
##    print("I'm Working!!")


    graph_data=open(os.getcwd()+'\\real_time_data.txt','r').read()
    lines=graph_data.split('\n')
##    print (lines)
    xs=[]
    ys=[]
    for line in lines:
        if len(line)>1:
            x,y,z=line.split(',')
            xs.append(float(x))
            ys.append(float(y))

##            print(float(x),float(y))
            
##    ax1.set_ylim(-1,1)
    ax1.set_xlim(0,x_range)  
    ax1.plot(xs,ys, linewidth=1,color='b')
    ax2.hist(ys,bins=50,color='blue')
##        ax2.hist(abs(ys),color='blue')



def get_plot_settings():
    """ Reads the plot settings from the plot_settings.txt."""

    path=os.getcwd()
    file='plot_settings.txt'
    filename=path+'\\plot_settings.txt'

    with open (filename) as f_obj:
        for line in f_obj:
            print(line.rstrip())
            p_set_1=float(line.rstrip())
            return p_set_1
    
 
if __name__ == '__main__':
    
 
    x_range=get_plot_settings()
    print(x_range)
    
    
    fig=plt.figure()
    ax1=fig.add_subplot(2,1,1)
    ax2=fig.add_subplot(2,1,2)
    ##ax1.clear()
    ax1.clear()
    ax2.clear()
    ani=animation.FuncAnimation(fig,animate,interval=1000,blit=False)
    plt.show()
    print ('im done')
