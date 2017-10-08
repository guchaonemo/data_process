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
import pandas as pd
#from scipy.linalg.misc import norm
from matplotlib.pyplot import savefig
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter
import matplotlib.ticker as ticker


def setupfunc(ax):
    xticks = ax.get_xticks()
    xticks = np.arange(0.0, 2.6, 0.1)
    yticks = ax.get_yticks()
    yticks = np.arange(0, 4.1, 0.1)
    ax.set_yticks(yticks)
    ytickslabel = ['%.1f' % ele for ele in yticks]
    ytickslabel = [ytickslabel[i] if (i %
                                      11 == 0 or i == 1) and i != 0 else '' for i in range(len(ytickslabel))]
    ax.set_yticklabels(ytickslabel)
    ax.set_xticks(xticks)
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(16)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(16)
    majorLocator = MultipleLocator(0.5)
    minorLocator = MultipleLocator(0.1)
    ymajorLocator = MultipleLocator(1.0)
    yminorLocator = MultipleLocator(0.2)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.xaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    ax.yaxis.set_major_locator(ymajorLocator)
    majors = ["0", "", "1", "", ""]
    ymajors = ["0", "", "2", "", ""]
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(majors))
    ax.yaxis.set_major_formatter(ticker.FixedFormatter(ymajors))
    ax.yaxis.set_label_coords(-0.03, 0.4)


def getflux(Filename):
    result = pd.read_table(
        Filename, skiprows=3, names=['1', '2', '3', '4', '5', '6', '7'], sep='  ')
    xmax = (result['2'].values).max()
    xflux = result[result['1'] > (xmax-1e-10)]
    yflux = result[result['2'] > (xmax-1e-10)]
    u_x = sum(xflux['3'].values)
    v_x = sum(xflux['4'].values)
    u_y = sum(yflux['3'].values)
    v_y = sum(yflux['4'].values)
    return u_x, v_x, u_y, v_y


def predealdata(intds):
    datadict = {}
    istar = 0.0
    iend = 200.0
    keyStr = '0.'+intds+'_'
    for line in sys.stdin:
        try:
            line = line.strip()
            line = line.split()
            result = [np.float64(a) for a in line]
            # cat ds and angle into
            dsangle = line[0]+'_'+line[2]
            if dsangle not in datadict:
                datadict[dsangle] = []
            datadict[dsangle].append(result)
        except:
            pass
    for each in datadict:
        datadict[each].sort(key=lambda x: x[1])
        datadict[each] = np.array(datadict[each])
    for each in datadict:
        if keyStr not in each:
            continue
        if istar < np.min(datadict[each][:, 1]):
            istar = np.min(datadict[each][:, 1])
        if iend > np.max(datadict[each][:, 1]):
            iend = np.max(datadict[each][:, 1])
    return datadict, [istar, iend]


def anglewith(data, angle):
    data = np.array(data)
    Re = data[:, 0]
    u = data[:, 1]
    v = data[:, 2]
    # print v
    if angle > 0.001:
        Points = angle*np.pi*v/(u*np.tan(angle*np.pi))
    else:
        Points = angle*np.pi*v/u
    realsult = np.pi*angle*np.ones([1, len(u)])[0]
    plt.plot(Re, Points, 's')
    plt.plot(Re, realsult, '-k')
    plt.ylim(0.0*angle*np.pi, 2.1*angle*np.pi+0.0001)
    plt.show()
    plt.close('all')


