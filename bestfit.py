#! /usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# -*- coding: gb18030 -*-


#--------------------------------------------------#
#     Author:guchao
#     mail  :guchaonemo@163.com
#     time  :2016.10.27 15:00
#     USAEG :fit line
#--------------------------------------------------#

import matplotlib.pyplot as plt
import os
import sys
import ctypes
import numpy as np
from scipy.linalg.misc import norm
from matplotlib.pyplot import plot, savefig
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter
import matplotlib.ticker as ticker



def setupfunc(ax):
    xticks = ax.get_xticks()
    xticks = np.arange(0, 40, 5)
    yticks = ax.get_yticks()
    print min(yticks), max(yticks)
    yticks = np.linspace(-0.2, (max(yticks)), 19)
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
    majorLocator = MultipleLocator(15.0)
    minorLocator = MultipleLocator(5)
    ymajorLocator = MultipleLocator(15)
    yminorLocator = MultipleLocator(5)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.xaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    ax.yaxis.set_major_locator(ymajorLocator)
    majors = ["0", "", "30", "", "4"]
    ymajors = ["0", "", "30", "", "4"]
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(majors))
    ax.yaxis.set_major_formatter(ticker.FixedFormatter(ymajors))

class Linedata(object):

    """docstring for ClassName"""

    def __init__(self, Re, F):
        self.Re = np.array(Re)
        self.F = np.array(F)
        self.F = self.F - min(F)
        self.L = len(Re)

    def bestfitline(self):
        self.font = {'fontname': 'Arial', 'weight': 'bold', 'size': 15}
        self.lineindex = 4
        L = len(self.Re)
        self.a0 = 0.0
        self.a1 = 0.0
        self.a2 = 0.0
        self.square = 1.0
        for i in xrange(self.lineindex, L+1):
            a, b, c = np.polyfit(self.Re[0:i], self.F[0:i], 2)
            Fit = a*self.Re[0:i]**2.0+b*self.Re[0:i] + c
            error = norm(np.abs(Fit-self.F[0:i]))/norm(self.F[0:i])
            plt.plot(self.Re[0:i], self.F[0:i], 'ks', label='numerical result')
            plt.plot(self.Re[0:i], Fit, '-k', label='least square fit')
            plt.xlabel(r'$Re,\alpha=0.25$', self.font)
            plt.ylabel(r'$\frac{F-F_s}{\mu U}$', self.font, fontsize=16)
            plt.legend(frameon=False, numpoints=1, loc=9)
            print error, a, b, c, self.Re[i-1], i
            savefig("%d.eps" % i)
            plt.close('all')
            if error < self.square:
                self.square = error
                self.a0 = a
                self.a1 = b
                self.a2 = c
                self.lineindex = i
                if i == 21:
                    break
        print self.square, self.a0, self.a1, self.a2, self.lineindex

    def bestfitone(self):
        self.lineindex = self.lineindex-2
        self.b0 = 0.0
        self.b1 = 0.0
        self.square = 1.0
        for i in xrange(self.lineindex, self.L-10):
            b0, b1 = np.polyfit(self.Re[i:self.L-9], self.F[i:self.L-9], 1)
            Fit = b0 * self.Re[i:self.L-9] + b1  # **2 + b1* self.Re[i:]+c1
            error = norm(Fit-self.F[i:self.L-9])/norm(self.F[i:self.L-9])
            plt.plot(self.Re[i:self.L-9], self.F[i:self.L-9],
                     'ks', label='numerical result')
            plt.plot(self.Re[i:self.L-9], Fit, 'r', label='least square')
            plt.xlabel(r'$Re,\alpha=0.25$', self.font)
            plt.ylabel(r'$\frac{F-F_s}{\mu U}$', self.font, fontsize=16)
            plt.legend(frameon=False, numpoints=1, loc=9)
            savefig("A%d.eps" % i)
            plt.close('all')
            print error, b0, b1, self.Re[i], i


