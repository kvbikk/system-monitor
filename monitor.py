import psutil
import time
import os

def clear_screen():
    os.system('clear')

def show_stats():
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    print(f"-- System Monitor --")
    print(f"CPU Usage: {cpu}%")
    print(f"RAM Usage: {ram}%")
    print(f"Disk Usage: {disk}%")
    print(f"Last Updated: {time.ctime()}")
    print(f"-------------------")
    print("Press Ctrl+C to exit.")

try:
    while True:
        clear_screen()
        show_stats()
        time.sleep(5)
except KeyboardInterrupt:
    print("\n Monitoring stopped. Goodbye!")