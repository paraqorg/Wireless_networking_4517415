# Wireless_networking_4517415
## NS3

* Go to NS3 folder 
* Go to code folder
* Copy ns3_assignment.cc to scratch folder of installed ns3 in your PC
* Copy run.py to /ns-allinone-3.24.1/ns-3.24.1 path of your PC
* run python file by "***python run.py***"
* Use genarated final_ns3.csv for analysis

## GNU radio

GNU radio can be run in two modes.
* Single detector
* Cooperative detection
 
#### Single detection
* Go to GNU folder
* Go to main folder
* run "***sh set_path.sh***"
* execute any run\_{db}.py file by "***python run\_{db}.py***". db value indicates value of RF and IF gain of the RTLSDR receiver. run\_{db}.py will execute repective G\_{db}.py (actual GNU radio backend script) and its decision in final_out.txt file. 
  
#### Cooperative detection
* Follow all steps from Single detection method
* Repeat last step as many times(I recommend odd number of times for ***M out of N type***). You can choose any detector files to run (run\_{db}.py).
* Last run "***python co\_op.py***"
* 

Logic of creating different GNU files is to create nodes with different gains. This means node with less will have low detection propability as well as less false alarm probability. While node with greater gain will have more detection and false alarm probabiliy. It is up to you to choose different comination of nodes.
