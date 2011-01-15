import socket 

host = 'localhost' #'block115387-yvm.blueboxgrid.com'
port = 50000 
size = 1024 


while(True):

    #### connect to server ####
    s = socket.socket(socket.AF_INET, 
                      socket.SOCK_STREAM) 
    s.connect((host,port)) 

    #### wait two number input & ask server to add them together ###
    l1 = raw_input('First Number(n1): ')
    l2 = raw_input('Second Number(n2): ')
    print l1, l2
    s.send(str(l1)+','+str(l2)) 
    data = s.recv(size) 

    #### disconnect from server ####
    s.close() 

    print 'n1 + n2 = ', data
    l3 = raw_input('Continue? (y/n)')
    if (l3 == 'y') or (l3 == 'Y'):
        continue
    else:
        #### connect to server ####
        s = socket.socket(socket.AF_INET, 
                          socket.SOCK_STREAM) 
        s.connect((host,port)) 

        #### terminate server process ####
        s.send('kill')
    	data = s.recv(size) 
	print data
        break