def drawdata(a, b):
    font = {'fontname': 'Arial', 'weight': 'bold', 'size': 15}
    #a1, b1, c1 = np.polyfit(a, b, 2)
    #Fit = a1*a**2.0+b1*a + c1
    b1, c1 = np.polyfit(a, b, 1)
    Fit = b1*a + c1
    print b1, c1
    plt.plot(a, b, 'ks', label='LBE', markersize=7, linewidth=2.0)
    plt.plot(a, Fit, '-k', label='least square', markersize=7, linewidth=2.0)
    plt.xlabel(r'$Re$', font, fontsize=20)
    plt.ylabel(r'${F_i}/{\mu U}$', font, fontsize=25)
    plt.legend(frameon=False, numpoints=1, loc=9)
    ax = plt.gca()
    setupfunc(ax)
    plt.tick_params(axis='x', which='major', length=7, width=2)
    plt.tick_params(axis='x', which='minor', length=4)
    plt.tick_params(axis='y', which='major', length=7, width=2)
    plt.tick_params(axis='y', which='minor', length=4)
    savefig(r'5-2permeability.eps', bbox_inches='tight')
    plt.show()
if __name__ == '__main__':
    data = [[0.311509890128, 57.6328942312],
            [0.436091711549, 57.635819494],
            [0.560651504763, 57.6397093646],
            [0.685183126744, 57.6445549632],
            [0.809680545197, 57.6503453202],
            [0.934137860738, 57.6570674559],
            [1.05854932761, 57.6647064783],
            [1.18290937286, 57.6732456897],
            [1.30721261367, 57.6826667071],
            [1.43145387289, 57.6929495896],
            [1.55562819278, 57.7040729688],
            [1.86574070518, 57.7354071767],
            [2.48436528097, 57.8118417199],
            [3.10052438811, 57.9038069126],
            [3.71395476143, 58.0078682801],
            [4.32452795209, 58.1208017343],
            [4.93222175829, 58.2397708118],
            [5.53709087899, 58.3623973233],
            [6.13924136961, 58.4867590924],
            [6.73881051013, 58.6113474338],
            [7.33595193934, 58.7350081846],
            [7.93082517984, 58.8568805527],
            [8.52358854067, 58.9763408919],
            [15.2873782782, 60.1283405583],
            [21.9249924489, 60.9222244629],
            [28.4902874914, 61.5028520089],
            [35.0067399656, 61.952314365],
            [41.4872372566, 62.3146623907],
            [47.9394938009, 62.6159679454],
            [54.3684370126, 62.8727368112],
            [60.7774399195, 63.0958964399],
            [67.1689663055, 63.2929448349],
            [73.5449140222, 63.4691924662]]
    data = np.array(data)
    #a = Linedata(data[:, 0], data[:, 1]-57.6298398805)
    # a.bestfitline()
    # a.bestfitone()
    data = [[9617.57006694, 0.02372931],
            [9617.57009594, 0.02847518],
            [9617.57013019, 0.03322104],
            [9617.57016972, 0.03796690],
            [9617.57021451, 0.04271276],
            [9617.57026457, 0.04745863],
            [9617.57031991, 0.05220449],
            [9617.57038052, 0.05695035],
            [9617.57044639, 0.06169622],
            [9617.57051754, 0.06644208],
            [9617.57059395, 0.07118794],
            [9617.57067564, 0.07593380],
            [9617.57076259, 0.08067967],
            [9617.5708548, 0.08542553],
            [9617.57095231, 0.09017139],
            [9617.57105506, 0.09491725],
            [9617.57237247, 0.14237586],
            [9617.57421668, 0.18983445],
            [9617.57658755, 0.23729300],
            [9617.57948487, 0.28475152],
            [9617.5829084, 0.33220999],
            [9617.58685785, 0.37966840],
            [9617.59133288, 0.42712676],
            [9617.59633312, 0.47458504],
            [9617.60185816, 0.52204324],
            [9617.60790753, 0.56950136],
            [9617.61448071, 0.61695939],
            [9617.62157716, 0.66441731],
            [9617.62919628, 0.71187513],
            [9617.63733744, 0.75933283],
            [9617.64599995, 0.80679040],
            [9617.65518308, 0.85424785],
            [9617.66488608, 0.90170515],
            [9617.67510814, 0.94916231],
            [9617.68584839, 0.99661931],
            [9617.69710595, 1.04407615],
            [9617.70887988, 1.09153282],
            [9617.74872154, 1.23889711],
            [9617.79350091, 1.38625947],
            [9617.84318244, 1.53361967],
            [9617.89772695, 1.68097750],
            [9617.95709165, 1.82833274],
            [9618.0212303, 1.97568519],
            [9618.09009332, 2.12303462],
            [9618.1636279, 2.27038084],
            [9618.24177811, 2.41772365],
            [9618.32448506, 2.56506285],
            [9618.41168706, 2.71239825],
            [9618.50331967, 2.85972966],
            [9618.59931595, 3.00705689],
            [9618.69960659, 3.15437978],
            [9618.80411999, 3.30169815],
            [9618.9127825, 3.44901183],
            [9619.02551852, 3.59632065],
            [9619.14225069, 3.74362447],
            [9619.26290002, 3.89092313],
            [9619.30257383, 3.93835717],
            [9619.55993618, 4.23543123],
            [9619.8321206, 4.53248242],
            [9620.11843311, 4.82950970],
            [9620.41816892, 5.12651216],
            [9620.73061707, 5.42348893],
            [9621.05506473, 5.72043929],
            [9621.39080139, 6.01736256],
            [9621.73712252, 6.31425816],
            [9622.09333296, 6.61112559],
            [9622.45874993, 6.90796444],
            [9622.83270564, 7.20477435],
            [9623.21454961, 7.50155504],
            [9623.60365051, 7.79830630],
            [9623.99939782, 8.09502797],
            [9624.40120301, 8.39171996],
            [9624.80850051, 8.68838222],
            [9625.22074844, 8.98501475],
            [9625.63742895, 9.28161760],
            [9626.05804848, 9.57819085],
            [9627.28467322, 10.4303638],
            [9633.06472974, 14.3568361],
            [9635.58988275, 16.0957866],
            [9638.05001325, 17.8339463],
            [9640.43038464, 19.5713807],
            [9642.72324682, 21.3081508],
            [9644.92545251, 23.0443117],
            [9647.03683031, 24.7799132],
            [9649.05909176, 26.5150001],
            [9650.99510273, 28.2496123],
            [9652.84839975, 29.9837857],
            [9654.62287009, 31.7175522],
            [9656.32254097, 33.4509407],
            [9657.95144232, 35.1839768],
            [9659.5135187, 36.9166839],
            [9661.01257454, 38.6490828],
            [9662.45224182, 40.3811923],
            [9663.83596302, 42.1130295],
            [9665.16698407, 43.8446100],
            [9666.44835439, 45.5759476],
            [9667.68293105, 47.3070553],
            [9668.56612398, 48.5852266],
            [9671.01190237, 52.3093195],
            [9673.28449211, 56.0325324],
            [9674.36207189, 57.8938342],
            [9676.41072772, 61.6158724],
            [9678.33017292, 65.3372072],
            [9680.13392224, 69.0578916],
            [9681.83367803, 72.7779714],
            [9683.43960642, 76.4974864],
            [9684.96057004, 80.2164716],
            [9686.40432302, 83.9349580],
            [9687.77767457, 87.6529730],
            [9689.08662586, 91.3705413],
            [9692.11063841, 100.662648],
            [9692.39542536, 101.591725],
            [9692.67725588, 102.520778],
            [9692.99996616, 103.596495],
            [9693.23227052, 104.378815],
            [9693.50556237, 105.307800],
            [9693.53273996, 105.400697]]
    data = np.array(data)
    #a = Linedata(data[:, 1], data[:, 0]-9617.57000108)
    #a.bestfitline()
    #a.bestfitone()
    drawdata(data[56:89, 1], data[56:89, 0]-9617.57000108)
    #drawdata(data[:55, 1], data[:55, 0]-9617.57000108)
