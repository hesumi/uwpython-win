import socket 

host = 'localhost' #'block115387-yvm.blueboxgrid.com'
port = 50000 
size = 1024 
s = socket.socket(socket.AF_INET, 
                  socket.SOCK_STREAM) 
s.connect((host,port)) 
s.send('10, 25') 
data = s.recv(size) 
s.close() 
print 'Received:', data