class DataSet(object):

    def __init__(self, data, basedata):
        data = np.array(data)
        self.x = data[:, 0]
        self.y = data[:, 1]-basedata
        self.quaindex = (np.where(self.x < 2.5))[0]
        self.qre = np.linspace(0.05, np.max(self.x[self.quaindex]), 22)
        self.linindex = (
            np.where(np.logical_and(self.x > 5.5, self.x < 35.0)))[0]

    def quadraticpolyfit(self, jpgname):
        self.k2 = (
            np.polyfit(self.x[self.quaindex]**2.0, self.y[self.quaindex], 1))
        plt.plot(self.x[self.quaindex], self.y[
                 self.quaindex], 'ks', label='LBE')
        P_poly = np.poly1d(self.k2)
        #plt.plot(self.x[self.quaindex], P_poly(    self.x[self.quaindex]**2.0), '-k', label='least square')
        plt.plot(self.qre, P_poly(
            self.qre**2.0), '-k', label='least square')
        plt.xlabel('$Re$', fontsize=20)
        plt.ylabel(r'${F_i}/{\mu U}$', fontsize=25)
        plt.legend(frameon=False, numpoints=1, loc=9)
        #plt.show()
        ax = plt.gca()
        setupfunc(ax)
        plt.tick_params(axis='x', which='major', length=5, width=2)
        plt.tick_params(axis='x', which='minor', length=3)
        plt.tick_params(axis='y', which='major', length=5, width=2)
        plt.tick_params(axis='y', which='minor', length=3)
        savefig(jpgname+'2.eps', bbox_inches='tight')
        plt.close("all")

    def linearpolyfit(self, jpgname):
        self.k1 = (
            np.polyfit(self.x[self.linindex], self.y[self.linindex], 1))
        plt.plot(self.x[self.linindex], self.y[
                 self.linindex], 'ks', label='LBE')
        plt.plot(self.x[self.linindex], np.polyval(
            self.k1, self.x[self.linindex]), '-k', label='least square')
        plt.xlabel(r'$Re$', fontsize=20)
        plt.ylabel(r'${F_i}/{\mu U}$', fontsize=25)
        plt.legend(frameon=False, numpoints=1, loc=9)
        ax = plt.gca()
        setupfunc(ax)
        plt.tick_params(axis='x', which='major', length=5, width=2)
        plt.tick_params(axis='x', which='minor', length=3)
        plt.tick_params(axis='y', which='major', length=5, width=2)
        plt.tick_params(axis='y', which='minor', length=3)
        savefig(jpgname+'.eps', bbox_inches='tight')
        plt.close('all')


class Pade(object):

    def __init__(self, data, basedata):
        data = np.array(data)
        self.x = data[:, 0]
        self.y = data[:, 1]-basedata
        self.size = len(self.x)

    def creatematrix(self, P, Q, Re):
        matrixcol = P+Q+1
        matrixrow = self.size
        self.matrix = np.zeros([matrixrow, matrixcol])
        for i in xrange(P+1):
            self.matrix[:, i] = self.x**i
        for i in xrange(Q):
            self.matrix[:, P+1+i] = -self.x**(i+1)*self.y
        self.matrix = np.matrix(self.matrix)
        B = self.matrix.T*(np.matrix(self.y)).T
        self.matrix = self.matrix.T*self.matrix
        A = self.matrix.I*B
        P_poly = np.array(A[:P+1, 0])
        Q_poly = np.array(A[P+1:, 0])
        Q_poly = [a[0] for a in Q_poly]
        P_poly = [a[0] for a in P_poly]
        P_poly.reverse()
        Q_poly.reverse()
        Q_poly.append(1.0)
        P_poly = np.poly1d(P_poly)
        Q_poly = np.poly1d(Q_poly)
        # print P_poly, Q_poly

        font = {'fontname': 'Arial', 'weight': 'bold', 'size': 15}
        plt.plot(self.x, self.y, 's', label='Drag Force',
                 markersize=7, linewidth=2.0)
        plt.plot(self.x, P_poly(self.x)/Q_poly(self.x), '-k',
                 label='Pade approximation', markersize=7, linewidth=2.0)
        plt.xlabel(r'$Re$', font, fontsize=16)
        plt.ylabel(r'${F}/{\mu U}$', font, fontsize=16)
        #plt.title('Normalized permeability of the flow through squares')
        plt.legend(frameon=False, numpoints=1, loc=9)
        plt.show()
        plt.close('all')
        return P_poly(Re)/Q_poly(Re)


