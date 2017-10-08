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
import os
import sys
import ctypes
import numpy as np
#from scipy.linalg.misc import norm
from numpy.linalg import norm
from matplotlib.pyplot import plot
from matplotlib.pyplot import savefig
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter


def drawdata(a, b):
    font = {'fontname': 'Arial', 'weight': 'bold', 'size': 15}
    plt.semilogy(
        1.0-a[:, 0]**2, a[:, 1], '-ks', label='FEM', markersize=7, linewidth=2.0)
    plt.semilogy(1.0-b[:, 0]**2, b[:, 1], '--ko', label='LBE', linewidth=2.0)
    plt.minorticks_off()
    plt.xlabel(r'$\varepsilon$',
               font, fontsize=20)
    #plt.ylabel(r'$\frac{K}{L^{2}_p}$', font, fontsize=20)
    plt.ylabel(r'${K}^{\ast}$', font, fontsize=20)
    plt.legend(frameon=False, numpoints=1, loc=1)
    #plt.show()
    ax = plt.gca()
    xticks = ax.get_xticks()
    xticks = np.linspace(min(xticks), max(xticks), 11)
    xtickslabel = ['%.1f' % a for a in xticks]
    xtickslabel = [xtickslabel[i] if i %
                   10 == 0 else '' for i in range(len(xtickslabel))]
    yticks = ax.get_yticks()
    yticks = np.linspace(np.log10(min(yticks)), np.log10(max(yticks)), 8)
    yticks = np.power(10.0, yticks)
    ax.set_yticks(yticks)
    ytickslabel = ['%.1E' % ele for ele in yticks]
    ytickslabel = [ytickslabel[i] if (i %
                                      6 == 0 or i == 1) and i != 0 else '' for i in range(len(ytickslabel))]
    ax.set_yticklabels(ytickslabel)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xtickslabel)
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(16)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(16)
    # ax.spines['top'].set_visible(False)
    # ax.spines['right'].set_visible(False)
    #plt.tick_params(top='off',  right='off')
    ax.yaxis.set_label_coords(-0.05, 0.5)
    savefig(r'4-1permeability.eps', bbox_inches='tight')
    plt.show()
# 边去掉


def fitsangani(data):
    font = {'fontname': 'Arial', 'weight': 'bold', 'size': 15}
    data = np.array(data)
    ds = data[0:, 0]
    F = data[0:, 2]
    ds = ds[10:]
    F = F[10:]
    alpha = ds**2.0
    B = np.matrix(F - alpha + 0.5*np.log(alpha))
    B = B.T
    A = np.array([alpha**0.0, alpha**2.0, alpha**3.0])
    A = np.matrix(A)
    A = A.T
    B = A.T*B
    A = A.T*A
    coffi = np.array(A.I*B)
    coffi = coffi[:, 0]
    ds = data[:, 0]
    F = data[:, 2]
    alpha = ds**2.0
    x = np.linspace(min(alpha), max(alpha), 101)
    Fitresult = -0.5 * \
        np.log(x)+coffi[0] + x+coffi[1]*x**2++coffi[2]*x**3
    Fitresult = lambda x:-0.5 * \
        np.log(x)+coffi[0] + x+coffi[1]*x**2++coffi[2]*x**3
    plt.plot(x, Fitresult(x), '-k',
             label='Sangani model', markersize=7, linewidth=2.0)
    plt.plot(alpha, F, 'ks', label='LBE', linewidth=2.0)
    plt.xlabel(r'$\alpha$', font, fontsize=20)
    plt.ylabel(r'${4\pi\mu U}/{F}$', font, fontsize=20)
    '''
    estimate error
    '''
    delta = norm(F-Fitresult(alpha))/3.0**0.5
    A=A.I
    plt.minorticks_off()
    plt.ylim([-0.1, 1.6])
    plt.legend(frameon=False, numpoints=1, loc=1)
    ax = plt.gca()
    xticks = ax.get_xticks()
    xticks = np.linspace(min(xticks), max(xticks), 11)
    xtickslabel = ['%.1f' % a for a in xticks]
    xtickslabel = [xtickslabel[i] if i %
                   10 == 0 else '' for i in range(len(xtickslabel))]
    majorLocator = MultipleLocator(0.5)
    minorLocator = MultipleLocator(0.1)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.xaxis.set_major_locator(majorLocator)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xtickslabel)
    ax.tick_params(axis='x', which='major', width=2)
    yticks = ax.get_yticks()
    yticks = np.linspace(-0.1, (max(yticks)), 18)
    ax.set_yticks(yticks)
    ytickslabel = ['%.1f' % ele for ele in yticks]
    ytickslabel = [ytickslabel[i] if (i %
                                      11 == 0 or i == 1) and i != 0 else '' for i in range(len(ytickslabel))]
    ax.set_yticklabels(ytickslabel)
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(16)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(16)
    ax.yaxis.set_label_coords(-0.05, 0.5)
    # ax.spines['top'].set_visible(False)
    # ax.spines['right'].set_visible(False)
    #plt.tick_params(top='off',  right='off')
    savefig(r'4-2Sangani.eps', bbox_inches='tight')
    plt.show()
    return coffi
