#!/usr/bin/env python 
import numpy as np
import os, sys
from math import *
from subprocess import Popen

#final round
Sigmas = {"x":(0.02,0.03),"y":(0.1,0.2),"z":(0.08,1.0),"Phix":(0.0003,0.01),"Phiy":(0.001,0.025),"Phiz":(0.0001,0.0004)}
APEs = {'y': ([0,0.0025, 0.010, 0.04, 1.0], [0,0.010, 0.040, 0.160, 4.0]), 'x': ([0,0.0001, 0.0004, 0.0016, 0.04], [0,0.000225, 0.0009, 0.0036, 0.09]), 'z': ([0,0.0016, 0.0064, 0.0256, 0.64], [0,0.25, 1.0, 4.0, 100.0]), 'Phiz': ([0,2.5e-09, 1e-08, 4e-08, 1e-06], [0,4e-08, 1.6e-07, 6.4e-07, 1.6e-05]), 'Phiy': ([0,2.5e-07, 1e-06, 4e-06, 0.0001], [0,0.00015625, 0.000625, 0.0025, 0.0625]), 'Phix': ([0,2.25e-08, 9e-08, 3.6e-07, 9e-06], [0,2.5e-05, 0.0001, 0.0004, 0.01])}

input_file = open('template.xml','r').readlines() #everything will be replaced
length = len(input_file)

Scenarios = [0,1,2,3,4]
scenLabel = ['ZERO4','Loose4','Medium4','Tight4','Extreme4'] #['ZERO','Loose','Medium','Tight']

