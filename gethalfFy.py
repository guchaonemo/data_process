#! /usr/bin/env python2.7
# -*- coding: UTF-8 -*-
# -*- coding: cp936 -*-
# -*- coding: gb18030 -*-
# coding=utf-8
import os
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt


def halfforce(FileName):
    result = pd.read_table(FileName, skiprows=3, names=[
                           '1', '2', '3', '4', '5', '6', '7'], sep='  ', iterator=True)
    #Fy    =sum(result[abs(result['2'])>0.5].values)[5]
    loop = True
    chunkSize = 100000
    chunks = []
    while loop:
        try:
            chunk = result.get_chunk(chunkSize)
            chunks.append(chunk)
        except StopIteration:
            loop = False
            # print "Iteration is stopped"
    result = pd.concat(chunks, ignore_index=True)
    Fx = sum(result.values)[4]
    Fy = sum(result.values)[5]
    u = (result['3'].values).mean()
    v = (result['4'].values).mean()
    return Fx, Fy, u, v


# get the foldes in this path
def getdirfolders(Path):
    Folder = os.walk(Path)
    Folders = []
    for eachfolder in Folder:
        temp = (eachfolder[0].split('\\'))[-1]
        if 'Niu' in temp:
            Folders.append(eachfolder[0])
    return Folders

# use ergun equation to compute the drag force


def ergun_equation(ds, u, mu, gravity, epson):
    return (150.0*(1.0-epson)**3.0)*mu*u/(gravity*ds**2)/(epson**2)+1.75*(1.0-epson)*u**2/(gravity*ds*epson**2)

# compute the normalized permeability


def Normal_permeability(u, grav, mu, ds):
    return (u*mu/(grav*ds**2))


def Normalized(L):
    return (L-np.min(L))/(np.max(L)-np.min(L))

# compute gravity use poiseuille flow


def avePoiseuille(ds, Ma, mu):
    u = Ma/np.sqrt(3.0)
    return u*(12.0*mu)/(1.0-ds)**2
    # return gra*(1.0-ds)**2/(12.0*mu)


def PoiseuilleVelocity(gra, ds, mu):
    return gra*(1.0-ds)**2/(12.0*mu)
if __name__ == "__main__":
    Folders = getdirfolders(
        r"D:\datapaper\blocktrt\NoLinear\volume\highsolidfraction")
    result = []
    for each in Folders:
        try:
            Grid = float(each.split("_")[5])
            mu = float(each.split("_")[1])  # the viscosity of the flow
            Fg = float(each.split("_")[3])  # a=F,the gravity force
            Angle = float(each.split("_")[6])
            d_s = 1.0-2.0*float(each.split("_")[7])/float(each.split("_")[8])
            Fx, Fy, u, v = halfforce(each+"\\force.dat")
            U_ave = np.sqrt(u**2+v**2)
            Re = U_ave*d_s/mu
            permea = Normal_permeability(U_ave, Fg, mu, d_s)
            F_total = np.sqrt(Fx**2+Fy**2)/mu/U_ave/Grid**2.0
            PoiseuilleVelo = PoiseuilleVelocity(Fg, d_s, mu)
            #tmp  = [Angle,Re,F_total,Fx,Fy,u,v,PoiseuilleVelo,permea]
            tmp = [d_s, Grid, Re, np.float64(U_ave), np.float64(permea)]
            result.append(tmp)
            # print "%.12lf %.12lf %.12lf %.12lf %.12lf %.12lf
            # %.12lf"%(d_s,mu,Fg,Fx,Fy,u,v)
        except:
            pass
    result.sort(key=lambda x: x[0])
    for each in result:
        print '\t'.join([str(a) for a in each])
