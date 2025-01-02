import psutil

def monitor_processes():
    print("Processus actifs :")
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
        try:
            print(f"PID: {proc.info['pid']}, Nom: {proc.info['name']}, Utilisateur: {proc.info['username']}")
        except psutil.AccessDenied:
            print(f"PID: {proc.info['pid']} - Accès refusé")
