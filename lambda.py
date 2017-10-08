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
from matplotlib.pyplot import savefig
import numpy as np
from matplotlib.ticker import MultipleLocator
from matplotlib.ticker import FormatStrFormatter
import matplotlib.ticker as ticker

u25 = [[1.3138, 0.15089, 0.13745, 0.028485],
       [1.4483, 0.17104, 0.15663, 0.032493],
       [1.5421, 0.18569, 0.17077, 0.035433],
       [1.578, 0.19141, 0.17634, 0.036587],
       [1.7032, 0.21194, 0.19652, 0.040761],
       [1.8242, 0.2326, 0.21712, 0.045009],
       [1.9414, 0.25337, 0.23812, 0.049331],
       [2.0549, 0.2742, 0.25944, 0.053727],
       [2.1652, 0.2951, 0.28106, 0.058198],
       [2.2724, 0.31604, 0.30294, 0.062749],
       [2.3767, 0.33701, 0.32503, 0.067383],
       [2.4784, 0.35801, 0.34731, 0.072103],
       [2.5775, 0.37905, 0.36971, 0.076915],
       [2.6743, 0.40013, 0.39221, 0.081822],
       [2.769, 0.42129, 0.41472, 0.086827],
       [2.8615, 0.44263, 0.43713, 0.091932],
       [2.9521, 0.4643, 0.45925, 0.097136],
       [3.0408, 0.48645, 0.48093, 0.10244],
       [3.2132, 0.53181, 0.52319, 0.11332],
       [3.2969, 0.55476, 0.54402, 0.11889],
       [3.3792, 0.57779, 0.56472, 0.12454],
       [3.46, 0.60085, 0.58532, 0.13026],
       [3.5394, 0.62392, 0.60583, 0.13604],
       [3.6176, 0.64699, 0.62626, 0.14189],
       [3.6944, 0.67005, 0.64661, 0.14778],
       [3.7701, 0.69308, 0.66687, 0.15372],
       [3.8446, 0.71607, 0.68706, 0.15969],
       [3.918, 0.73902, 0.70716, 0.1657],
       [3.9902, 0.76192, 0.72718, 0.17174],
       [4.0615, 0.78477, 0.74712, 0.17781],
       [4.1317, 0.80756, 0.76697, 0.18389],
       [4.201, 0.83029, 0.78673, 0.18999],
       [4.2694, 0.85295, 0.80641, 0.19611],
       [4.3368, 0.87554, 0.826, 0.20223],
       [4.4033, 0.89806, 0.8455, 0.20836],
       [4.469, 0.9205, 0.86492, 0.21449],
       [4.5339, 0.94286, 0.88424, 0.22062],
       [4.5979, 0.96514, 0.90347, 0.22675],
       [4.6612, 0.98735, 0.92261, 0.23288],
       [4.7237, 1.0095, 0.94166, 0.23899],
       [4.7855, 1.0315, 0.96062, 0.2451],
       [4.8466, 1.0534, 0.97948, 0.2512],
       [4.9069, 1.0753, 0.99825, 0.25728],
       [4.9666, 1.0971, 1.0169, 0.26335],
       [5.0256, 1.1187, 1.0355, 0.2694],
       [5.084, 1.1403, 1.054, 0.27544]]
u25 = np.array(u25)
v25 = [[1.3138, 0.15089, 0.13745, 0.028485],
       [1.4483, 0.17104, 0.15663, 0.032493],
       [1.5421, 0.18569, 0.17077, 0.035433],
       [1.578, 0.19141, 0.17634, 0.036587],
       [1.7032, 0.21194, 0.19652, 0.040761],
       [1.8242, 0.2326, 0.21712, 0.045009],
       [1.9414, 0.25337, 0.23812, 0.049331],
       [2.0549, 0.2742, 0.25944, 0.053727],
       [2.1652, 0.2951, 0.28106, 0.058198],
       [2.2724, 0.31604, 0.30294, 0.062749],
       [2.3767, 0.33701, 0.32503, 0.067383],
       [2.4784, 0.35801, 0.34731, 0.072103],
       [2.5775, 0.37905, 0.36971, 0.076915],
       [2.6743, 0.40013, 0.39221, 0.081822],
       [2.769, 0.42129, 0.41472, 0.086827],
       [2.8615, 0.44263, 0.43713, 0.091932],
       [2.9521, 0.4643, 0.45925, 0.097136],
       [3.0408, 0.48645, 0.48093, 0.10244],
       [3.2132, 0.53181, 0.52319, 0.11332],
       [3.2969, 0.55476, 0.54402, 0.11889],
       [3.3792, 0.57779, 0.56472, 0.12454],
       [3.46, 0.60085, 0.58532, 0.13026],
       [3.5394, 0.62392, 0.60583, 0.13604],
       [3.6176, 0.64699, 0.62626, 0.14189],
       [3.6944, 0.67005, 0.64661, 0.14778],
       [3.7701, 0.69308, 0.66687, 0.15372],
       [3.8446, 0.71607, 0.68706, 0.15969],
       [3.918, 0.73902, 0.70716, 0.1657],
       [3.9902, 0.76192, 0.72718, 0.17174],
       [4.0615, 0.78477, 0.74712, 0.17781],
       [4.1317, 0.80756, 0.76697, 0.18389],
       [4.201, 0.83029, 0.78673, 0.18999],
       [4.2694, 0.85295, 0.80641, 0.19611],
       [4.3368, 0.87554, 0.826, 0.20223],
       [4.4033, 0.89806, 0.8455, 0.20836],
       [4.469, 0.9205, 0.86492, 0.21449],
       [4.5339, 0.94286, 0.88424, 0.22062],
       [4.5979, 0.96514, 0.90347, 0.22675],
       [4.6612, 0.98735, 0.92261, 0.23288],
       [4.7237, 1.0095, 0.94166, 0.23899],
       [4.7855, 1.0315, 0.96062, 0.2451],
       [4.8466, 1.0534, 0.97948, 0.2512],
       [4.9069, 1.0753, 0.99825, 0.25728],
       [4.9666, 1.0971, 1.0169, 0.26335],
       [5.0256, 1.1187, 1.0355, 0.2694],
       [5.084, 1.1403, 1.054, 0.27544]]
