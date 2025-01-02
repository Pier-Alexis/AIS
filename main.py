from sniffing.packet_sniffer import start_sniffing
from sniffing.high_bandwidth_detector import detect_high_bandwidth_usage
from scanning.port_scanner import scan_ports
from monitoring.active_connections import list_connections
from monitoring.process_monitor import monitor_processes
from alerts.log_handler import log_activity
from alerts.email_alerts import send_alert

def main():
    print("1. Capture network trafic")
    print("2. Detect a high consommation of network band")
    print("3. Scan open ports")
    print("4. Lists networks connections")
    print("5. Watch network connection")
    choice = input("Choose an option : ")

    if choice == "1":
        start_sniffing()
    elif choice == "2":
        detect_high_bandwidth_usage()
    elif choice == "3":
        target = input("Entrez l'adresse IP cible : ")
        scan_ports(target)
    elif choice == "4":
        list_connections()
    elif choice == "5":
        monitor_processes()
    else:
        print("Invalid option. Please enter a valid number.")

if __name__ == "__main__":
    main()
