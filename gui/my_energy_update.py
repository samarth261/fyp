#!/usr/bin/python3.5


import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mp
import time

'''
x = np.linspace(0, 6*np.pi, 100)
y = np.sin(x)

# You probably won't need this if you're embedding things in a tkinter plot...
plt.ion()

fig = plt.figure()
ax = fig.add_subplot(111)
line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

input()
for phase in np.linspace(0, 10*np.pi, 500):
    line1.set_ydata(np.sin(x + phase))
    fig.canvas.draw()
    fig.canvas.flush_events()
'''

## my code ##

def gen_syn_error(ite):
    # basically synthetically generate error
    LENGTH = 10
    ite = ite/LENGTH
    return np.sin(ite) + np.sin(3*ite) + np.sin(3.5*ite)

plt.ion()

# added this part so that it is initially scaled to that size and nthing more
x = [0,100]
y = [-3,3]

fig = plt.figure()
ax = fig.add_subplot(111)
l1, =  ax.plot(x, y, 'r-')

x = [0]
y = [0]

for i in range(0,100):
    time.sleep(0.1)
    x = x + [i]
    y = y + [(gen_syn_error(i))]
    l1.set_xdata(x)
    l1.set_ydata(y)
    fig.canvas.draw()
    fig.canvas.flush_events()


