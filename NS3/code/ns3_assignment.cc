/* -*-  Mode: C++; c-file-style: "gnu"; indent-tabs-mode:nil; -*- */
/*
 * 
 *
 * Authors: Parag Bhosale <parag.bhosale@gmail.com>
 */

#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/applications-module.h"
#include "ns3/wifi-module.h"
#include "ns3/mobility-module.h"
#include "ns3/ipv4-global-routing-helper.h"
#include "ns3/internet-module.h"
#include "ns3/netanim-module.h"
#include "ns3/gnuplot.h"
#include "ns3/nstime.h"
#include "ns3/flow-monitor-module.h"


// This is a simple example in order to show how to configure an IEEE 802.11n Wi-Fi network.
//
// It ouputs the UDP or TCP goodput for every VHT bitrate value, which depends on the MCS value (0 to 7), the
// channel width (20 or 40 MHz) and the guard interval (long or short). The PHY bitrate is constant over all
// the simulation run. The user can also specify the distance between the access point and the station: the
// larger the distance the smaller the goodput.
//
// The simulation assumes a single station in an infrastructure network:
//
//  STA     AP(Moving access point)    STA (All STAs are fixed)
//    *     *                           * 
//    |     |                           |
//   n1     n2                          n10
//
//Packets in this simulation aren't marked with a QosTag so they are considered
//belonging to BestEffort Access Class (AC_BE).

using namespace ns3;

NS_LOG_COMPONENT_DEFINE ("ns3_assignment");
//NS_LOG_ERROR ("ns3_assign_error");




