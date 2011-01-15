import socket
import time

host = 'localhost' 
port = 50000
backlog = 5 
size = 1024 

#### prepare a server socket ####
s = socket.socket(socket.AF_INET,
		  socket.SOCK_STREAM) 	# create a blocking socket
s.bind((host,port))			# bind it to a waiting port
s.listen(backlog) 			#  and listen

#### expect two numbers separated by ',' and add them togather ####
while True: 
    client, address = s.accept()
    data = client.recv(size)
    if data: 
	if data == 'kill':		# gracious termination
	    client.send('bye')
	    break

	l = data.split(',')
	r = int(l[0].strip()) + int(l[1].strip())	# add two numbers
        client.send(str(r))
        
    client.close()