v25 = np.array(v25)
Re25 = [4.86707866315,
        5.36755267433,
        5.71702662152,
        5.85058821727,
        6.31738177475,
        6.76909358377,
        7.20681550613,
        7.6315562339,
        8.04423694934,
        8.44569301386,
        8.83667890601,
        9.21787470299,
        9.58989308708,
        9.95328629134,
        10.3085526676,
        10.6561427229,
        10.996464568,
        11.3298887781,
        11.9773642159,
        12.2920051221,
        12.600933994,
        12.9043887666,
        13.2025889664,
        13.4957376726,
        13.7840232364,
        14.0676207919,
        14.3466935843,
        14.6213941397,
        14.8918652985,
        15.1582411274,
        15.4206477288,
        15.6792039575,
        15.9340220594,
        16.1852082394,
        16.4328631691,
        16.6770824402,
        16.9179569714,
        17.1555733735,
        17.3900142775,
        17.621358631,
        17.8496819649,
        18.0750566356,
        18.2975520438,
        18.5172348334,
        18.7341690722,
        18.9484164167]
Re25 = np.array(Re25)
Fy25 = [[0.52788, 0.21916, 0.12039, 0.0074101],
        [0.59964, 0.24955, 0.13283, 0.0092907],
        [0.65219, 0.27183, 0.14155, 0.010766],
        [0.67281, 0.28057, 0.1449, 0.011366],
        [0.74732, 0.31205, 0.15679, 0.01371],
        [0.82301, 0.34397, 0.16847, 0.016241],
        [0.89979, 0.37622, 0.18005, 0.018974],
        [0.97748, 0.40884, 0.19135, 0.02177],
        [1.0563, 0.44155, 0.20301, 0.024922],
        [1.1357, 0.47458, 0.21433, 0.028033],
        [1.2161, 0.50769, 0.22598, 0.031376],
        [1.2971, 0.54097, 0.23762, 0.03477],
        [1.3787, 0.57445, 0.24907, 0.038128],
        [1.4612, 0.60783, 0.26132, 0.041767],
        [1.5442, 0.64137, 0.27349, 0.045352],
        [1.6276, 0.67505, 0.2855, 0.048866],
        [1.7116, 0.70867, 0.29815, 0.052506],
        [1.7962, 0.74233, 0.31103, 0.056142],
        [1.9664, 0.80982, 0.33708, 0.063276],
        [2.0523, 0.84348, 0.35098, 0.066891],
        [2.1384, 0.87721, 0.3648, 0.070411],
        [2.225, 0.91086, 0.37929, 0.073946],
        [2.3117, 0.94465, 0.39332, 0.077341],
        [2.3988, 0.97833, 0.40809, 0.080753],
        [2.4862, 1.012, 0.42308, 0.084112],
        [2.5739, 1.0456, 0.43846, 0.087434],
        [2.6618, 1.0792, 0.45415, 0.090712],
        [2.7499, 1.1129, 0.46984, 0.09392],
        [2.8382, 1.1464, 0.48605, 0.097104],
        [2.9267, 1.1799, 0.50252, 0.10024],
        [3.0155, 1.2133, 0.51943, 0.10335],
        [3.1044, 1.2467, 0.53664, 0.10641],
        [3.1933, 1.2802, 0.55348, 0.1094],
        [3.2824, 1.3135, 0.57108, 0.11239],
        [3.3717, 1.3467, 0.58907, 0.11534],
        [3.461, 1.38, 0.60664, 0.11823],
        [3.5503, 1.4133, 0.62439, 0.12109],
        [3.64, 1.4463, 0.64383, 0.12397],
        [3.7295, 1.4794, 0.66197, 0.12677],
        [3.8193, 1.5123, 0.68168, 0.12959],
        [3.9091, 1.5452, 0.70109, 0.13236],
        [3.9987, 1.5782, 0.72005, 0.13509],
        [4.0885, 1.6111, 0.73943, 0.13781],
        [4.1782, 1.6439, 0.75875, 0.14051],
        [4.2679, 1.6767, 0.77824, 0.14318],
        [4.3578, 1.7093, 0.79881, 0.14585]]
