import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind((socket.gethostname(), 1234))

s.listen(5)

while True:
    clientSocket, address = s.accept()
    print(f"Connection from {address} has been established")
    clientSocket.send(bytes("Welcome to Manoj Server", 'UTF-8'))
    clientSocket.close()