# 一幅虚线，实线，标记相同

def fitsangani1(data):
    font = {'fontname': 'Arial', 'weight': 'bold', 'size': 15}
    data = np.array(data)
    ds = data[0:, 0]
    F = data[0:, 2]
    alpha = ds**2.0
    B = np.matrix(F + 0.5*np.log(alpha))
    B = B.T
    A = np.array([alpha**0.0,alpha, alpha**2.0, alpha**3.0])
    A = np.matrix(A)
    A = A.T
    B = A.T*B
    A = A.T*A
    coffi = np.array(A.I*B)
    coffi = coffi[:, 0]
    ds = data[:, 0]
    F = data[:, 2]
    alpha = ds**2.0
    x = np.linspace(min(alpha), max(alpha), 101)
    Fitresult = -0.5 * \
        np.log(x)+coffi[0] + coffi[1]*x+coffi[2]*x**2++coffi[3]*x**3
    Fitresult = lambda x:-0.5 * \
        np.log(x)+coffi[0] + coffi[1]*x+coffi[2]*x**2++coffi[3]*x**3
    plt.plot(x, Fitresult(x), '-k',
             label='Sangani model', markersize=7, linewidth=2.0)
    plt.plot(alpha, F, 'ks', label='LBE', linewidth=2.0)
    plt.xlabel(r'$\alpha$', font, fontsize=20)
    plt.ylabel(r'${4\pi\mu U}/{F}$', font, fontsize=20)
    '''
    estimate error
    '''
    delta = norm(F-Fitresult(alpha))/4.0**0.5
    A=A.I
    print delta*A[0,0],delta*A[1,1],delta*A[2,2], delta*A[3,3]
    plt.minorticks_off()
    plt.ylim([-0.1, 1.6])
    plt.legend(frameon=False, numpoints=1, loc=1)
    ax = plt.gca()
    xticks = ax.get_xticks()
    xticks = np.linspace(min(xticks), max(xticks), 11)
    xtickslabel = ['%.1f' % a for a in xticks]
    xtickslabel = [xtickslabel[i] if i %
                   10 == 0 else '' for i in range(len(xtickslabel))]
    majorLocator = MultipleLocator(0.5)
    minorLocator = MultipleLocator(0.1)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.xaxis.set_major_locator(majorLocator)
    ax.set_xticks(xticks)
    ax.set_xticklabels(xtickslabel)
    ax.tick_params(axis='x', which='major', width=2)
    yticks = ax.get_yticks()
    yticks = np.linspace(-0.1, (max(yticks)), 18)
    ax.set_yticks(yticks)
    ytickslabel = ['%.1f' % ele for ele in yticks]
    ytickslabel = [ytickslabel[i] if (i %
                                      11 == 0 or i == 1) and i != 0 else '' for i in range(len(ytickslabel))]
    ax.set_yticklabels(ytickslabel)
    for tick in ax.xaxis.get_major_ticks():
        tick.label1.set_fontsize(16)
    for tick in ax.yaxis.get_major_ticks():
        tick.label1.set_fontsize(16)
    ax.yaxis.set_label_coords(-0.05, 0.5)
    # ax.spines['top'].set_visible(False)
    # ax.spines['right'].set_visible(False)
    #plt.tick_params(top='off',  right='off')
    savefig(r'4-2Sangani.eps', bbox_inches='tight')
    plt.show()
    return coffi


