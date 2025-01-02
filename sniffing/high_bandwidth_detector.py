import psutil
import time

def detect_high_bandwidth_usage(interval=1):
    print("Watching network activity...")
    while True:
        net1 = psutil.net_io_counters()
        time.sleep(interval)
        net2 = psutil.net_io_counters()
        bytes_sent = net2.bytes_sent - net1.bytes_sent
        bytes_recv = net2.bytes_recv - net1.bytes_recv

        if bytes_sent > 1e6 or bytes_recv > 1e6:  # Seuil de 1 Mo/s
            print(f"ALERT : Suspicious activity detected ! Sended: {bytes_sent} bytes, Received: {bytes_recv} bytes")
        else:
            print(f"Sended: {bytes_sent} bytes, Received: {bytes_recv} bytes")
