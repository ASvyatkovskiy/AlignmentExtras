#!/usr/bin/env python

import sys
import numpy as np
from subprocess import Popen

print 'Reading file named: ', sys.argv[1][:-4]

filename = sys.argv[1][:-4]
ifile = open(filename+'.txt','r')
inputtable = ifile.readlines()
nrows = len(inputtable)
ncols = 7 #always 
nIOVs = 1 #not always!
if 'express' in filename: nIOVs = 8
if 'hlt' in filename: nIOVs = 4
if 'offline' in filename: nIOVs = 2

#for each iov
ofiles = []
for i in range(nIOVs):
    ofiles.append(open(filename+'_IOV'+str(i+1)+'.txt','w'))

for i in range(0,nrows,nIOVs):
   #print i, ' ', j, ' ', multitag_APE[i][j] 
    for ifile in range(len(ofiles)):
       ofiles[ifile].write(inputtable[i+ifile])      

for ifile in range(len(ofiles)):
    ofiles[ifile].close()

print 'Converting them to db...'
for i in range(nIOVs):
    Popen('cmsRun apeLocalSetting_cfg.py '+filename+'_IOV'+str(i+1),shell=True).wait()
