#/usr/lib/python2.7

from BeautifulSoup import BeautifulSoup
import re

import urllib, urllib2

str1 = raw_input("Please enter the network address: ")

if "https://" in str1:
	try:
		response = urllib2.urlopen(str(str1))
	except URLError:
		print "Cannot open website!"
		response = None
elif "http://" in str1:
	try:
		response = urllib.urlopen(str(str1))
	except URLError:
		print "Cannot open website!"
		response = None
else:

	# Try HTTPS
	str2 = "https://" + str1
	try:
		response = urllib2.urlopen(str(str2))
	except URLError:
		str2 = "http://" + str1
		try:
			response = urllib.urlopen(str(str1))
		except URLError:
			print "Cannot open website!"
			response = None




if response == None:
	print "URL invalid!"
else:
	data = response.read()

	soup = BeautifulSoup(''.join(data))

	print soup.prettify()
