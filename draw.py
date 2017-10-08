#! /usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# -*- coding: gb18030 -*-


#--------------------------------------------------#
#     Author:guchao
#     mail  :guchaonemo@163.com
#     time  :2016.10.27 15:00
#     USAEG :draw data
#--------------------------------------------------#


import matplotlib.pyplot as plt
import sys
import numpy as np
from matplotlib.pyplot import savefig
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter
import matplotlib.ticker as ticker

reload(sys)
sys.setdefaultencoding("utf-8")

def setupfunc(ax):
    xticks = ax.get_xticks()
    xticks = np.arange(0, 6, 1)
    yticks = ax.get_yticks()
    yticks = np.arange(-0.01, 0.13, 0.02)
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
    ax.yaxis.set_label_coords(-0.05, 0.5)
    majorLocator = MultipleLocator(2.5)
    minorLocator = MultipleLocator(0.5)
    ymajorLocator = MultipleLocator(0.06)
    yminorLocator = MultipleLocator(0.01)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.xaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    ax.yaxis.set_major_locator(ymajorLocator)
    majors = ["0", "", "5", "", "10"]
    ymajors = ["0", "", "0.12", "", ""]
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(majors))
    ax.yaxis.set_major_formatter(ticker.FixedFormatter(ymajors))
    ax.yaxis.set_label_coords(-0.03, 0.35)
    ax.xaxis.set_label_coords(0.5, -0.03)


def drawdata(a, b):
    font = {'fontname': 'Arial', 'weight': 'bold', 'size': 15}
    #plt.plot(a, b, 'ks', label=r'$F^1_2 {\alpha}^2$', markersize=7, linewidth=2.0)
    plt.plot(a, b, 'ks', label=r'LBE', markersize=7, linewidth=2.0)
    b0, b1= np.polyfit(a, b, 1)
    Fit = b0 * a + b1  # **2 + b1* self.Re[i:]+c1
    #plt.plot(a, Fit, '-k', label=r'$\frac{0.0036192}{(\ln \alpha)^2}-\frac{0.033475}{{\ln \alpha}}-0.010048$', linewidth=2.0)
    plt.plot(a, Fit, '-k', label=r'least square', linewidth=2.0)
    plt.xlabel(r'$-{(\ln \alpha)}^{-1}$', font, fontsize=20)
    plt.ylabel(r'$F_2 {\alpha}$', font, fontsize=20)
    plt.legend(frameon=False, numpoints=1, loc=9,fontsize=20)
    ax = plt.gca()
    setupfunc(ax)
    plt.tick_params(axis='x', which='major', length=5, width=2)
    plt.tick_params(axis='x', which='minor', length=3)
    plt.tick_params(axis='y', which='major', length=5, width=2)
    plt.tick_params(axis='y', which='minor', length=3)
    savefig(r'5-4permeability.eps', bbox_inches='tight')
    plt.show()

if __name__ == "__main__":
    a = [[0.9025, 0.116350],
         [0.81, 0.061074],
         [0.5625, 0.032327],
         [0.49, 0.029845],
         [0.25, 0.031062],
         [0.16, 0.038402],
         [0.09, 0.063248]]
    a = np.array(a)
    alpha = a[:, 0]
    F = a[:, 1]
    Falpha = F*alpha
    b = -1.0/np.log(alpha)
    drawdata(b, Falpha)

    '''c = np.array([0.09, 0.16, 0.25, 0.49, 0.5625, 0.81])
    ka1 = np.array([0.61864, 0.38816, 0.23699, 0.17779, 0.19096, 0.35096])
    Falpha = c**2.0*ka1
    b = -1.0/np.log(c)
    drawdata(b, Falpha)'''