for scenario in Scenarios:
    for dof in Sigmas.keys():
        misalDT = np.random.normal(0, Sigmas[dof][0], length)
        misalCSC = np.random.normal(0, Sigmas[dof][1], length)
        apesCSC = APEs[dof][1][scenario]
        apesDT  = APEs[dof][0][scenario]
        output_file = open("artifScenario_Sigma"+dof+'_'+scenLabel[scenario]+".xml",'w') #str(sys.argv[2]),'w')
        for iline in range(length):
            if input_file[iline].find('setape') != -1:
                APE = apesDT
                if input_file[iline-1].find('CSC') != -1:
                    APE = apesCSC
                #print scenLabel[scenario], ' ',APE, ' ', dof
                if dof == "Phix": output_file.write("    <setape xx=\"%4.9f\" xy=\"%4.9f\" xz=\"%4.9f\" yy=\"%4.9f\" yz=\"%4.9f\" zz=\"%4.9f\" xa=\"%4.9f\" xb=\"%4.9f\" xc=\"%4.9f\" ya=\"%4.9f\" yb=\"%4.9f\" yc=\"%4.9f\" za=\"%4.9f\" zb=\"%4.9f\" zc=\"%4.9f\" aa=\"%4.9f\" ab=\"%4.9f\" ac=\"%4.9f\" bb=\"%4.9f\" bc=\"%4.9f\" cc=\"%4.9f\" />\n" % (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,APE,0,0,0,0,0))
                elif dof == "Phiz": output_file.write("    <setape xx=\"%4.9f\" xy=\"%4.9f\" xz=\"%4.9f\" yy=\"%4.9f\" yz=\"%4.9f\" zz=\"%4.9f\" xa=\"%4.9f\" xb=\"%4.9f\" xc=\"%4.9f\" ya=\"%4.9f\" yb=\"%4.9f\" yc=\"%4.9f\" za=\"%4.9f\" zb=\"%4.9f\" zc=\"%4.9f\" aa=\"%4.9f\" ab=\"%4.9f\" ac=\"%4.9f\" bb=\"%4.9f\" bc=\"%4.9f\" cc=\"%4.9f\" />\n" % (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,APE))
                elif dof == "Phiy": output_file.write("    <setape xx=\"%4.9f\" xy=\"%4.9f\" xz=\"%4.9f\" yy=\"%4.9f\" yz=\"%4.9f\" zz=\"%4.9f\" xa=\"%4.9f\" xb=\"%4.9f\" xc=\"%4.9f\" ya=\"%4.9f\" yb=\"%4.9f\" yc=\"%4.9f\" za=\"%4.9f\" zb=\"%4.9f\" zc=\"%4.9f\" aa=\"%4.9f\" ab=\"%4.9f\" ac=\"%4.9f\" bb=\"%4.9f\" bc=\"%4.9f\" cc=\"%4.9f\" />\n" % (0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,APE,0,0))
                elif dof == "x": output_file.write("    <setape xx=\"%4.9f\" xy=\"%4.9f\" xz=\"%4.9f\" yy=\"%4.9f\" yz=\"%4.9f\" zz=\"%4.9f\" xa=\"%4.9f\" xb=\"%4.9f\" xc=\"%4.9f\" ya=\"%4.9f\" yb=\"%4.9f\" yc=\"%4.9f\" za=\"%4.9f\" zb=\"%4.9f\" zc=\"%4.9f\" aa=\"%4.9f\" ab=\"%4.9f\" ac=\"%4.9f\" bb=\"%4.9f\" bc=\"%4.9f\" cc=\"%4.9f\" />\n" % (APE,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
                elif dof == "y": output_file.write("    <setape xx=\"%4.9f\" xy=\"%4.9f\" xz=\"%4.9f\" yy=\"%4.9f\" yz=\"%4.9f\" zz=\"%4.9f\" xa=\"%4.9f\" xb=\"%4.9f\" xc=\"%4.9f\" ya=\"%4.9f\" yb=\"%4.9f\" yc=\"%4.9f\" za=\"%4.9f\" zb=\"%4.9f\" zc=\"%4.9f\" aa=\"%4.9f\" ab=\"%4.9f\" ac=\"%4.9f\" bb=\"%4.9f\" bc=\"%4.9f\" cc=\"%4.9f\" />\n" % (0,0,0,APE,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
                elif dof == "z": output_file.write("    <setape xx=\"%4.9f\" xy=\"%4.9f\" xz=\"%4.9f\" yy=\"%4.9f\" yz=\"%4.9f\" zz=\"%4.9f\" xa=\"%4.9f\" xb=\"%4.9f\" xc=\"%4.9f\" ya=\"%4.9f\" yb=\"%4.9f\" yc=\"%4.9f\" za=\"%4.9f\" zb=\"%4.9f\" zc=\"%4.9f\" aa=\"%4.9f\" ab=\"%4.9f\" ac=\"%4.9f\" bb=\"%4.9f\" bc=\"%4.9f\" cc=\"%4.9f\" />\n" % (0,0,0,0,0,APE,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0))
                elif dof == "xxx": output_file.write("    <setape xx=\"%4.9f\" xy=\"%4.9f\" xz=\"%4.9f\" yy=\"%4.9f\" yz=\"%4.9f\" zz=\"%4.9f\" xa=\"%4.9f\" xb=\"%4.9f\" xc=\"%4.9f\" ya=\"%4.9f\" yb=\"%4.9f\" yc=\"%4.9f\" za=\"%4.9f\" zb=\"%4.9f\" zc=\"%4.9f\" aa=\"%4.9f\" ab=\"%4.9f\" ac=\"%4.9f\" bb=\"%4.9f\" bc=\"%4.9f\" cc=\"%4.9f\" />\n" % (APE,APE,APE,APE,APE,APE,APE,APE,APE,APE,APE,APE,APE,APE,APE,APE,APE,APE,APE,APE,APE))
            elif input_file[iline].find('setposition') != -1:
                misal = misalDT
                if input_file[iline-1].find('CSC') != -1:
                    misal = misalCSC
                MISAL = misal[iline] 
                #if not (input_file[iline-1].find("wheel=\"0\" station=\"4") !=-1): APE = 0. #or input_file[iline-1].find("wheel=\"0\" station=\"2") !=-1): APE = 0.
                #print input_file[iline-1], " ", APE
                if dof == "Phix": output_file.write("    <setposition relativeto=\"ideal\" x=\"%4.9f\" y=\"%4.9f\" z=\"%4.9f\" phix=\"%4.9f\" phiy=\"%4.9f\" phiz=\"%4.9f\" />\n" % (0,0,0,MISAL,0,0))
                elif dof == "Phiz": output_file.write("    <setposition relativeto=\"ideal\" x=\"%4.9f\" y=\"%4.9f\" z=\"%4.9f\" phix=\"%4.9f\" phiy=\"%4.9f\" phiz=\"%4.9f\" />\n" % (0,0,0,0,0,MISAL))
                elif dof == "Phiy": output_file.write("    <setposition relativeto=\"ideal\" x=\"%4.9f\" y=\"%4.9f\" z=\"%4.9f\" phix=\"%4.9f\" phiy=\"%4.9f\" phiz=\"%4.9f\" />\n" % (0,0,0,0,MISAL,0)) 
                elif dof == "x": output_file.write("    <setposition relativeto=\"ideal\" x=\"%4.9f\" y=\"%4.9f\" z=\"%4.9f\" phix=\"%4.9f\" phiy=\"%4.9f\" phiz=\"%4.9f\" />\n" % (MISAL,0,0,0,0,0))
                elif dof == "y": output_file.write("    <setposition relativeto=\"ideal\" x=\"%4.9f\" y=\"%4.9f\" z=\"%4.9f\" phix=\"%4.9f\" phiy=\"%4.9f\" phiz=\"%4.9f\" />\n" % (0,MISAL,0,0,0,0))
                elif dof == "z": output_file.write("    <setposition relativeto=\"ideal\" x=\"%4.9f\" y=\"%4.9f\" z=\"%4.9f\" phix=\"%4.9f\" phiy=\"%4.9f\" phiz=\"%4.9f\" />\n" % (0,0,MISAL,0,0,0))
            else: 
                output_file.write(input_file[iline])   
        output_file.close()

        print "Converting the xml to db..."
        Popen("cmsRun convertXMLtoSQLite_cfg.py artifScenario_Sigma"+dof+'_'+scenLabel[scenario]+".xml",shell=True).wait()
