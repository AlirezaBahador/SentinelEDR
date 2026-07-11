import psutil
import time
from datetime import datetime
from sender import send

known_pids = set()

print("[+] SentinelEDR Agent Started")

while True:
    for proc in psutil.process_iter(['pid', 'name', 'username', 'cmdline']):
        try:
            pid = proc.info['pid']

            if pid not in known_pids:
                known_pids.add(pid)

                print(f"""
[{datetime.now()}]
PID: {proc.info['pid']}
Process: {proc.info['name']}
User: {proc.info['username']}
Command: {' '.join(proc.info['cmdline'])}
                """)

        except (psutil.NoSuchProcess,
                psutil.AccessDenied):
            pass

    time.sleep(1)
