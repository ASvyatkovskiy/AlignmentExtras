#!/usr/bin/env python

from subprocess import Popen

print 'Processing TrackerAlignmentErr_2009_v2_express.txt...'
Popen('python extractIOV.py TrackerAlignmentErr_2009_v2_express.txt',shell=True).wait()
print 'Processing TrackerAlignmentErr_2009_v2_hlt.txt...'
Popen('python extractIOV.py TrackerAlignmentErr_2009_v2_hlt.txt',shell=True).wait()
print 'Processing TrackerAlignmentErrors_v3_offline.txt...'
Popen('python extractIOV.py TrackerAlignmentErrors_v3_offline.txt',shell=True).wait()
print 'Processing TrackerAlignmentErrors_v4_offline.txt...'
Popen('python extractIOV.py TrackerAlignmentErrors_v4_offline.txt',shell=True).wait()

#run mergeTemporalDB.py afterwards
