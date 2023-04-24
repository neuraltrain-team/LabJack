# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:32:46 2023

@author: neuraltrainlab
"""

# 01. Get the packages
import matplotlib.pyplot as plt
import numpy as np
import u3

# 02. Set the stream parameters
n_trials = 1 # how many data blocks should be collected
max_requests = 50
scan_frequency = 5000 # sample frequency
samp_rate = 1/scan_frequency # sample rate

# 03. Set up LabJack
d = None # clear object
d = u3.U3() # open Labjack object
d.getCalibrationData() # calibrate labjack
d.configIO(FIOAnalog = 3) # Set the channels to analog
d.streamConfig(NumChannels=1, 
               PChannels=[0], 
               NChannels=[31], 
               Resolution=3, 
               ScanFrequency=scan_frequency) # cofigure the stream
 
# 04. Start the stream
AIN0 = list() # empty container for the data

## Loop for trials
for t in range(n_trials):
    # 03. Start the stream
    d.streamStart()
    
    r = None # empty stream
    dataCount = 0 # reset data counter
    
    for r in d.streamData(): # loop through stream data
        if r is not None:
            if dataCount >= max_requests:
                break
            
            dataCount += 1
    
    d.streamStop() # stop the stream
    
    tmp = r["AIN0"] # Collect the analog data for this trial
    AIN0 = AIN0+tmp # concatenate with the previous trials
## Close connection    
d.close()

# 05. Some Plots
timevec = np.arange(0,len(AIN0)*samp_rate,samp_rate)
plt.plot(timevec,AIN0)

# 04. Compute the FFT
from scipy.signal import hamming
from scipy.fft import fft, fftfreq

N = len(AIN0) # How many items
T = samp_rate # Sample interval
w = hamming(N) # Window Function
ywf = fft(AIN0*w) # Windowed FFT

xfreq = fftfreq(N,T)[:N//2] # Extract the Frequency
yval = 2.0/N*np.abs(ywf[:N//2]) # Extract the power values

uplim = np.argmin(np.abs(xfreq-200))

plt.plot(xfreq[:uplim],yval[:uplim]) # Aaaaand finally plot the FFT