def relativeerr(x, y):
    x = np.array(x)
    # porosity = 1.0 - x**
    porosity = x**2
    logy = np.log(y)
    a, b = np.polyfit(porosity, logy, 1)
    fity = a*porosity+b
    print "the porosity %.4lf  %.4lf" % (a, b)
    y1 = np.e**fity
    plt.semilogy(porosity, y1, '-rs', linewidth=2.0)
    plt.semilogy(porosity, y, '-kd', linewidth=2.0)
    plt.minorticks_off()
    plt.tick_params(top='off',  right='off')
    ax = plt.gca()
    # ax.spines['top'].set_visible(False)
    # ax.spines['right'].set_visible(False)
    print norm(np.abs(y1-y))/norm(y)
    plt.show()
a = [[0.8,   1.20391829718959e-003,   1.11696652816e-003],
     [0.7,   5.61375857355795e-003,   5.04181365052e-003],
     [0.6,   1.88203140306559e-002,   1.73921782033e-002],
     [0.5,   5.35005453492635e-002,   5.19462705377e-002],
     [0.4,   1.60683080549599e-001,   1.45774577413e-001],
     [0.3,   4.56774123099134e-001,   4.45297245925e-001],
     [0.2,   1.70936898930253e+000,   1.65527195841e+000]]
'''
b=[[0.1  ,7.57129865329  ,  2.36813372704     ],
[0.125 ,4.61121260466    ,  1.90785192358     ],
[0.150 ,3.01063725524    ,  1.55206274693     ],
[0.175 ,2.06005772736    ,  1.29109687023     ],
[0.2   ,1.43983208498    ,  1.06569495321     ],
[0.225 ,  1.05296007413  , 0.931844676932 ],
[0.250 ,  0.774551156718 , 0.80271027451  ],
[0.275 ,  0.57704637862  , 0.695838782122 ],
[0.3   ,0.432114689106   ,  0.602684840767    ],
[0.4   ,0.145501573202   ,  0.354985297045    ],
[0.5   ,0.0519293987123  ,  0.215611861954    ],
[0.55  ,0.0304133802071  ,  0.164244178002    ],
[0.6   ,0.0174130991884  ,  0.122616011079    ],
[0.65  ,0.00980027442198 ,  0.089940090975    ],
[0.7   ,0.00522128845516 ,  0.0630206412829   ],
[0.75  ,0.00257411530089 ,  0.0416526473141   ],
[0.8   ,0.00113367284086 ,  0.0253549907674   ],
[0.82  ,0.000780111750282,  0.0201438568586   ],
[0.84  ,0.000517917432905,  0.0156166852417   ],
[0.86  ,0.000328463895227,  0.0117370052134   ],
[0.88  ,0.000196134112607,  0.00847030439579  ],
[0.91  ,7.67025834503e-05,  0.00464885955356  ],
[0.92  ,5.26098951504e-05,  0.00364740300738  ],
[0.93  ,3.44654295385e-05,  0.00277606953464  ],
[0.94  ,2.12690726403e-05,  0.00203137519724  ],
[0.95  ,1.21063500642e-05,  0.00140993162099  ]]'''
b = [[0.1,  11.7441648558, 1.49173818333],
     [0.125,  6.51065199843, 1.29922139983],
     [0.15,  3.90878759607, 1.13133834817],
     [0.175,  2.49964386264, 0.993231225889],
     [0.2,  1.67314399433, 0.877058836392],
     [0.225,  1.15889416741, 0.777710669959],
     [0.25,  0.832364329622, 0.69786532059],
     [0.275,  0.604163452684, 0.621798517309],
     [0.3,  0.445682612896, 0.554694174864],
     [0.4,  0.147546209593, 0.353691942059],
     [0.5,  0.0520191221745, 0.218180900115],
     [0.55,  0.0304319621001, 0.166287038296],
     [0.6,  0.0174200731516, 0.123678834345],
     [0.65,  0.00980159630886, 0.0903299930439],
     [0.7,  0.00515674387452, 0.0625619617843],
     [0.75,  0.00257411620978, 0.0416589172531],
     [0.8,  0.00112048832365, 0.0251628343133],
     [0.82,  0.000780942081936, 0.0201877958328],
     [0.84,  0.000518766494314, 0.0156600398339],
     [0.86,  0.000329278358742, 0.0117796434327],
     [0.88,  0.000196874985537, 0.00851219780357],
     [0.9,  0.000108478133804, 0.00582519768458],
     [0.91,  7.72848977895e-05, 0.00468969821414],
     [0.92,  5.31311348207e-05, 0.00368792388041],
     [0.93,  3.49230750452e-05, 0.00281629594935],
     [0.94,  2.16614178905e-05, 0.00207133410544],
     [0.95,  1.24324101946e-05, 0.00144965346994]]
