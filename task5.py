# The task 5 of the Prodigy Infotech Internship program--Network Packet Analyser


from scapy.all import sniff, IP, TCP, UDP
def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = "Other"
        if TCP in packet:
            protocol = "TCP"
        elif UDP in packet:
            protocol = "UDP"
        print(f"Source IP: {ip_src} -> Destination IP: {ip_dst} | Protocol: {protocol}")
        if protocol in ["TCP", "UDP"]:
            payload_len = len(packet[IP].payload)
            print(f"Payload Size: {payload_len} bytes\n")
def start_sniffing(interface="eth0"):
    print(f"[*] Starting packet capture on interface: {interface}")
    sniff(prn=packet_callback, iface=interface, store=False)
start_sniffing(interface="Wi-Fi")