Fy25 = np.array(Fy25)
Fx25 = [[0.52788, 0.21916, 0.12039, 0.0074101],
        [0.59964, 0.24955, 0.13283, 0.0092907],
        [0.65219, 0.27183, 0.14155, 0.010766],
        [0.67281, 0.28057, 0.1449, 0.011366],
        [0.74732, 0.31205, 0.15679, 0.01371],
        [0.82301, 0.34397, 0.16847, 0.016241],
        [0.89979, 0.37622, 0.18005, 0.018974],
        [0.97748, 0.40884, 0.19135, 0.02177],
        [1.0563, 0.44155, 0.20301, 0.024922],
        [1.1357, 0.47458, 0.21433, 0.028033],
        [1.2161, 0.50769, 0.22598, 0.031376],
        [1.2971, 0.54097, 0.23762, 0.03477],
        [1.3787, 0.57445, 0.24907, 0.038128],
        [1.4612, 0.60783, 0.26132, 0.041767],
        [1.5442, 0.64137, 0.27349, 0.045352],
        [1.6276, 0.67505, 0.2855, 0.048866],
        [1.7116, 0.70867, 0.29815, 0.052506],
        [1.7962, 0.74233, 0.31103, 0.056142],
        [1.9664, 0.80982, 0.33708, 0.063276],
        [2.0523, 0.84348, 0.35098, 0.066891],
        [2.1384, 0.87721, 0.3648, 0.070411],
        [2.225, 0.91086, 0.37929, 0.073946],
        [2.3117, 0.94465, 0.39332, 0.077341],
        [2.3988, 0.97833, 0.40809, 0.080753],
        [2.4862, 1.012, 0.42308, 0.084112],
        [2.5739, 1.0456, 0.43846, 0.087434],
        [2.6618, 1.0792, 0.45415, 0.090712],
        [2.7499, 1.1129, 0.46984, 0.09392],
        [2.8382, 1.1464, 0.48605, 0.097104],
        [2.9267, 1.1799, 0.50252, 0.10024],
        [3.0155, 1.2133, 0.51943, 0.10335],
        [3.1044, 1.2467, 0.53664, 0.10641],
        [3.1933, 1.2802, 0.55348, 0.1094],
        [3.2824, 1.3135, 0.57108, 0.11239],
        [3.3717, 1.3467, 0.58907, 0.11534],
        [3.461, 1.38, 0.60664, 0.11823],
        [3.5503, 1.4133, 0.62439, 0.12109],
        [3.64, 1.4463, 0.64383, 0.12397],
        [3.7295, 1.4794, 0.66197, 0.12677],
        [3.8193, 1.5123, 0.68168, 0.12959],
        [3.9091, 1.5452, 0.70109, 0.13236],
        [3.9987, 1.5782, 0.72005, 0.13509],
        [4.0885, 1.6111, 0.73943, 0.13781],
        [4.1782, 1.6439, 0.75875, 0.14051],
        [4.2679, 1.6767, 0.77824, 0.14318],
        [4.3578, 1.7093, 0.79881, 0.14585]]
Fx25 = np.array(Fx25)
Re0 = [0.643151520846,
       1.28543370589,
       5.26348007684,
       5.88604389878,
       6.5057548449,
       7.12278067582,
       7.73729960076,
       8.34949055248,
       8.95952688354,
       9.56757251139,
       10.1737797866,
       10.7782885552,
       11.3812260305,
       11.9827071948,
       12.5828355263,
       13.1817039088,
       13.7793956186,
       14.3759853209,
       14.9715400304,
       16.1597795765,
       16.75256786,
       17.3445294282,
       17.9357048689,
       18.5261312828,
       19.1158427118,
       19.7048705078,
       20.2932436491,
       20.8809890111,
       21.4681315986,
       22.0546947443,
       22.6407002792,
       23.2261686786,
       23.8111191882,
       24.395569933,
       24.9795380123,
       25.5630395817,
       26.1460899263,
       26.7287035242,
       27.3108941038,
       27.8926746943,
       28.4740576718,
       29.0550548005,
       29.6356772705,
       30.2159357322,
       30.7958403279,
       31.3754007215,
       31.9546261252]
Re0 = np.array(Re0)
Fy0 = [[0.023137, 0.0011937, 0.00045028, 6.0626e-14],
       [0.0476, 0.0033591, 0.0017755, 3.0737e-14],
       [0.2512, 0.030662, 0.024194, 6.1343e-16],
       [0.28976, 0.036144, 0.028854, 7.6563e-16],
       [0.33061, 0.042005, 0.03356, 1.2049e-15],
       [0.37246, 0.048101, 0.03824, 9.918e-16],
       [0.41416, 0.054357, 0.042832, 1.3575e-15],
       [0.45689, 0.060864, 0.047342, 1.3066e-15],
       [0.50029, 0.067583, 0.051755, 1.2309e-15],
       [0.54453, 0.074505, 0.056072, 1.3877e-15],
       [0.58785, 0.081539, 0.060251, 1.2187e-15],
       [0.63281, 0.088792, 0.064355, 1.1399e-15],
       [0.67662, 0.096135, 0.068322, 1.499e-15],
       [0.72194, 0.10367, 0.072214, 1.1819e-15],
       [0.76522, 0.11125, 0.07596, 1.642e-15],
       [0.81045, 0.11903, 0.079645, 2.0135e-15],
       [0.85524, 0.1269, 0.083222, 1.4238e-15],
       [0.90049, 0.1349, 0.086712, 1.7185e-15],
       [0.94557, 0.14301, 0.090105, 1.6986e-15],
       [1.0354, 0.15952, 0.096618, 1.6252e-15],
       [1.082, 0.16798, 0.099769, 1.577e-15],
       [1.1258, 0.17646, 0.1028, 1.5365e-15],
       [1.1701, 0.18505, 0.10575, 1.9312e-15],
       [1.2147, 0.19375, 0.10863, 2.2403e-15],
       [1.2604, 0.20257, 0.11145, 2.0825e-15],
       [1.3052, 0.21147, 0.11418, 2.6517e-15],
       [1.3503, 0.22046, 0.11684, 2.4096e-15],
       [1.3957, 0.22956, 0.11944, 3.6751e-15],
       [1.4388, 0.23869, 0.12194, 2.8388e-15],
       [1.4856, 0.248, 0.12442, 2.0744e-15],
       [1.5279, 0.2573, 0.12678, 1.8529e-15],
       [1.5735, 0.26676, 0.12912, 3.0064e-15],
       [1.617, 0.27627, 0.13137, 3.1637e-15],
       [1.6617, 0.28589, 0.13358, 3.5662e-15],
       [1.704, 0.29554, 0.13571, 2.5516e-15],
       [1.7509, 0.30539, 0.13783, 1.9615e-15],
       [1.7949, 0.31526, 0.13987, 1.9476e-15],
       [1.8382, 0.3252, 0.14185, 2.1763e-15],
       [1.8833, 0.33526, 0.1438, 2.8227e-15],
       [1.9297, 0.34544, 0.14571, 3.0057e-15],
       [1.9701, 0.35557, 0.14753, 4.4914e-15],
       [2.016, 0.36591, 0.14935, 4.7784e-15],
       [2.0586, 0.37626, 0.1511, 4.2337e-15],
       [2.1037, 0.38674, 0.15283, 3.3679e-15],
       [2.1473, 0.39728, 0.15451, 3.5667e-15],
       [2.1911, 0.4079, 0.15615, 3.2621e-15],
       [2.2331, 0.41857, 0.15775, 3.7195e-15]]
