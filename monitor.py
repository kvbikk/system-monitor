import psutil
import time
import logging
import os

LOG_FILE = "/home/student/system-monitor/monitor.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s - %(message)s')
logging.info("System Monitor Started")

try:
    while True:
        cpu = psutil.cpu_percent(interval=1)
        ram = psutil.virtual_memory().percent

        logging.info(f"CPU Usage: {cpu}% | RAM Usage: {ram}%")
        print(f"Status: CPU Usage: {cpu}% | RAM Usage: {ram}%", flush=True)
        time.sleep(2)
except KeyboardInterrupt:
    logging.error(f"Error")