#! /usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# -*- coding: gb18030 -*-
#coding=utf-8
import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import sys

i  = 0
u  = 0.0
v  = 0.0
fx = 0.0
fy = 0.0
rho= 0.0
maxu = 0.0
for line in sys.stdin:
    line = line.strip().split()
    try:
        if np.abs(np.float64(line[2]))>maxu:
            maxu = np.abs(np.float64(line[2]))
        u  += np.float64(line[2])
        v  += np.float64(line[3])
        fx += np.float64(line[4])
        fy += np.float64(line[5])
        rho+= np.float64(line[6])
        i  +=1
    except:
        pass
print "%.15f\t%.15f\t%.15f\t%.15f\t%d"%(u/np.float64(i),maxu,fx,fy,i)