Fy0 = np.array(Fy0)
Fx0 = [[0.082254, 0.033498, 5.0721e-05, 8.2466e-15],
       [0.16452, 0.067004, 0.0009404, 3.7591e-15],
       [0.68341, 0.28054, 0.023667, 2.9759e-16],
       [0.76639, 0.31533, 0.028907, 4.2041e-16],
       [0.84923, 0.35021, 0.033819, 4.2385e-16],
       [0.93205, 0.38528, 0.038768, 5.4468e-16],
       [1.015, 0.42061, 0.04403, 5.7335e-16],
       [1.0978, 0.45606, 0.049104, 4.8103e-16],
       [1.1805, 0.49165, 0.054043, 6.7991e-16],
       [1.2632, 0.52731, 0.058752, 9.8113e-16],
       [1.3459, 0.56324, 0.063747, 6.3828e-16],
       [1.4284, 0.59912, 0.068185, 7.0839e-16],
       [1.5111, 0.63526, 0.072918, 1.1485e-15],
       [1.5936, 0.67133, 0.077103, 1.0567e-15],
       [1.6763, 0.70775, 0.081811, 1.3074e-15],
       [1.7587, 0.74402, 0.085822, 1.013e-15],
       [1.8412, 0.78043, 0.089847, 8.1305e-16],
       [1.9236, 0.81687, 0.093613, 1.0535e-15],
       [2.006, 0.85339, 0.097301, 1.5267e-15],
       [2.1708, 0.92665, 0.10437, 1.117e-15],
       [2.2529, 0.96316, 0.10721, 9.9562e-16],
       [2.3356, 1.0001, 0.11073, 2.7424e-15],
       [2.418, 1.0369, 0.11394, 1.8727e-15],
       [2.5005, 1.0738, 0.11693, 1.7132e-15],
       [2.5828, 1.1106, 0.11948, 1.4642e-15],
       [2.6651, 1.1476, 0.12211, 1.743e-15],
       [2.7475, 1.1845, 0.12452, 1.8556e-15],
       [2.8298, 1.2214, 0.12671, 2.0487e-15],
       [2.9125, 1.2587, 0.1294, 1.207e-15],
       [2.9945, 1.2955, 0.1309, 1.3066e-15],
       [3.0773, 1.3329, 0.13352, 1.0993e-15],
       [3.1596, 1.3699, 0.13508, 1.2231e-15],
       [3.2422, 1.4072, 0.1371, 1.5274e-15],
       [3.3246, 1.4444, 0.13859, 1.1511e-15],
       [3.4074, 1.4819, 0.14068, 1.4865e-15],
       [3.4894, 1.5188, 0.14128, 1.8684e-15],
       [3.5719, 1.5561, 0.1426, 1.4661e-15],
       [3.6546, 1.5935, 0.14395, 1.7616e-15],
       [3.7369, 1.6307, 0.14467, 2.226e-15],
       [3.8189, 1.6677, 0.1449, 2.1964e-15],
       [3.9021, 1.7055, 0.14669, 1.7287e-15],
       [3.9843, 1.7426, 0.1468, 2.2724e-15],
       [4.0671, 1.7802, 0.14773, 2.4903e-15],
       [4.1494, 1.8174, 0.14783, 3.2166e-15],
       [4.232, 1.8548, 0.14821, 2.2824e-15],
       [4.3145, 1.8923, 0.14845, 1.7279e-15],
       [4.3974, 1.9299, 0.14904, 2.2046e-15]]
