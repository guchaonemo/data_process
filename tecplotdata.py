#! /usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# -*- coding: gb18030 -*-


#--------------------------------------------------#
#     Author:guchao
#     mail  :guchaonemo@163.com
#     time  :2016.10.27 15:00
#     USAEG :deal with data tecplot
#--------------------------------------------------#


import sys
import os
import numpy as np
import pandas as pd
import warnings
warnings.filterwarnings("ignore")

reload(sys)
sys.setdefaultencoding("utf-8")


def getargument(casefolder):
    Grid = float(casefolder.split("_")[5])
    mu = float(casefolder.split("_")[1])
    d_s = 1.0-2.0 * \
        float(casefolder.split("_")[7])/float(casefolder.split("_")[8])
    Fg = float(casefolder.split("_")[3])
    Angle = float(casefolder.split("_")[6])
    return [Grid, mu, d_s, Fg, Angle]


def getdirfolders(Path):
    Folder = os.walk(Path)
    Folders = []
    for eachfolder in Folder:
        temp = (eachfolder[0].split('\\'))[-1]
        if 'Niu' in temp:
            Folders.append(eachfolder[0])
    return Folders

#------------------------------------------------------------------------------
#     tecplotdata： 处理 dat 文件类
#
#------------------------------------------------------------------------------


class tecplotdata(object):

    def __init__(self, FileName):
        self.FileName = FileName
        self.Vorfilename = FileName.split(os.path.sep)[:-1]
        self.Vorfilename.append('vorti.dat')
        self.Vorfilename = os.path.sep.join(self.Vorfilename)

    def getflux(self):
        self.result = pd.read_table(
            self.FileName, skiprows=3, names=['1', '2', '3', '4', '5', '6', '7'], sep='  ', iterator=True)
        loop = True
        chunkSize = 100000
        chunks = []
        while loop:
            try:
                chunk = self.result.get_chunk(chunkSize)
                chunks.append(chunk)
            except StopIteration:
                loop = False
        self.result = pd.concat(chunks, ignore_index=True)
        xmax = max((self.result['2']).values)
        xflux = self.result[self.result['1'] > (xmax-1e-10)]
        yflux = self.result[self.result['2'] > (xmax-1e-10)]
        self.xflux = sum(xflux['3'].values)
        self.yflux = sum(yflux['4'].values)

    def getFxy(self):
        self.Fx = sum(self.result['5'].values)
        self.Fy = sum(self.result['6'].values)
        self.u = self.result['3'].mean()
        self.v = self.result['4'].mean()

    def getVorticity(self):
        Grid = int(np.sqrt(len(self.result['1'])))
        u = self.result['3'].values
        v = self.result['4'].values
        u = np.reshape(u, [Grid, Grid])
        v = np.reshape(v, [Grid, Grid])
        streamfunction = np.zeros([Grid, Grid])
        streamfunctionx = np.zeros([Grid, Grid])
        delta = np.float64(1.0/(Grid-2.0))
        for i in range(1, Grid):
            if i == 1:
                streamfunction[i, :] = delta*u[i, :]/2.0
            else:
                streamfunction[i, :] = streamfunction[i-2, :] - delta*(u[i-2, :] + 4.0*u[i-1, :] + u[i, :])/6.0
        for i in range(1, Grid):
            if i == 1:
                streamfunctionx[:, i] = delta*u[:, i]/2.0
            else:
                streamfunctionx[:, i] = streamfunctionx[:, i-2] - delta*(u[:, i-2] + 4.0*u[:, i-1] + u[:, i])/6.0
        indices = np.array(range(Grid))
        Vorticity = (v[(indices+1) % Grid, :]-v[(indices-1) % Grid, :])*np.float64(Grid-2.0) / 2.0 - \
            (u[:, (indices+1) % Grid]-u[:, (indices-1) % Grid]) * \
            np.float64(Grid-2.0)/2.0
        Vorticity = np.reshape(Vorticity, Grid*Grid)
        streamfunction = np.reshape(streamfunction, Grid*Grid)
        streamfunctionx = np.reshape(streamfunctionx, Grid*Grid)
        x = self.result['1'].values
        y = self.result['2'].values
        L = Grid*Grid
        with open(self.Vorfilename, 'w') as filewrite:
            print >>filewrite, "Title=\"Porous Media Flow\""
            print >>filewrite, "VARIABLLES=\"X\",\"Y\",\"U\",\"V\",\"fx\",\"fy\""
            print >>filewrite, "ZONE T=\"BOX\",I=%s,J=%s,F=POINT" % (
                Grid, Grid)
            for i in xrange(L):
                print >>filewrite, "%.14lf %.14lf %.14lf %.14lf %.14lf" % (
                    x[i], y[i], Vorticity[i], streamfunction[i], streamfunctionx[i])


#------------------------------------------------------------------------------
#
#       casefolder : 文件的相对路径名  Folders ：所有包含dat文件的路径
#       dataPath :   dat 文件全路径
#------------------------------------------------------------------------------
if __name__ == "__main__":
    FilePath = raw_input("Please input the path of the files:")
    PathSep = os.path.sep
    result = []
    if "Niu" in FilePath:
        casefolder = FilePath.split(PathSep)[-1]
        dataPath = os.path.join(FilePath, 'force.dat')
        tec = tecplotdata(dataPath)
        tec.getflux()
        tec.getFxy()
        tec.getVorticity()
        eledata = getargument(casefolder)
        eledata.extend([tec.xflux, tec.yflux, tec.Fx, tec.Fy, tec.u, tec.v])
        result.append(eledata)
    else:
        Folders = getdirfolders(FilePath)
        for folder in Folders:
            casefolder = folder.split(PathSep)[-1]
            dataPath = os.path.join(folder, 'force.dat')
            tec = tecplotdata(dataPath)
            tec.getflux()
            tec.getFxy()
            tec.getVorticity()
            eledata = getargument(casefolder)
            eledata.extend(
                [tec.xflux, tec.yflux, tec.Fx, tec.Fy, tec.u, tec.v])
            result.append(eledata)
    result.sort(key=lambda x: x[3])
    for each in result:
        print '\t'.join([str(a) for a in each])
