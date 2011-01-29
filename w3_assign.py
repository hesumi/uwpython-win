import urllib, urllib2, os, re, BeautifulSoup
#MIME = ['.pdf', '.doc', '.txt', '.py']
sy_uri = 'http://briandorsey.info/uwpython/Internet_Programming_in_Python.html'
syb_uri = 'http://briandorsey.info/uwpython/'

fp = urllib2.urlopen(sy_uri)
sy = fp.read()
fp.close()

### temporary read the html doc from a file ###
#fp = open('syllabus', 'r')
#sy = fp.read()
#fp.close()
### temp script ends here ###

sy = re.sub('[\r\n]','', sy)
sySoup = BeautifulSoup.BeautifulSoup(sy)
#print sySoup.prettify()
ptr = sySoup.tr		# move pointer to label row[0]
i=0
while True:
	i+=1
	d = './w'+str(i)+'ref'
	print d
	if not os.path.exists(d):	# create the directory if doesn't exist
		os.makedirs(d)

	ptr = ptr.findNextSibling('tr')

	############## search Topics column ###############
	atag =  ptr.contents[2].findAll('a')
	for tag in atag:
		tag = str(tag)
		begin = tag.find('href=') + 6
		end = tag.find('"', begin)
		uri = tag[begin:end]
		if not re.match('http', uri):
			uri = syb_uri + uri
		fname = uri.rstrip('/').lower()
		fname = re.sub('[/:=+&]', '_', fname).strip()
		fname = re.sub('http___', '', fname)
		fname = re.sub('https___', '', fname)
		path = d+'/'+fname
		print uri
		print path
		fp = urllib.urlretrieve(uri, path)
		print
	############## search Readings column ###############
	atag = ptr.contents[3].findAll('a')
	for tag in atag:
		tag = str(tag)
		begin = tag.find('href=') + 6
		end = tag.find('"', begin)
		uri = tag[begin:end]
		if not re.match('http', uri):
			uri = syb_uri + uri
		fname = uri.rstrip('/').lower()
		fname = re.sub('[/:=+&]', '_', fname).strip()
		fname = re.sub('http___', '', fname)
		fname = re.sub('https___', '', fname)
		path = d+'/'+fname
		print uri
		print path
		fp = urllib.urlretrieve(uri, path)
		print

	if ptr == None or i >= 10:
		break
	
