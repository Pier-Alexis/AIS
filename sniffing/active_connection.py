import psutil

def list_connections():
    print("Actives Network connections :")
    for conn in psutil.net_connections(kind='inet'):
        laddr = f"{conn.laddr.ip}:{conn.laddr.port}" if conn.laddr else "Unknown"
        raddr = f"{conn.raddr.ip}:{conn.raddr.port}" if conn.raddr else "Unknown"
        status = conn.status
        print(f"Local: {laddr} -> Distant: {raddr}, Statut: {status}")
