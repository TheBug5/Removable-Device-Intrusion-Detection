import socket
try:
	s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
except:
	print "Failed to create socket."
host="localhost"
port = 5555
s.bind((host,port))
s.listen(10)
while 1:
	conn,adr = s.accept()
	while 1:
		reply = conn.recv(1024)
		print str(adr[0])+" : "+reply
		if(reply):
			conn.sendall("You have been warned!")
conn.close()
s.close()