Fx0 = np.array(Fx0)
u0 = [[0.24604, 0.023211, 0.004238, 0.0020256],
      [0.49195, 0.046171, 0.0085886, 0.0041046],
      [2.0274, 0.17524, 0.041536, 0.018189],
      [2.2701, 0.19304, 0.047398, 0.020349],
      [2.5121, 0.21021, 0.053255, 0.022454],
      [2.7537, 0.22681, 0.059052, 0.024506],
      [2.9948, 0.2429, 0.064746, 0.02651],
      [3.2353, 0.25856, 0.070306, 0.028472],
      [3.4754, 0.27385, 0.075708, 0.0304],
      [3.7151, 0.28881, 0.080937, 0.032301],
      [3.9544, 0.30349, 0.085987, 0.034181],
      [4.1933, 0.31793, 0.090854, 0.036049],
      [4.4318, 0.33216, 0.09554, 0.037909],
      [4.67, 0.34621, 0.10005, 0.039767],
      [4.9078, 0.36011, 0.10439, 0.041629],
      [5.1454, 0.37387, 0.10857, 0.043498],
      [5.3827, 0.38752, 0.1126, 0.045378],
      [5.6196, 0.40105, 0.11649, 0.047271],
      [5.8564, 0.41449, 0.12025, 0.049178],
      [6.3291, 0.44111, 0.1274, 0.053039],
      [6.5651, 0.4543, 0.13082, 0.054994],
      [6.8009, 0.46742, 0.13414, 0.056963],
      [7.0365, 0.48047, 0.13737, 0.058946],
      [7.2718, 0.49346, 0.14052, 0.060943],
      [7.507, 0.50639, 0.1436, 0.062951],
      [7.742, 0.51926, 0.14661, 0.064969],
      [7.9768, 0.53207, 0.14955, 0.066997],
      [8.2115, 0.54482, 0.15244, 0.069031],
      [8.4459, 0.55751, 0.15527, 0.071072],
      [8.6802, 0.57016, 0.15805, 0.073118],
      [8.9143, 0.58274, 0.16079, 0.075168],
      [9.1483, 0.59528, 0.16348, 0.07722],
      [9.3821, 0.60776, 0.16613, 0.079274],
      [9.6158, 0.62019, 0.16874, 0.081328],
      [9.8494, 0.63257, 0.17132, 0.083382],
      [10.0827, 0.6449, 0.17386, 0.085436],
      [10.316, 0.65718, 0.17637, 0.087487],
      [10.5491, 0.66941, 0.17885, 0.089537],
      [10.7821, 0.68159, 0.1813, 0.091584],
      [11.015, 0.69372, 0.18373, 0.093627],
      [11.2477, 0.70581, 0.18613, 0.095667],
      [11.4803, 0.71785, 0.1885, 0.097703],
      [11.7128, 0.72983, 0.19085, 0.099735],
      [11.9452, 0.74178, 0.19317, 0.10176],
      [12.1775, 0.75367, 0.19548, 0.10378],
      [12.4096, 0.76552, 0.19776, 0.1058],
      [12.6417, 0.77733, 0.20002, 0.10781]]
u0 = np.array(u0)
v0 = [[0.021242, 0.0032924, 0.0020993, 0.00071853],
      [0.042036, 0.0065934, 0.0041969, 0.0014595],
      [0.14614, 0.027222, 0.016764, 0.0083427],
      [0.158, 0.03033, 0.018675, 0.010066],
      [0.16878, 0.033347, 0.020638, 0.011936],
      [0.1786, 0.036268, 0.02272, 0.013884],
      [0.18757, 0.039095, 0.025, 0.015825],
      [0.19581, 0.041832, 0.027547, 0.017674],
      [0.20339, 0.044493, 0.030401, 0.019373],
      [0.21041, 0.047095, 0.033555, 0.020902],
      [0.21695, 0.049669, 0.036959, 0.022272],
      [0.22308, 0.052262, 0.040537, 0.023503],
      [0.22884, 0.054946, 0.044184, 0.024621],
      [0.23429, 0.05783, 0.047762, 0.025643],
      [0.23948, 0.061048, 0.051113, 0.026586],
      [0.24444, 0.064701, 0.054115, 0.02746],
      [0.24921, 0.068802, 0.05674, 0.028274],
      [0.25382, 0.073276, 0.059044, 0.029034],
      [0.25829, 0.078032, 0.061105, 0.029746],
      [0.26693, 0.088098, 0.064738, 0.031042],
      [0.27113, 0.093312, 0.066383, 0.031632],
      [0.27528, 0.098602, 0.067943, 0.032187],
      [0.27939, 0.10394, 0.06943, 0.032708],
      [0.28348, 0.10932, 0.070857, 0.033198],
      [0.28756, 0.11471, 0.072228, 0.033658],
      [0.29164, 0.12009, 0.073551, 0.03409],
      [0.29575, 0.12546, 0.07483, 0.034495],
      [0.29988, 0.13081, 0.076068, 0.034876],
      [0.30405, 0.13611, 0.07727, 0.035232],
      [0.30827, 0.14136, 0.078437, 0.035566],
      [0.31254, 0.14654, 0.079572, 0.035878],
      [0.31689, 0.15166, 0.080678, 0.03617],
      [0.32131, 0.15669, 0.081755, 0.036443],
      [0.32582, 0.16163, 0.082807, 0.036699],
      [0.33041, 0.16647, 0.083834, 0.036937],
      [0.3351, 0.17121, 0.084837, 0.03716],
      [0.33989, 0.17584, 0.085819, 0.037368],
      [0.34479, 0.18035, 0.08678, 0.037562],
      [0.34979, 0.18475, 0.087721, 0.037744],
      [0.35491, 0.18902, 0.088643, 0.037915],
      [0.36013, 0.19316, 0.089548, 0.038075],
      [0.36547, 0.19718, 0.090436, 0.038226],
      [0.37092, 0.20107, 0.091308, 0.038368],
      [0.37649, 0.20484, 0.092165, 0.038502],
      [0.38216, 0.20848, 0.093007, 0.03863],
      [0.38794, 0.212, 0.093835, 0.038753],
      [0.39383, 0.21539, 0.09465, 0.03887]]
