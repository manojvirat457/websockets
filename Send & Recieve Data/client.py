import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect((socket.gethostname(), 1234))

full_message = '';
while True:
    message = s.recv(8)
    if len(message) <= 0:
        break
    full_message += message.decode('UTF-8')

print(full_message)