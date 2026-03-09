import socket
import time
import json
import random
from security import generate_hmac, verify_hmac
from logger import log_result

SERVER_IP = "127.0.0.1"
PORT = 5000

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Simulate clock drift between -2 and +2 seconds
clock_drift = random.uniform(-2, 2)

print("Simulated clock drift:", clock_drift)

# t1 = client send time
t1 = time.time() + clock_drift

payload = {
    "t1": t1
}

# generate secure signature
signature = generate_hmac(payload)

packet = {
    "data": payload,
    "hmac": signature
}

# send request
client_socket.sendto(json.dumps(packet).encode(), (SERVER_IP, PORT))

# receive response
data, _ = client_socket.recvfrom(4096)

# t4 = client receive time
t4 = time.time() + clock_drift

response = json.loads(data.decode())

response_data = response["data"]
response_signature = response["hmac"]

# verify server authenticity
if not verify_hmac(response_data, response_signature):
    print("Server authentication failed")
    exit()

t1 = response_data["t1"]
t2 = response_data["t2"]
t3 = response_data["t3"]

# calculate delay
delay = (t4 - t1) - (t3 - t2)

# calculate offset
offset = ((t2 - t1) + (t3 - t4)) / 2

corrected_time = time.time() + offset

print("----------- Client Sync Result -----------")
print("Client Local Time :", time.time())
print("Network Delay     :", delay)
print("Clock Offset      :", offset)
print("Corrected Time    :", corrected_time)
print("------------------------------------------")

# log results
log_result(delay, offset)

client_socket.close()