v0 = np.array(v0)
u10 = [[1.8819, 0.17665, 0.069366, 0.03106],
       [2.095, 0.19701, 0.079286, 0.034443],
       [2.246, 0.21159, 0.086451, 0.036834],
       [2.3042, 0.21724, 0.089237, 0.037753],
       [2.5096, 0.23736, 0.099162, 0.040996],
       [2.7113, 0.25737, 0.10902, 0.044178],
       [2.9093, 0.27726, 0.11877, 0.047306],
       [3.1039, 0.29704, 0.12838, 0.050392],
       [3.2953, 0.31669, 0.13785, 0.053447],
       [3.4837, 0.3362, 0.14715, 0.056484],
       [3.6693, 0.35556, 0.15626, 0.059515],
       [3.8523, 0.37474, 0.16518, 0.062553],
       [4.0331, 0.39375, 0.17391, 0.06561],
       [4.2118, 0.41257, 0.18242, 0.068695],
       [4.3886, 0.43119, 0.19072, 0.071815],
       [4.5639, 0.4496, 0.19881, 0.074974],
       [4.7376, 0.4678, 0.20667, 0.078171],
       [4.9101, 0.48577, 0.21432, 0.081407],
       [5.2521, 0.52105, 0.22895, 0.087976],
       [5.4219, 0.53834, 0.23594, 0.091298],
       [5.5911, 0.55541, 0.24272, 0.094638],
       [5.7597, 0.57224, 0.24928, 0.09799],
       [5.928, 0.58885, 0.25563, 0.10135],
       [6.096, 0.60523, 0.26177, 0.10471],
       [6.2638, 0.62139, 0.26772, 0.10806],
       [6.4315, 0.63733, 0.27347, 0.11141],
       [6.5991, 0.65306, 0.27903, 0.11474],
       [6.7668, 0.66857, 0.28441, 0.11806],
       [6.9346, 0.68388, 0.28961, 0.12136],
       [7.1024, 0.69898, 0.29464, 0.12465],
       [7.2705, 0.71389, 0.2995, 0.12791],
       [7.4387, 0.7286, 0.30421, 0.13115],
       [7.6072, 0.74313, 0.30877, 0.13436],
       [7.7759, 0.75747, 0.31318, 0.13755],
       [7.9449, 0.77163, 0.31746, 0.14071],
       [8.1142, 0.78562, 0.3216, 0.14385],
       [8.2837, 0.79944, 0.32562, 0.14696],
       [8.4536, 0.8131, 0.32952, 0.15005],
       [8.6238, 0.82659, 0.33331, 0.15311],
       [8.7943, 0.83994, 0.33699, 0.15614],
       [8.9651, 0.85313, 0.34058, 0.15914],
       [9.1362, 0.86618, 0.34406, 0.16212],
       [9.3077, 0.87909, 0.34746, 0.16507],
       [9.4794, 0.89185, 0.35076, 0.168],
       [9.6514, 0.90449, 0.35399, 0.1709],
       [9.8238, 0.917, 0.35715, 0.17377]]
v10 = [[0.56099, 0.14998, 0.072087, 0.02516],
       [0.61894, 0.1651, 0.082279, 0.028242],
       [0.65963, 0.1757, 0.089698, 0.030485],
       [0.67522, 0.17977, 0.092597, 0.031362],
       [0.72988, 0.19407, 0.10299, 0.034517],
       [0.78291, 0.20806, 0.11339, 0.037699],
       [0.83434, 0.2218, 0.12376, 0.040899],
       [0.88416, 0.23533, 0.13405, 0.044107],
       [0.93238, 0.24868, 0.14421, 0.047315],
       [0.979, 0.26188, 0.1542, 0.050514],
       [1.024, 0.27493, 0.16399, 0.053697],
       [1.0675, 0.28785, 0.17355, 0.056859],
       [1.1095, 0.30063, 0.18286, 0.059995],
       [1.1499, 0.31328, 0.19191, 0.063102],
       [1.1888, 0.32577, 0.20069, 0.066176],
       [1.2263, 0.33811, 0.20919, 0.069216],
       [1.2624, 0.35028, 0.21741, 0.072221],
       [1.2971, 0.36226, 0.22534, 0.075191],
       [1.3625, 0.38564, 0.24038, 0.081022],
       [1.3933, 0.39701, 0.24749, 0.083886],
       [1.4229, 0.40815, 0.25434, 0.086716],
       [1.4514, 0.41906, 0.26094, 0.089512],
       [1.4787, 0.42974, 0.2673, 0.092278],
       [1.505, 0.44017, 0.27342, 0.095014],
       [1.5302, 0.45035, 0.27931, 0.097721],
       [1.5545, 0.46029, 0.28499, 0.1004],
       [1.5778, 0.46998, 0.29046, 0.10306],
       [1.6003, 0.47942, 0.29573, 0.10569],
       [1.6219, 0.48862, 0.30081, 0.1083],
       [1.6427, 0.49757, 0.30571, 0.1109],
       [1.6628, 0.50628, 0.31044, 0.11347],
       [1.6821, 0.51475, 0.315, 0.11604],
       [1.7008, 0.52299, 0.31941, 0.11858],
       [1.7188, 0.53101, 0.32367, 0.12112],
       [1.7362, 0.5388, 0.32779, 0.12365],
       [1.7531, 0.54637, 0.33178, 0.12617],
       [1.7694, 0.55374, 0.33564, 0.12868],
       [1.7853, 0.56089, 0.33938, 0.13119],
       [1.8006, 0.56785, 0.34301, 0.1337],
       [1.8155, 0.57462, 0.34653, 0.13621],
       [1.8301, 0.58119, 0.34996, 0.13872],
       [1.8442, 0.58759, 0.35329, 0.14122],
       [1.8579, 0.59381, 0.35653, 0.14374],
       [1.8713, 0.59986, 0.35968, 0.14625],
       [1.8844, 0.60575, 0.36276, 0.14877],
       [1.8972, 0.61148, 0.36576, 0.1513]]
