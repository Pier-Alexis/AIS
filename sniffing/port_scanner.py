import socket

def scan_ports(target_ip):
    print(f"Scan des ports sur {target_ip}...")
    for port in range(1, 1025):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(0.5)
                if s.connect_ex((target_ip, port)) == 0:
                    print(f"Port {port} ouvert")
        except Exception as e:
            print(f"Erreur avec le port {port}: {e}")
