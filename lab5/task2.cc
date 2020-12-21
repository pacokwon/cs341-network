#include "ns3/core-module.h"
#include "ns3/network-module.h"
#include "ns3/mobility-module.h"
#include "ns3/wifi-module.h"
#include "ns3/internet-module.h"
#include "ns3/olsr-helper.h"
#include "ns3/flow-monitor-module.h"
#include "ns3/wifi-mac-helper.h"
#include "ns3/applications-module.h"
#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace ns3;

/*
 * addFlow - add flow, according to source and destination from the arguments.
 *   data rate is set to 3000000bps as default.
 *   startTime is also specified from the aargument.
 */
void addFlow(ApplicationContainer cbrApps, int port, NodeContainer nodes, int source, int destination, double startTime, uint32_t packetSize) {
    std::string destAddr = "10.1.1." + std::to_string(destination + 1);
    OnOffHelper onOffHelper1("ns3::UdpSocketFactory", InetSocketAddress(Ipv4Address(destAddr.c_str()), port));
    onOffHelper1.SetAttribute("PacketSize", UintegerValue(packetSize));
    onOffHelper1.SetAttribute("DataRate", StringValue("3000000bps"));
    onOffHelper1.SetAttribute("StartTime", TimeValue(Seconds(startTime)));
    onOffHelper1.SetAttribute("StopTime", TimeValue(Seconds(90.0)));
    cbrApps.Add(onOffHelper1.Install(nodes.Get(source)));
}

int main (int argc, char *argv[])
{
    // Network Configurations
    std::string phyMode ("DsssRate1Mbps");
    double distance = 100;  // m
    uint32_t numNodes = 64;  // by default, 5x5
    double interval = 0.1; // seconds
    uint32_t packetSize = 1500; // bytes

    // Convert to time object
    Time interPacketInterval = Seconds(interval);

    // Trigger RTS/CTS here
    bool enableCtsRts = false;
    UintegerValue ctsThr = (enableCtsRts ? UintegerValue (100) : UintegerValue (2200));
    Config::SetDefault ("ns3::WifiRemoteStationManager::RtsCtsThreshold", ctsThr);

    // Configure network - you can use examples/wireless/wifi-simple-adhoc-grid.cc as a guideline
    NodeContainer nodes;
    nodes.Create(numNodes);

    // initialize YansWifiPhyHelper instance for wifi installation on devices
    WifiHelper wifi;
    YansWifiPhyHelper wifiPhy = YansWifiPhyHelper::Default();
    wifiPhy.Set("RxGain", DoubleValue(-10));
    wifiPhy.SetPcapDataLinkType(YansWifiPhyHelper::DLT_IEEE802_11_RADIO);
    YansWifiChannelHelper wifiChannel;
    wifiChannel.SetPropagationDelay("ns3::ConstantSpeedPropagationDelayModel");
    wifiChannel.AddPropagationLoss("ns3::FriisPropagationLossModel");
    wifiPhy.SetChannel(wifiChannel.Create());

    // Create Application container and install applications
    WifiMacHelper wifiMac;
    wifi.SetStandard (WIFI_PHY_STANDARD_80211b);
    wifi.SetRemoteStationManager ("ns3::ConstantRateWifiManager",
            "DataMode",StringValue (phyMode),
            "ControlMode",StringValue (phyMode));

    // set wifi to adhoc mode
    wifiMac.SetType("ns3::AdhocWifiMac");
    NetDeviceContainer devices = wifi.Install(wifiPhy, wifiMac, nodes);

    // place nodes in a 8x8 grid.
    MobilityHelper mobility;
    mobility.SetPositionAllocator ("ns3::GridPositionAllocator",
            "MinX", DoubleValue(0.0),
            "MinY", DoubleValue(0.0),
            "DeltaX", DoubleValue(distance),
            "DeltaY", DoubleValue(distance),
            "GridWidth", UintegerValue(8),
            "LayoutType", StringValue("RowFirst"));
    mobility.SetMobilityModel("ns3::ConstantPositionMobilityModel");
    mobility.Install(nodes);

    // Enable OLSR
    OlsrHelper olsr;
    Ipv4ListRoutingHelper list;
    list.Add(olsr, 10);
    InternetStackHelper internet;
    internet.SetRoutingHelper(list);
    internet.Install(nodes);

    // install ipv4 stack on devices
    Ipv4AddressHelper ipv4;
    ipv4.SetBase("10.1.1.0", "255.255.255.0");
    Ipv4InterfaceContainer ifcont = ipv4.Assign(devices);

    ApplicationContainer cbrApps;
    uint16_t cbrPort = 12345;

    /*
       Add flows according to the specification.
       0 -> 63, 56 -> 7, 16 -> 23, 40 -> 47, 58 -> 2, 5 -> 61, 26 -> 53, 13 -> 51
       */
    addFlow(cbrApps, cbrPort, nodes,  0, 63, 10.0, packetSize);
    addFlow(cbrApps, cbrPort, nodes, 56,  7, 10.5, packetSize);
    addFlow(cbrApps, cbrPort, nodes, 16, 23, 11.0, packetSize);
    addFlow(cbrApps, cbrPort, nodes, 40, 47, 11.5, packetSize);
    addFlow(cbrApps, cbrPort, nodes, 58,  2, 12.0, packetSize);
    addFlow(cbrApps, cbrPort, nodes,  5, 61, 12.5, packetSize);
    addFlow(cbrApps, cbrPort, nodes, 26, 53, 13.0, packetSize);
    addFlow(cbrApps, cbrPort, nodes, 13, 51, 13.5, packetSize);

    // Install FlowMonitor on all nodes
    FlowMonitorHelper flowmon;
    Ptr<FlowMonitor> monitor = flowmon.Install(nodes); // TODO You can change the name of the NodeContainer if you wish

    Simulator::Stop (Seconds (100.0));
    Simulator::Run ();

    // Print per flow statistics
    monitor->CheckForLostPackets ();
    Ptr<Ipv4FlowClassifier> classifier = DynamicCast<Ipv4FlowClassifier> (flowmon.GetClassifier ());
    std::map<FlowId, FlowMonitor::FlowStats> stats = monitor->GetFlowStats ();

    for (std::map<FlowId, FlowMonitor::FlowStats>::const_iterator iter = stats.begin (); iter != stats.end (); ++iter)
    {
        Ipv4FlowClassifier::FiveTuple t = classifier->FindFlow (iter->first);

        std::cout<< "Flow ID: " << iter->first << " Src Addr " << t.sourceAddress << " Dst Addr " << t.destinationAddress << "\n";
        std::cout<< "Tx Packets = " << iter->second.txPackets << "\n";
        std::cout<< "Rx Packets = " << iter->second.rxPackets << "\n";
        std::cout<< "Throughput: " << iter->second.rxBytes * 8.0 / (iter->second.timeLastRxPacket.GetSeconds()-iter->second.timeFirstTxPacket.GetSeconds()) / 1024  << " Kbps" << "\n";
    }
    monitor->SerializeToXmlFile("scratch/practice_5.flowmon", false, true);
    Simulator::Destroy ();

    return 0;
}