b = [[1.00000000e-01,   1.17203986e+01,   8.36464201e+00],
     [1.25000000e-01,   6.46466808e+00,   9.69118490e+00],
     [1.50000000e-01,   3.90077045e+00,   1.11011076e+01],
     [1.75000000e-01,   2.50345549e+00,   1.26171693e+01],
     [2.00000000e-01,   1.68043609e+00,   1.42603458e+01],
     [2.25000000e-01,   1.16675762e+00,   1.60526122e+01],
     [2.50000000e-01,   8.31523179e-01,   1.80181939e+01],
     [2.75000000e-01,   6.04856914e-01,   2.01849908e+01],
     [3.00000000e-01,   4.47138363e-01,   2.25860995e+01],
     [4.00000000e-01,   1.47769035e-01,   3.54776948e+01],
     [5.00000000e-01,   5.19809417e-02,   5.76174180e+01],
     [5.50000000e-01,   3.05775946e-02,   7.52741869e+01],
     [6.00000000e-01,   1.76225361e-02,   1.00692021e+02],
     [6.50000000e-01,   9.82551850e-03,   1.38840059e+02],
     [7.00000000e-01,   5.21324501e-03,   1.99238316e+02],
     [7.50000000e-01,   2.56934626e-03,   3.02067631e+02],
     [8.00000000e-01,   1.13094081e-03,   4.96270879e+02],
     [8.20000000e-01,   7.77934240e-04,   6.24880395e+02],
     [8.40000000e-01,   5.16190742e-04,   8.06452345e+02],
     [8.60000000e-01,   3.27104876e-04,   1.07387539e+03],
     [8.80000000e-01,   1.95076637e-04,   1.48988736e+03],
     [9.00000000e-01,   1.07030174e-04,   2.18642795e+03],
     [9.10000000e-01,   7.60035270e-05,   2.72474496e+03],
     [9.20000000e-01,   5.20109435e-05,   3.48082569e+03],
     [9.30000000e-01,   3.39588925e-05,   4.58870916e+03],
     [9.40000000e-01,   2.08482845e-05,   6.30342027e+03],
     [9.50000000e-01,   1.17655785e-05,   9.15983621e+03]]
b = np.array(b)
b[:, 2] = 4.0*np.pi/b[:, 2]
# b[:,2]=b[:,2]*b[:,0]
coffi = fitsangani(b)
print coffi
a = np.array(a)
b = np.array(b)
relativeerr(b[9:21, 0], b[9:21, 1])
drawdata(a, b)
