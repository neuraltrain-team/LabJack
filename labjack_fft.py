# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 09:46:14 2023

@author: neuraltrainlab
"""

# 01. Set the required packes
from scipy.fft import fft, fftfreq
import numpy as np
import matplotlib.pyplot as plt
import os

# 02. set the working directors
os.chdir('C:\\Users\\neuraltrainlab\\Documents\\Labjack\\Data\\')
datafile = 'example_0.dat'

# 03. get the data
with open(datafile) as f:
    lines = f.readlines() # Read Text
    
raw = lines[7:] # Remove Header
x = [i.split('\t')[0] for i in raw] # Time
xf = [float(i) for i in x]
y = [i.split('\t')[1] for i in raw] # Data
yf = [float(i) for i in y]

plt.plot(xf[1:1000],yf[1:1000])

# 04. Compute the FFT
from scipy.signal import hamming
N = len(xf) # How many items
T = xf[1]-xf[0] # Sample interval
w = hamming(N) # Window Function
ywf = fft(yf*w) # Windowed FFT

xfreq = fftfreq(N,T)[:N//2] # Extract the Frequency
yval = 2.0/N*np.abs(ywf[:N//2]) # Extract the power values

uplim = np.where(xfreq == 200) # Set the upper limits for the plot
uplim = float(uplim[0]) # Again
uplim = int(uplim) # And finally have a number we can use for the plot

plt.plot(xfreq[:uplim],yval[:uplim]) # Aaaaand finally plot the FFT
