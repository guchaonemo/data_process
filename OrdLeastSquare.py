#! /usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# -*- coding: gb18030 -*-


#--------------------------------------------------#
#     Author:guchao
#     mail  :guchaonemo@163.com
#     time  :2017.7.9 15:00
#     USAEG :ordinary Least Square
#--------------------------------------------------#

import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


def func(x, a, b, c):
    return a*x**3.0 + b*x**2.0 + c  # Refer [1]


def linefunc(x, a, b):
    return a*x+b


def LS(x, y):
    coeff, var_matrix = curve_fit(linefunc, x, y)
    variance = np.diagonal(var_matrix)  # Refer [3]
    SE = np.sqrt(variance)  # Refer [4]

    #======Making a dictionary to print results========
    results = {'a': [coeff[0], SE[0]], 'b': [
        coeff[1], SE[1]]}

    print "Coeff\tValue\t\tError"
    for v, c in results.iteritems():
        print v, "\t", c[0], "\t", c[1]

    #========End Results Printing=================
    # Saves the y values for the fitted model
    y2 = linefunc(x, coeff[0], coeff[1])
    plt.plot(x, y, '-*')
    plt.plot(x, y2)
    plt.show()


def OLS(x, y):
    coeff, var_matrix = curve_fit(func, x, y)
    variance = np.diagonal(var_matrix)  # Refer [3]
    SE = np.sqrt(variance)  # Refer [4]

    #======Making a dictionary to print results========
    results = {'a': [coeff[0], SE[0]], 'b': [
        coeff[1], SE[1]], 'c': [coeff[2], SE[2]]}

    print "Coeff\tValue\t\tError"
    for v, c in results.iteritems():
        print v, "\t", c[0], "\t", c[1]

    #========End Results Printing=================
    # Saves the y values for the fitted model
    y2 = func(x, coeff[0], coeff[1], coeff[2])
    plt.plot(x, y, '-*')
    plt.plot(x, y2)
    plt.show()

if __name__ == '__main__':
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
    ds = b[0:, 0]
    F = b[0:, 2]
    alpha = ds**2.0
    y = (F - alpha + 0.5*np.log(alpha))
    OLS(alpha, y)
    OLS(alpha[10:], y[10:])
    print alpha[10]
    '''
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
    x = data[:, 1]
    y = data[:, 0]
    y = y - 9617.57000108
    linindex = (np.where(np.logical_and(x > 4.0, x < 35.0)))[0]
    x = x[linindex]
    y = y[linindex]
    LS(x, y)
    per = [[0.125, 0.240510954273],
           [0.25, 0.420226959286],
           [0.05, 0.0954587154591],
           [0.075, 0.135277673431],
           [0.2, 0.385892085152],
           [0.1, 0.184806037333],
           [0.0, 0.0610930824812],
           [0.17, 0.336788004278],
           [0.15, 0.296029420513]]
    per = sorted(per)
    per = np.array(per)
    x = per[:,0]*np.pi
    y = per[:,1]
    x = (np.sin(2*x))**2.0
    LS(x, y)
    '''
