import socket
import xml.etree.ElementTree as ET

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
def julius_connect():
	HOST = "localhost"
	PORT = 10500
	client.connect((HOST,PORT))

def julius_close():
	client.close()
	print("Connection closed ")

def julius_recv(callback):
	tmp = bytes()
	while True:
		try:
			buf = client.recv(1024)
			tmp += buf

			n = tmp.find(b"\n.\n")
			if n < 0: continue
			line = tmp[:n].decode("utf-8")
			tmp = tmp[n+3:]

			root = ET.fromstring(line)
			if root.tag != "RECOGOUT": continue
			shypo = root[0]

			words = []
			for whypo in shypo:
				words.append(whypo.attrib["WORD"])

			words = words[1:len(words)-1]
			if callback(words) == False:
				break
		except KeyboardInterrupt:
			break
	socket.close()
	return

def test_callback(words):
	print("認識した語句=",words)
	return True

if __name__ == "__main__":
	try:
		julius_connect()
		julius_recv(test_callback)
	except KeyboardInterrupt:
		client.close()


