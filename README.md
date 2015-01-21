# AlignmentExtras
The repository contains a set of scripts useful for alignment studies.

First, the custom payload generation with multiple IOVs
1) Assuming the the APEs are dumped in the ASCII format from the initial db files 
using the following query:

sqlite> select DAERROR_M_ALIGNERROR_C_M_RAWID,DAERROR_M_ALIGNERROR_CV_M_P_I0,DAERROR_M_ALIGNERROR_CV_M_P_I1,DAERROR_M_ALIGNERROR_CV_M_P_I2,DAERROR_M_ALIGNERROR_CV_M_P_I3,DAERROR_M_ALIGNERROR_CV_M_P_I4,DAERROR_M_ALIGNERROR_CV_M_P_I5 from ORA_C_ALIGNMENTERR_A0 order by DAERROR_M_ALIGNERROR_C_M_RAWID;

2) run the IOV extraction steps using:
python wrapper.py

3) Merge into the super-file
python mergeTemporalDB.py

4) perfrom the upload
python upload.py ~/public/MarcoM/TrackerAlignmentErrors_v4_offline.db

See more instructions in the twiki:
#https://twiki.cern.ch/twiki/bin/viewauth/CMS/UserTagsInTheGTProcedure