Fx10 = [[0.66174, 0.27229, 0.062436, 0.0051393],
        [0.74487, 0.30699, 0.069904, 0.0062143],
        [0.80525, 0.33223, 0.075138, 0.0070203],
        [0.82886, 0.34211, 0.077153, 0.0073518],
        [0.91367, 0.37761, 0.084092, 0.0084932],
        [0.99924, 0.41342, 0.090644, 0.0095943],
        [1.0855, 0.44952, 0.096776, 0.010642],
        [1.1726, 0.48591, 0.10257, 0.0117],
        [1.2604, 0.52258, 0.10803, 0.012759],
        [1.3488, 0.55942, 0.11302, 0.013732],
        [1.4378, 0.5964, 0.11757, 0.014631],
        [1.5274, 0.63361, 0.12188, 0.015578],
        [1.6174, 0.67088, 0.12573, 0.016421],
        [1.7078, 0.70827, 0.12928, 0.017265],
        [1.7987, 0.74573, 0.1325, 0.018075],
        [1.8901, 0.78338, 0.13561, 0.018997],
        [1.9816, 0.82096, 0.13832, 0.019831],
        [2.0735, 0.85869, 0.14096, 0.020793],
        [2.258, 0.93421, 0.14576, 0.022906],
        [2.3506, 0.9721, 0.1481, 0.024158],
        [2.4433, 1.0099, 0.15034, 0.025511],
        [2.5362, 1.0478, 0.15263, 0.027029],
        [2.629, 1.0857, 0.15496, 0.028716],
        [2.7224, 1.1237, 0.15739, 0.030523],
        [2.8151, 1.1615, 0.15999, 0.032609],
        [2.9086, 1.1996, 0.16267, 0.034705],
        [3.002, 1.2376, 0.16554, 0.036975],
        [3.0953, 1.2756, 0.16867, 0.039399],
        [3.1887, 1.3137, 0.17199, 0.041886],
        [3.2823, 1.3518, 0.17545, 0.044385],
        [3.3753, 1.3897, 0.17958, 0.047167],
        [3.4691, 1.4279, 0.18351, 0.049726],
        [3.5621, 1.4659, 0.18834, 0.052565],
        [3.6554, 1.504, 0.19328, 0.055292],
        [3.7493, 1.5423, 0.19797, 0.057805],
        [3.8423, 1.5803, 0.20378, 0.06054],
        [3.9356, 1.6184, 0.20973, 0.063159],
        [4.0291, 1.6566, 0.21565, 0.065632],
        [4.1224, 1.6948, 0.22217, 0.068107],
        [4.216, 1.7331, 0.22859, 0.070438],
        [4.309, 1.7712, 0.23612, 0.072833],
        [4.4023, 1.8094, 0.24344, 0.075073],
        [4.4955, 1.8476, 0.25113, 0.077252],
        [4.5885, 1.8858, 0.25942, 0.079394],
        [4.6823, 1.9243, 0.26663, 0.081335],
        [4.775, 1.9624, 0.27595, 0.083385]]