if __name__ == "__main__":
    intds = '9'
    datadict, interval = predealdata(intds)
    Re = np.linspace(interval[0], interval[1], 21)
    InterResult = np.linspace(0.0, 0.0, 21)
    #c = [0.09, 0.16, 0.25, 0.49, 0.5625, 0.81]
    #ka1 = [0.61864, 0.38816, 0.23699, 0.17779, 0.19096, 0.35096]
    #ka2 = np.array([0.063248, 0.038402, 0.031062, 0.029845, 0.03232, 0.061074])
    #test = np.array([c, ka1])
    #Padeobj = Pade(test.T, 0.0)
    # print test.T
    #Padeobj.creatematrix(2, 1)
    draw_data = {}
    Omega = {'0.0': 19.0/288.0, '0.05': 25.0/96.0, '0.1': 25.0/144.0,
             '0.15': 25.0/144.0, '0.2': 25.0/96.0, '0.25': 19.0/288.0}
    symbols = {'0.0': 'k*', '0.05': 'ks', '0.1': 'ko',
               '0.15': 'kd', '0.2': 'kv', '0.25': 'k+'}
    labels = {'0.0': '$0$', '0.05': '$0.05\pi$', '0.1': '$0.1\pi$',
              '0.15': '$0.15\pi$', '0.2': '$0.2\pi$', '0.25': '$0.25\pi$'}
    for each in datadict:
        # print each
        if '0.%s_' % intds in each:
            basedict = {"ds_0.9": 2204.81617352, "ds_0.1": 8.46929442547, "ds_0.5": 57.626921003,
                        "ds_0.3": 22.6845780132, "ds_0.7": 204.056566794, "ds_0.75":  302.089494014, 'ds_0.4': 35.8786957376, "ds_0.71": 40.2274660178}
            sumKey = each.split('_')[1]
            #angle = np.float64(each.split('_')[1])
            #anglewith(datadict[each][:, [1, 7, 8]], angle)
            dataobj = DataSet(
                datadict[each][:, [1, 4]], basedict["ds_0.%s" % intds])
            Padeobj = Pade(
                datadict[each][:, [1, 4]], basedict["ds_0.%s" % intds])
            InterResult = InterResult + \
                Omega[sumKey]*Padeobj.creatematrix(4, 3, Re)
            #dataobj.quadraticpolyfit('1_'+each)
            dataobj.linearpolyfit('1_'+each)
            if each.split('_')[1] not in draw_data:
                draw_data[each.split('_')[1]] = datadict[each][:, [1, 4]]
    draw_data = sorted(
        draw_data.iteritems(), key=lambda d: float(d[0]), reverse=True)
    #draw_data = dict(draw_data)
    plt.plot(Re, 0.25*np.pi*InterResult, '-ok')
    plt.xlabel('Re')
    plt.ylabel(r'$\int \frac{F_i}{\mu U}$', fontsize=16)
    plt.title('The integration of the drag -- d = 0.%s' % intds)
    plt.show()
    plt.close('all')
    for each in draw_data:
        try:
            plt.plot(each[1][:, 0], each[1][
                     :, 1]-basedict["ds_0.%s" % intds], symbols[each[0]], label=labels[each[0]])
        except:
            pass
    InterResult = 0.25*np.pi*InterResult
    plt.plot(Re, InterResult, '-k', label='inter')
    plt.legend(frameon=False, numpoints=1, loc='upper right')
    plt.xlabel('Re')
    plt.ylabel(r'$\frac{F_i}{\mu U}$', fontsize=16)
    savefig('ds0%s.eps' % intds, dpi=600)
    plt.show()
    Re = (1.0-float('0.%s' % intds))*Re/float('0.%s' % intds)
    print '0.%s' % intds
    print '\t'.join([str(ele) for ele in Re])
    print '\t'.join([str(ele) for ele in InterResult])
