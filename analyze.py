def analyze():
    delays = []

    with open("sync_log.txt", "r") as f:
        for line in f:
            parts = line.strip().split(",")
            delay = float(parts[1])
            delays.append(delay)

    avg_delay = sum(delays) / len(delays)
    print("Average Delay:", avg_delay)

analyze()