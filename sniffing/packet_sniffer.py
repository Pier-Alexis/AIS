from scapy.all import sniff, IP, TCP, UDP

def packet_callback(packet):
    if packet.haslayer(IP):
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        proto = "TCP" if packet.haslayer(TCP) else "UDP" if packet.haslayer(UDP) else "Other"
        print(f"[{proto}] Source: {ip_src} -> Destination: {ip_dst}")

def start_sniffing():
    print("Démarrage de la capture réseau...")
    sniff(prn=packet_callback, store=0)
