#!/usr/bin/env python2
##################################################
# Parag Bhosale parag.bhosale1990@gmail.com
# Python Script for signal detection
##################################################
import scipy
import os


execfile("G_75.py")
#read raw file from GNU output
filename="out1.txt"
f1 = scipy.fromfile(open("out1.txt"), dtype=scipy.int32)
sub= f1[len(f1)-1000:len(f1)]
avg= sum(sub) / (len(sub))

f1 = scipy.fromfile(open("out1.txt"), dtype=scipy.int32)
sub= f1[len(f1)-1000:len(f1)]
avg= sum(sub) / (len(sub))
if avg > 0:
   avg=1
if os.path.exists("out1.txt"):
 os.remove("out1.txt")

f = open("final_out.txt","a")
f.write(str(avg))
f.write('\n')




if avg > 0:
   print('######### Signal is detected based on this detector ##############')
else:
   print('######### Signal is absent  based on this detector ##############')
