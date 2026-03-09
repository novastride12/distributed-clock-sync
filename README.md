# Distributed Clock Synchronization System

This project implements a **UDP-based distributed clock synchronization system** where multiple clients synchronize their clocks with a central time server. The system also incorporates **secure message authentication using HMAC** to ensure data integrity.

The design is inspired by concepts used in the **Network Time Protocol (NTP)**.

---

# Project Overview

In distributed systems, different machines maintain independent clocks which can drift over time. This can lead to inconsistencies in:

- distributed databases  
- logging systems  
- financial transactions  
- distributed computing environments  

To address this problem, clients periodically synchronize their clocks with a **reference server**.

This project simulates that process using **UDP communication and timestamp exchange**.

---



# Time Synchronization Algorithm

The synchronization process uses four timestamps:

```
t1 → Client sends request  
t2 → Server receives request  
t3 → Server sends response  
t4 → Client receives response
```

### Network Delay

```
delay = (t4 - t1) - (t3 - t2)
```

### Clock Offset

```
offset = ((t2 - t1) + (t3 - t4)) / 2
```

The client then adjusts its logical clock using:

```
corrected_time = client_time + offset
```

---

# Security Mechanism (HMAC)

To prevent message tampering or spoofing, the system uses **HMAC (Hash-based Message Authentication Code)**.

HMAC ensures:

- message integrity  
- sender authenticity  

Each packet contains:

```
{
   "data": {...},
   "hmac": "hash_signature"
}
```

The receiver recalculates the HMAC using a **shared secret key** and verifies the authenticity of the message.

---

# Features

- UDP-based communication  
- Multiple clients supported  
- Clock synchronization using timestamp exchange  
- Network delay and offset calculation  
- Secure message authentication using HMAC  
- Artificial clock drift simulation  
- Synchronization logging for evaluation  

---

# Project Structure

```
distributed-clock-sync/

server.py
client.py
client_simulator.py
security.py
logger.py
sync_log.txt
README.md
```

---

# Running the Project

### 1. Start the server

```
python server.py
```

### 2. Run a single client

```
python client.py
```

### 3. Simulate multiple clients

```
python client_simulator.py
```

---

# Example Output

```
Simulated clock drift: -1.4

----------- Client Sync Result -----------
Client Local Time : 1712001.22
Network Delay     : 0.0021
Clock Offset      : 1.39
Corrected Time    : 1712002.61
------------------------------------------
```

This demonstrates how the system **detects and corrects clock drift**.

---

# Future Improvements (Deliverable 2)

The following enhancements are planned:

- performance evaluation under high client load  
- scalability testing with large numbers of clients  
- failure scenario analysis  
- network delay optimization  

---

# Technologies Used

- Python  
- UDP sockets (`socket`)  
- Threading  
- HMAC authentication (`hashlib`, `hmac`)  

---

# Authors

Distributed Systems Project  
Clock Synchronization using UDP and HMAC Security
