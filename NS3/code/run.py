#!/usr/bin/env python2
import os
import subprocess

payload = [1472,1000,500]

if os.path.exists("final_ns3.csv"):
 os.remove("final_ns3.csv")

f = open("final_out.txt","a")

#iteration for datarate and payload data

#print  "datarate 	Distance 	Payload data 	Nodes  		Net_throughput 		Avg_delay		Not_reachability";
for i in range (2,5):
 #print "Datarate change ###############################"
 for t in range(0,len(payload)):
  #print "payload change##########################" 
  #for d in range(20,70,5):
	 # for n in range (2,10):
	#print  i
	    z='./waf --run "scratch/ns3_assignment --payloadSize=' + str(payload[t]) + ' --dataratevalue=' + str(i) + '"'
	    print z
	    #d=d+2
	    #os.system(z)
	    direct_output = subprocess.check_output(z, shell=True)
	    f.write(direct_output)
#f = open('out.txt', "r+")

#val = f.readlines()

#for x in range(0,len(val)):
 # if "::" in val[x]:
	#  print "yes"
f.close()

f1 = open("final_out.txt","r+")
val=f1.readlines()

if os.path.exists("final_out.txt"):
 os.remove("final_out.txt")

#writing readings into data file  
f2 = open("final_ns3.csv","a")
f2.write("datarate 		Distance 		Payload data	 	Nodes  		Net_throughput		Delay		NR")
for x in range(0,len(val)):
  if "::" in val[x]:
	 f2.write(val[x].replace("::",""))

f2.close()
