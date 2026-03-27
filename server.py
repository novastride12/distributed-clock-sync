import socket
import time
import json
import threading
from security import generate_hmac, verify_hmac


HOST = "127.0.0.1"
PORT = 5000

server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print("Server running on port", PORT)


def handle_request(data, addr):

    packet = json.loads(data.decode())

    payload = packet["data"]
    signature = packet["hmac"]

    if not verify_hmac(payload, signature):
        print("Authentication failed from", addr)
        return

    t1 = payload["t1"]

    t2 = time.time()
    t3 = time.time()

    response_data = {
        "t1": t1,
        "t2": t2,
        "t3": t3
    }

    response_signature = generate_hmac(response_data)

    response_packet = {
        "data": response_data,
        "hmac": response_signature
    }

    server_socket.sendto(json.dumps(response_packet).encode(), addr)


while True:

    data, addr = server_socket.recvfrom(4096)

    thread = threading.Thread(target=handle_request, args=(data, addr))
    thread.start()