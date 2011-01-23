import time
import datetime

#print "Here is the time: %s" % time.time()
#print "and again: %s" % datetime.datetime.now()

##########  Compose html doc for current time ###########
lst = []
lst.append('<html>')
lst.append('<head><title>Current Time</title></head>')
lst.append('<body>')
lst.append('<h1>Current Time</h1>')
lst.append('<pre>')
lst.append("Here is the time: %s" % time.time()) 
lst.append("and again: %s" % datetime.datetime.now())
lst.append('</pre>')
lst.append('</body>')
lst.append('</html>')

##########   dump the html doc to stdout ###########
print '\n'.join(lst)
