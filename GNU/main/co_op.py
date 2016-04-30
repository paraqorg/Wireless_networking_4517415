#!/usr/bin/env python2

import scipy
import os

#read central decision file
f = open('final_out.txt', "r+")

val = f.readlines()
f.close()
val[len(val)-1]=val[len(val)-1].replace("\n","")


#remove central file after reading

if os.path.exists("final_out.txt"):
 os.remove("final_out.txt")

# OR decision
dec=0
for x in range(0, len(val)):
 
  dec=dec | int(val[x].replace("\n",""))
 



print "#################   OR decesion  ####################"

if int(dec)==1:
 print('Signal is detected')
else:
  print('Signal is absent')

print "######################################################"

# AND decision
dec=1
for x in range(0, len(val)):
 
 dec=dec & int(val[x].replace("\n",""))
 


print "#################   AND decesion  ####################"

if int(dec)==1:
 print('Signal is detected')
else:
  print('Signal is absent')

print "######################################################"

# M out of N decision
# in this script majority out of N decides the detection 

y_val=0 # number of detection
n_val=0 # number of absents

for x in range(0, len(val)-1):
  if int(val[x].replace("\n",""))==1:
   y_val+= 1
  else: 
	n_val+=1  
 
if y_val>n_val:
 dec=1
else: 
 dec=0
#print dec
#print val[2]


print "#################   M out of N decesion  ####################"

if int(dec)==1:
 print('Signal is detected')
else:
  print('Signal is absent')

print "######################################################"




