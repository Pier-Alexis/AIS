import logging

# Configuration des logs
logging.basicConfig(filename='network_logs.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def log_activity(activity):
    logging.info(activity)
    print(f"Activité enregistrée : {activity}")
