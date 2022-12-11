import socket
import time

HEADER = 64
PORT = 12800
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "DISCONNECT!"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)
    print(f"{msg}")
    print(f"SERVER: {client.recv(2048).decode(FORMAT)}")


for i in range(1, 25):
    str1 = f"CLIENT4: Data Fragment {i} Sent To Server"
    send(str1)
    time.sleep(10)

client.close()


