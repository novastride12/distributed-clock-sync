import time

def log_result(delay, offset):
    with open("sync_log.txt", "a") as f:
        f.write(f"{time.time()},{delay},{offset}\n")