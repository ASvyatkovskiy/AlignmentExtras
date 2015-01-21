#!/usr/bin/env python

from subprocess import Popen

#cmscond_export_iov -s sqlite_file:TrackerAlignmentErr_2009_v2_express_IOV1.db -d sqlite_file:TrackerAlignmentErr_2009_v2_express_IOV_ALL.db -i AlignmentErrors -t AlignmentErrors -b 1 -e 123097

#cmscond_list_iov --connect sqlite_file:TrackerAlignmentErr_2009_v2_express_IOV1.db --tag AlignmentErrors

runRanges = {'express':[1,123098,123570,124226,125960,131425,137380,159701,4294967295],'hlt':[1,133083,141400,153691,4294967295],'offline':[1,185189,4294967295],'offline2':[1,157865,4294967295]}
filenames = {'express':'TrackerAlignmentErr_2009_v2_express','hlt':'TrackerAlignmentErr_2009_v2_hlt','offline':'TrackerAlignmentErrors_v3_offline','offline2':'TrackerAlignmentErrors_v4_offline'}

for key in runRanges.keys():
    for iIOV in range(len(runRanges[key])-1):
        Popen('cmscond_export_iov -s sqlite_file:'+filenames[key]+'_IOV'+str(iIOV+1)+'.db -d sqlite_file:'+filenames[key]+'_ALL.db -i AlignmentErrors -t AlignmentErrors -b '+str(runRanges[key][iIOV])+' -e '+str(runRanges[key][iIOV+1]-1),shell=True).wait()
        #print 'cmscond_export_iov -s sqlite_file:'+filenames[key]+'_IOV'+str(iIOV+1)+'.db -d sqlite_file:'+filenames[key]+'_ALL.db -i AlignmentErrors -t AlignmentErrors -b '+str(runRanges[key][iIOV])+' -e '+str(runRanges[key][iIOV+1]-1)