Fy10 = [[0.3124, 0.12644, 0.10214, 0.020588],
        [0.36117, 0.14334, 0.11627, 0.025654],
        [0.39704, 0.15657, 0.12664, 0.029451],
        [0.41107, 0.16196, 0.1307, 0.03094],
        [0.46211, 0.18208, 0.14576, 0.036375],
        [0.5143, 0.20348, 0.16173, 0.041877],
        [0.56747, 0.22604, 0.17869, 0.047357],
        [0.62101, 0.24968, 0.19637, 0.052726],
        [0.67483, 0.27427, 0.2147, 0.057963],
        [0.72936, 0.29969, 0.23396, 0.063073],
        [0.78443, 0.32589, 0.25401, 0.068036],
        [0.83919, 0.35278, 0.27428, 0.07283],
        [0.89463, 0.38031, 0.29534, 0.077483],
        [0.95006, 0.40842, 0.31673, 0.081986],
        [1.0058, 0.43706, 0.33858, 0.086352],
        [1.0607, 0.46609, 0.36025, 0.090581],
        [1.1166, 0.49565, 0.38271, 0.094695],
        [1.1718, 0.52549, 0.40497, 0.098694],
        [1.2826, 0.58626, 0.4502, 0.10639],
        [1.3372, 0.61696, 0.47264, 0.11011],
        [1.3926, 0.64809, 0.49557, 0.11374],
        [1.4473, 0.67934, 0.51829, 0.11731],
        [1.5024, 0.71093, 0.54128, 0.12082],
        [1.5558, 0.74233, 0.56356, 0.12426],
        [1.6118, 0.77461, 0.58705, 0.12766],
        [1.6649, 0.80634, 0.60933, 0.13101],
        [1.7185, 0.83841, 0.63189, 0.13432],
        [1.7723, 0.87072, 0.65456, 0.1376],
        [1.8256, 0.90305, 0.67701, 0.14085],
        [1.878, 0.93529, 0.69917, 0.14407],
        [1.9323, 0.96831, 0.72208, 0.14727],
        [1.984, 1.0007, 0.74401, 0.15045],
        [2.0379, 1.0339, 0.76676, 0.15362],
        [2.0906, 1.067, 0.78908, 0.15677],
        [2.1413, 1.0995, 0.8107, 0.15992],
        [2.1943, 1.133, 0.8331, 0.16305],
        [2.2465, 1.1664, 0.85521, 0.16618],
        [2.2975, 1.1995, 0.87695, 0.16931],
        [2.3491, 1.2329, 0.89885, 0.17243],
        [2.3996, 1.2662, 0.92039, 0.17555],
        [2.4516, 1.3001, 0.94242, 0.17867],
        [2.5024, 1.3338, 0.96404, 0.1818],
        [2.5532, 1.3677, 0.98566, 0.18492],
        [2.6044, 1.4018, 1.0074, 0.18805],
        [2.653, 1.4351, 1.0284, 0.19118],
        [2.7048, 1.4699, 1.0503, 0.19432]]
Re10 = [5.11159780098,
        5.68136331581,
        6.08419527078,
        6.23918667323,
        6.78520185749,
        7.31969712838,
        7.84308426455,
        8.35586900665,
        8.85862439176,
        9.35196779041,
        9.83654182045,
        10.3129989254,
        10.7819892094,
        11.2441510531,
        11.7001040369,
        12.150443746,
        12.5957380849,
        13.0365247959,
        13.9065670593,
        14.3367371012,
        14.7642285753,
        15.1894182443,
        15.6126520263,
        16.0342461233,
        16.4544883124,
        16.8736393532,
        17.2919344758,
        17.709584917,
        18.1267794773,
        18.5436860776,
        18.9604532942,
        19.3772118577,
        19.7940761023,
        20.2111453554,
        20.6285052602,
        21.0462290254,
        21.4643785987,
        21.8830057642,
        22.3021531607,
        22.721855225,
        23.14213906,
        23.5630252329,
        23.9845285045,
        24.4066584954,
        24.8294202914,
        25.2528149944]
u10 = np.array(u10)
v10 = np.array(v10)
Fx10 = np.array(Fx10)
Fy10 = np.array(Fy10)


def setupfunc(ax):
    xticks = ax.get_xticks()
    xticks = np.arange(0, 36, 5)
    yticks = ax.get_yticks()
    yticks = np.arange(0, 0.5, 0.1)
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
    majorLocator = MultipleLocator(10)
    minorLocator = MultipleLocator(2)
    ymajorLocator = MultipleLocator(0.1)
    yminorLocator = MultipleLocator(0.02)
    ax.xaxis.set_minor_locator(minorLocator)
    ax.xaxis.set_major_locator(majorLocator)
    ax.yaxis.set_minor_locator(yminorLocator)
    ax.yaxis.set_major_locator(ymajorLocator)
    majors = ["0", "", "20", "", ""]
    ymajors = ["0", "", "0.2", "", ""]
    ax.xaxis.set_major_formatter(ticker.FixedFormatter(majors))
    ax.yaxis.set_major_formatter(ticker.FixedFormatter(ymajors))
    ax.yaxis.set_label_coords(-0.03, 0.5)

if __name__ == '__main__':
    font = {'fontname': 'Arial', 'weight': 'bold', 'size': 15}
    plt.plot(Re0,  np.sqrt(Fx0[:, 1]**2.0+Fy0[:,  1]**2.0), 'k*', label='0')
    plt.plot(
        Re10,     np.sqrt(Fx10[:, 1]**2.0+Fy10[:, 1]**2.0), 'ko', label=r'$0.1\pi$')
    plt.plot(
        Re25,      np.sqrt(Fx25[:, 1]**2.0+Fy25[:, 1]**2.0), 'ks', label=r'$0.25\pi$')
    plt.xlabel('$Re$', font, fontsize=20)
    plt.ylabel(r'$\lambda_4$', font, fontsize=20)
    #plt.ylim([-0.05, 0.25])
    plt.legend(frameon=False, numpoints=1, loc=2)
    plt.show()
    ulam3 = np.sqrt(u25[:, 3]**2.0+v25[:,  3]**2.0)
    ulam2 = np.sqrt(u25[:, 1]**2.0+v25[:,  1]**2.0)
    print np.dot(ulam3, ulam2)/(np.linalg.norm(ulam3)*np.linalg.norm(ulam2))
    ax = plt.gca()
    setupfunc(ax)
    plt.tick_params(axis='x', which='major', length=5, width=2)
    plt.tick_params(axis='x', which='minor', length=3)
    plt.tick_params(axis='y', which='major', length=5, width=2)
    plt.tick_params(axis='y', which='minor', length=3)
    ax.yaxis.set_label_coords(-0.05, 0.6)
    savefig('lambda4_'+'.eps', bbox_inches='tight')
    plt.close("all")
