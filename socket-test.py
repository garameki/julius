import socket
import sys
HOST="localhost"
PORT = 10500
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect((HOST,PORT))

print(client.recv(4096))
print(client.recv(4096))
print(client.recv(4096))

client.close()
