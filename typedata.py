#! /usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# -*- coding: gb18030 -*-


#--------------------------------------------------#
#     Author:guchao
#     mail  :guchaonemo@163.com
#     time  :2016.10.27 15:00
#     USAEG :deal with data set
#--------------------------------------------------#


import matplotlib.pyplot as plt
import sys
import numpy as np
import dataset

reload(sys)
sys.setdefaultencoding("utf-8")


def predealdata(intds=None, pos=2):
    retdata = []
    for line in sys.stdin:
        try:
            line = line.strip()
            line = line.split()
            if intds == line[pos]:
                result = [np.float64(a) for a in line]
                retdata.append(result)
        except:
            pass
    retdata.sort(key=lambda x: x[3])
    retdata = np.array(retdata)
    return retdata

if __name__ == "__main__":
    intds = "0.25"
    retdata = predealdata(intds=intds)
    baseforce = {"0.1": 20.9268068822, "0.15": 30.6628660176, "0.2": 44.3942728406, "0.25": 65.6112474869,
                 "0.3": 98.5776242932, "0.35": 168.837969375, "0.4": 353.994854353, "0.45": 1256.98349229}
    dataobj = dataset.DataSet(retdata[:, [-1, 7]], baseforce[intds])
    dataobj.quadraticpolyfit('2_'+intds+'eps')
