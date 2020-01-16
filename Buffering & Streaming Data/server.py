import socket
import time
HEADER_SIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 1234))

s.listen(5)

while True:
    clientSocket, address = s.accept()
    message = "Welcome to Manoj Server"
    message = f'{len(message) :< {HEADER_SIZE}}' + message
    print(f"Connection from {address} has been established")
    clientSocket.send(bytes(message, 'UTF-8'))
    
    while True:
        # time.sleep(3)
        message = f"{time.time()}"
        messge = f'{len(message) :< {HEADER_SIZE}}' + message
        clientSocket.send(bytes(message, 'UTF-8'))