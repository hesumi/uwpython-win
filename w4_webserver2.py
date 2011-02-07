
# ws30 -- the thirty minute web server
# author: Wilhelm Fitzpatrick (rafial@well.com)
# date: August 3rd, 2002
# version: 1.0
#
# Written after attending a Dave Thomas talk at PNSS and hearing about
# his "write a web server in Ruby in one hour" challenge.
#
# Actual time spent:
#  30 minutes reading socket man page
#  30 minutes coding to first page fetched
#   3 hours making it prettier & more pythonic
#
# updated for UW Internet Programming in Python, by Brian Dorsey
#

import os, socket, sys, subprocess, re, time

defaults = ['', '8081']
mime_types = {'.jpg' : 'image/jpg', 
             '.gif' : 'image/gif', 
             '.png' : 'image/png',
             '.html' : 'text/html', 
             '.pdf' : 'application/pdf',
             '.py' : 'application/py'}
response = {}

response[200] =\
"""HTTP/1.0 200 Okay
Server: ws30
Content-type: %s

%s
"""

response[301] =\
"""HTTP/1.0 301 Moved
Server: ws30
Content-type: text/plain
Location: %s

moved
"""

response[404] =\
"""HTTP/1.0 404 Not Found
Server: ws30
Content-type: text/plain

%s not found
"""

DIRECTORY_LISTING =\
"""<html>
<head><title>%s</title></head>
<body>
<a href="%s..">..</a><br>
%s
</body>
</html>
"""

DIRECTORY_LINE = '<a href="%s">%s</a><br>'


def server_socket(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    return s

def listen(s):
    connection, client = s.accept()
    return connection.makefile('r+')

def get_request(stream):
    method = None
    while True:
        line = stream.readline()
        print line
        if not line.strip(): 
            break
        elif not method: 
            method, uri, protocol = line.split()
    return uri

def list_directory(uri):
    entries = os.listdir('.' + uri)
    entries.sort()
    return DIRECTORY_LISTING % (uri, uri, '\n'.join(
        [DIRECTORY_LINE % (e, e) for e in entries]))

def get_file(path):
    f = open(path)
    try: 
        return f.read()
    finally: 
        f.close()

def get_content(uri):
	print 'fetching:', uri

	##### Week4 Assignment query? #####
	if uri.find('/execute_py/jsonout?') != -1:
		qstr = uri[uri.find('?')+1:].strip()
#		s_n1 = uri[(uri.find('a=')+2):uri.find('&')]
#		s_n2 = uri[(uri.find('b=')+2):].strip()
#		print 'INPUT= a: '+s_n1+',\t'+'b: '+s_n2
#		print

		### call 'jsonout.py' with variables ###
		try:
			path = './execute_py/jsonout2.py'
			args = [path, qstr]

			child_proc = subprocess.Popen(args, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

			child_proc.wait()
		
			rst = child_proc.stdout.read()		# get output of 'jsonout.py'
			print 'OUTPUT=\\\n'+rst
			return (200, 'text/plain', rst)
		except IOError, e:
			return (404, e)
		
	else:
		try:
			path = '.' + uri
			if os.path.isfile(path):
				m_type = get_mime(uri)
				if m_type == 'application/py':        # Python script?
                                                  # if 'yes', open a subprocess to run it
					child_proc = subprocess.Popen('python '+path, shell=True, stdout=subprocess.PIPE)
		######  2011-02-02 #####
					child_proc.wait()

					lst = []
					for line in child_proc.stdout:    # collect all output to stdout into a list
						print '[parent_proc] '+ line.strip()
						lst.append(line)
					if re.match('<html>', lst[0]):
						m_type = 'text/html'          # swap MIME type to html
					else:
						m_type = 'text/plain'         # swap MIME type to plain text
					return (200, m_type, ''.join(lst))
				else:
					return (200, m_type, get_file(path))

			if os.path.isdir(path):
				if(uri.endswith('/')):
					return (200, 'text/html', list_directory(uri))
				else:
					return (301, uri + '/')
			else: return (404, uri)
		except IOError, e:
			return (404, e)

def get_mime(uri):
    return mime_types.get(os.path.splitext(uri)[1], 'text/plain')

def send_response(stream, content):
    stream.write(response[content[0]] % content[1:])

if __name__ == '__main__':
    args, nargs = sys.argv[1:], len(sys.argv) - 1
    host, port = (args + defaults[-2 + nargs:])[0:2]
    server = server_socket(host, int(port))
    print 'starting %s on %s...' % (host, port)
    try:
        while True:
            stream = listen (server)
            send_response(stream, get_content(get_request(stream)))
            stream.close()
    except KeyboardInterrupt:
        print 'shutting down...'
    server.close()

