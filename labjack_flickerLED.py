# -*- coding: utf-8 -*-
"""
Created on Wed Apr 26 15:37:18 2023

@author: neuraltrainlab
"""

# 01. Get the packages
import u3
import time

# 02. Set the flicker parameters


# 03. Set up LabJack
d = None # clear object
d = u3.U3() # open Labjack object
d.getCalibrationData() # calibrate labjack


for i in range(31):
    print(i)
    d.getFeedback(u3.BitStateWrite(IONumber = 0, State = 1))
    time.sleep(.005)
    d.getFeedback(u3.BitStateWrite(IONumber = 0, State = 0))
    time.sleep(.005)

