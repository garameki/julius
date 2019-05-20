import socket
import xml.etree.ElementTree as ET

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
HOST = "localhost"
PORT = 10500
client.connect((HOST,PORT))
client.disconnect()
