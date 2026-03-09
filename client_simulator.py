import threading
import subprocess
import time

NUM_CLIENTS = 10

def run_client():
    subprocess.run(["python", "client.py"])

threads = []

for i in range(NUM_CLIENTS):
    t = threading.Thread(target=run_client)
    threads.append(t)
    t.start()
    time.sleep(0.2)   # small delay so requests don't all fire at once

for t in threads:
    t.join()

print("All clients finished synchronization.")