int main (int argc, char *argv[])
{
	for (int d=20; d<=100; d=d+5)
	{
		std::cout << "::\n";
	for (int i=2;i<=10;++i)
	{
		
  bool udp = true,verbose=false;
  double simulationTime = 10; //seconds
  int distance = d; //meters
  double frequency = 5.0; //whether 2.4 or 5.0 GHz
  int nStanodes=i;   // number of stations
  double payloadSize=1472; // payloadsize
  double dataratevalue=3; // datarate mode

  CommandLine cmd;
  cmd.AddValue ("frequency", "Whether working in the 2.4 or 5.0 GHz band (other values gets rejected)", frequency);
  cmd.AddValue ("distance", "Distance in meters between the station and the access point", distance);
  cmd.AddValue ("simulationTime", "Simulation time in seconds", simulationTime);
  cmd.AddValue ("udp", "UDP if set to 1, TCP otherwise", udp);
  cmd.AddValue ("nStanodes", "Number of stations", nStanodes);
  cmd.AddValue ("payloadSize", "payloadsize for UDP", payloadSize);
  cmd.AddValue ("dataratevalue", "datarate value for MAC", dataratevalue);
  cmd.Parse (argc,argv);



                              
					
                 NodeContainer wifiStaNode;
              wifiStaNode.Create (nStanodes);
              NodeContainer wifiApNode;
              wifiApNode.Create (1);

              YansWifiChannelHelper channel = YansWifiChannelHelper::Default ();
              YansWifiPhyHelper phy = YansWifiPhyHelper::Default ();
              phy.SetChannel (channel.Create ());

               phy.Set ("ShortGuardEnabled", BooleanValue (true)); 
                WifiHelper wifi = WifiHelper::Default (); 
                wifi.SetStandard (WIFI_PHY_STANDARD_80211n_5GHZ);
               // wifi.SetStandard (WIFI_PHY_STANDARD_80211n_2_4GHZ);       
                
  if (verbose)
    {
      wifi.EnableLogComponents ();
     }

                HtWifiMacHelper mac = HtWifiMacHelper::Default ();
              StringValue DataRate = HtWifiMacHelper::DataRateForMcs (dataratevalue);
              wifi.SetRemoteStationManager ("ns3::ConstantRateWifiManager","DataMode", DataRate,
                                            "ControlMode", DataRate);        
  
        Ssid ssid = Ssid ("ns3-80211n");


         mac.SetType ("ns3::StaWifiMac",
                           "Ssid", SsidValue (ssid),
                           "ActiveProbing", BooleanValue (false));

              NetDeviceContainer staDevice;
              staDevice = wifi.Install (phy, mac, wifiStaNode);

              mac.SetType ("ns3::ApWifiMac",
                           "Ssid", SsidValue (ssid));

              NetDeviceContainer apDevice;
              apDevice = wifi.Install (phy, mac, wifiApNode);

                Config::Set ("/NodeList/*/DeviceList/*/$ns3::WifiNetDevice/Phy/ChannelWidth", UintegerValue (20));
        // fixed mobility for STA.
              MobilityHelper mobility;
              
              mobility.SetPositionAllocator ("ns3::GridPositionAllocator",
                                 "MinX", DoubleValue (0.0),
                                 "MinY", DoubleValue (0.0),
                                 "DeltaX", DoubleValue (15.0),
                                 "DeltaY", DoubleValue (15.0),
                                 "GridWidth", UintegerValue (4),
                                 "LayoutType", StringValue ("ColumnFirst"));
       
             
             
             
             
              mobility.SetMobilityModel ("ns3::ConstantPositionMobilityModel");
				mobility.Install (wifiStaNode);
			//	mobility.Install (wifiApNode);
              
              //moving AP with variable distance from fixed STAs

                MobilityHelper mobility1;
				
              Ptr<ListPositionAllocator> positionAlloc = CreateObject<ListPositionAllocator> ();

              positionAlloc->Add (Vector (distance, 0.0, 0.0));
              
              
              mobility1.SetPositionAllocator (positionAlloc); 

              mobility1.SetMobilityModel ("ns3::ConstantPositionMobilityModel");
              
             
              
              mobility1.Install (wifiApNode);
              
			
  
                /* Internet stack*/
              InternetStackHelper stack;
              stack.Install (wifiApNode);
              stack.Install (wifiStaNode);

              Ipv4AddressHelper address;

              address.SetBase ("192.168.1.0", "255.255.255.0");
              Ipv4InterfaceContainer staNodeInterface;
              Ipv4InterfaceContainer apNodeInterface;

              staNodeInterface = address.Assign (staDevice);
              apNodeInterface = address.Assign (apDevice);

                ApplicationContainer serverApp, sinkApp;
                UdpServerHelper myServer (9);
                  serverApp = myServer.Install (wifiStaNode.Get (0));
                  serverApp.Start (Seconds (1.0));
                  serverApp.Stop (Seconds (simulationTime));

                  UdpClientHelper myClient (staNodeInterface.GetAddress (0), 9);
                  myClient.SetAttribute ("MaxPackets", UintegerValue (4294967295));
                  myClient.SetAttribute ("Interval", TimeValue (Seconds (1))); //packets/s
                  myClient.SetAttribute ("PacketSize", UintegerValue (payloadSize));//payload

                  
                  
                  ApplicationContainer clientApp = myClient.Install (wifiStaNode); 

                    
                  clientApp.Start (Seconds (2.0));
                //clientApp1.Start (Seconds (2.0));
                  clientApp.Stop (Seconds (simulationTime));
                  //clientApp1.Stop (Seconds (simulationTime));            
                Ipv4GlobalRoutingHelper::PopulateRoutingTables ();

               // phy.EnablePcap("ns3",wifiStaNode);
                  
                      AnimationInterface anim("ns3.xml");
                     
                    //calculate throughput 
                    
                     FlowMonitorHelper flowmon;
					Ptr<FlowMonitor> monitor = flowmon.Install(wifiStaNode);
                       
                    monitor->CheckForLostPackets ();

					
              Simulator::Stop (Seconds (simulationTime + 1));
             // SetResolution(US);
              Simulator::Run ();
              
             
              double nt_throughput = 0,throughput=0,nt_delay=0;bool inf=false;int f_nodes=0;
              Ptr<Ipv4FlowClassifier> classifier = DynamicCast<Ipv4FlowClassifier> (flowmon.GetClassifier ());
std::map<FlowId, FlowMonitor::FlowStats> stats = monitor->GetFlowStats ();
for (std::map<FlowId, FlowMonitor::FlowStats>::const_iterator i = stats.begin (); i != stats.end (); ++i)
{
	//std::cout << "  Tx Bytes:   " << i->second.txBytes << "\n";
	//std::cout << " Delay : " << i->second.delaySum / i->second.rxPackets << "\n";
		//Ipv4FlowClassifier::FiveTuple t = classifier->FindFlow (i->first);
	 // if ((t.sourceAddress=="10.1.1.3" && t.destinationAddress == "10.1.2.5"))
     // {

//std::cout << "Flow " << i->first << " (" << t.sourceAddress << " -> " << t.destinationAddress << ")\n";
//std::cout << " Tx Bytes: " << i->second.txBytes << "\n";
//std::cout << " Rx Bytes: " << i->second.rxBytes << "\n";
throughput=i->second.rxBytes * 8.0 / (i->second.timeLastRxPacket.GetSeconds() - i->second.timeFirstTxPacket.GetSeconds())/1024/nStanodes;
//std::cout << " Average Throughput: " << throughput << " kbps\n";
if (throughput==0)
	{
	  
        inf=true;
        f_nodes=f_nodes+1;	   
        //std::cout <<  "Delay is infinite as node no longer able to receive..........\n";
	}
	else
	{
		
		nt_delay=nt_delay+ (i->second.delaySum / i->second.rxPackets).ToDouble(Time::US);
	//std::cout << " Delay : " << i->second.delaySum / i->second.rxPackets << "\n";
		}

//std::cout << " Delay : " << i->second.delaySum / i->second.rxPackets << "\n";
     // } 
     
     
     nt_throughput=nt_throughput+throughput;
}
            
              
              Simulator::Destroy ();
                            // double throughput = 0;
                 //uint32_t totalPacketsThrough = DynamicCast<UdpServer> (serverApp.Get (0))->GetReceived ();
                 //throughput = totalPacketsThrough * payloadSize * 8 / (nStanodes * simulationTime * 1000000.0); //Mbit/s
       /*
        if(inf)
		{
		 nt_delay=-1;
		 
		 }
		 else
		 {
			nt_delay=nt_delay/nStanodes;
			
		} */
		
               nt_delay=nt_delay/(nStanodes-f_nodes);
               
               nt_throughput=nt_throughput/nStanodes;
               //std::cout << "datarate 	Distance 	Payload data 	Nodes  		Net_throughput \n";
        std::cout <<"::" << dataratevalue << "\t\t" << distance  << "\t\t" <<  payloadSize << "\t\t" << nStanodes << "\t\t"<< nt_throughput << " \t\t" << nt_delay << " \t\t" << inf << std::endl;

        //std::cout << throughput << " Mbit/s" << std::endl;
        //th[i]=throughput;
       // gnuplot.AddDataset (th[i]);
       
        
//}
/*
Gnuplot gnuplot;
Gnuplot2dDataset dataset;
//gnuplot.AddDataset (th);
gnuplot.GenerateOutput (std::cout);
*/
}
}
return 0;
}
