#! /usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# -*- coding: gb18030 -*-


#--------------------------------------------------#
#     Author:guchao
#     mail  :guchaonemo@163.com
#     time  :2016.10.27 15:00
#     USAEG :Interpolate value
#--------------------------------------------------#

import os
import sys
import numpy as np
import pandas as pd
import matplotlib
from scipy import interpolate
import scipy
import matplotlib.pyplot as plt
from itertools import izip

def gravityfrommach(mach,ds,mu):
    u = mach/np.sqrt(3.0)
    gravity = u*12.0*mu/((1.0-ds)**2)
    return gravity

def datainterp(datapath,intersize,p,npoints):
    dataname = datapath+"\\force.dat"
    mainpath = '\\'.join(datapath.split('\\')[0:-1])
    gridPath = (list(filter(None,datapath.split('\\')))[-1])
    number   = np.log2(intersize/(int(gridPath.split('_')[4])-2))
    interdataname = datapath+"\\interforce%s.dat"%(int(number))
    #read the file 
    gridlines=(int(gridPath.split('_')[4]))**2
    x = np.zeros(gridlines)
    y = np.zeros(gridlines)
    u = np.zeros(gridlines)
    v = np.zeros(gridlines)
    fileread = open(dataname,'r')
    nlines = 0
    for line in fileread:
        line = line.strip().split()
        try:
            u[nlines]= np.float64(line[2])
            v[nlines]= np.float64(line[3])
            x[nlines]= np.float64(line[0])
            y[nlines]= np.float64(line[1])
            nlines+=1
        except:
            pass
    fileread.close()
    if (nlines)!=gridlines:
        print nlines,gridlines
        print "error for result of the lines data"
        return 0
    tree  =scipy.spatial.cKDTree(zip(x,y))
    xnew  = np.linspace(0.0,np.float64(1.0),intersize+1.0)
    intersize = (intersize+1)**2
    xx,yy = np.meshgrid(xnew,xnew)
    xx    = (xx.T).reshape(intersize)
    yy    = (yy.T).reshape(intersize)
    unew  = np.zeros(intersize)
    vnew  = np.zeros(intersize)
    for i in xrange(intersize):
        dis,inds = tree.query((xx[i],yy[i]),k=npoints)
        if dis[0]<1.0e-10:
            unew[i] = u[inds[0]]
            vnew[i] = v[inds[0]]
            continue
        else:
            dis = 1.0/dis**p
            for j in xrange(npoints):
                try:
                    unew[i]+=dis[j]*np.float64(u[inds[j]])
                    vnew[i]+=dis[j]*np.float64(v[inds[j]])
                    if np.isnan(np.float64(u[inds[j]])):
                        print "Error in this file,the value should be data"
                        return 1
                except:
                    print u[inds[j]],type(u[inds[j]])
            unew[i]=unew[i]/sum(dis)
            vnew[i]=vnew[i]/sum(dis)
            if np.isnan(unew[i]):
                print sum(dis),unew[i]
                return 2
    with open(interdataname,'w') as filepointer:
        for i in xrange(intersize):
            print >>filepointer,'%.15f\t%.15f\t%.15f\t%.15f'%(xx[i],yy[i],unew[i],vnew[i])
    return 0

def listPath(fatherPath):
    result = []
    for subPath,subsubPath,files in os.walk(fatherPath):
        result.append(subPath)
    return result

def maininter(interPaths):
        interPaths = listPath(interPaths)
        Grid = 0
        for subPath in interPaths:
                if 'Niu' in subPath:
                        gridPath = (list(filter(None,subPath.split('\\')))[-1])
                        Grid=max((int(gridPath.split('_')[4]))-2,Grid)
        for subPath in interPaths:
            try:
                datainterp(subPath,int(Grid),2,8)
            except:
                print subPath,Grid
        return 0

def machmain(grid,mach):
    ds = np.linspace(0.1,.9,9)
    mu = 0.01
    result = gravityfrommach(mach,ds,mu)
    gap    = 10.0-np.linspace(1,9,9)
    print '#!/bin/bash'
    for i in xrange(9):
        output = ['./trtNoLinear_10',str(grid),str(grid),str(int(gap[i])),str(20),'0',str(("%.14f" %result[i])),str(mu),'1','2',str(ds[i])]
        print '\t'.join(output)
    return 0

def main(Path):
    for i in xrange(1,10):
        maininter(Path+str(i))
        print convergenceorder(Path+str(i),514),str(i)
    return 0

def convergenceorder(filepath,grids):
    lines = grids**2
    i = 0
    fileread3 = open(filepath+'\\interforce3.dat')
    fileread2 = open(filepath+'\\interforce2.dat')
    fileread1 = open(filepath+'\\interforce1.dat')
    fileread0 = open(filepath+'\\interforce0.dat')
    u0 = 0.0
    u1 = 0.0
    u2 = 0.0
    u3 = 0.0
    for line0,line1,line2,line3 in izip(fileread0,fileread1,fileread2,fileread3):
        try:
            line0 = line0.strip().split()
            line1 = line1.strip().split()
            line2 = line2.strip().split()
            line3 = line3.strip().split()
            i+=1
            u0 +=np.sqrt(np.float64(line0[3])**2+np.float64(line0[2])**2)
            u1 +=np.sqrt( (np.float64(line0[3])-np.float64(line1[3]))**2 +(np.float64(line0[2])-np.float64(line1[2]))**2  )
            u2 +=np.sqrt( (np.float64(line0[3])-np.float64(line2[3]))**2 +(np.float64(line0[2])-np.float64(line2[2]))**2  )
            u3 +=np.sqrt( (np.float64(line0[3])-np.float64(line3[3]))**2 +(np.float64(line0[2])-np.float64(line3[2]))**2  )
        except:
            print "error in this function"
            sys.exit(1)
    fileread0.close()
    fileread1.close()
    fileread2.close()
    fileread3.close()
    err = np.array([u3/u0,u2/u0,u1/u0])
    h   = np.array([1.0/64.0,1.0/128.0,1.0/256.0])
    print err
    err = np.log10(err)
    h   = np.log10(h)
    x   = np.linspace(min(h),max(h),20)
    y   = 2*(x-min(h)) + u3/u0
    #fig, ax = plt.subplots()
    #ax.plot(h,err,'-o')
    #ax.plot(x,y,'k-')
    #plt.show()
    return np.polyfit(h,err,1)

if __name__ == '__main__':
    a = r'D:\datapaper\blocktrt\NoLinear\volume\mach\0.02\20to'
    main(a)
