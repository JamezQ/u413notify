#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#       u413notify.py
#       
#       Copyright 2011 James McClain <james@james-laptop>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 3 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.


import sys
import pynotify
import urllib
from BeautifulSoup import BeautifulSoup
import time
notify = pynotify.Notification("New messages on u413!","Test")
def since(stamp):
	current = time.time()
	since = current - float(stamp)
	return "("+str(int(since))+" seconds ago)"
	
def main():
	print "Starting notify..."
	f_old = ""
	while True:
		try:
			#notify.show()
			f = urllib.urlopen("http://jq.dyndns-free.com/logcheck.php").read()
			if f == f_old:
				time.sleep(10)
				continue
			soup = BeautifulSoup(f)
			lastfive = []
			for s in soup:
				lastfive.append(s.contents[0].contents[0].strip(" "))
				lastfive.append(s.contents[1].contents[0].strip(" "))
				lastfive.append(s.contents[2].contents[0].strip(" "))
				lastfive.append(s.contents[3].contents[0].strip(" "))
				lastfive.append(s.contents[4].contents[0].strip(" "))
			
			notifylist = []
			message = 0
			for x in range(5):
				
				#~ print "0:",lastfive[x+message+0]
				#~ print "1:",lastfive[x+message+1]
				#~ print "2:",lastfive[x+message+2]
				#~ print "3:",lastfive[x+message+3]
				#~ print "4:",lastfive[x+message+4]
				notifylist.append(lastfive[x+message+1]\
				+" > "+lastfive[x+message+2]+" "+since(lastfive[x+message+4])\
				)
				message += 4
			notify.update("New messages on u413!",notifylist[0]+"\n"+notifylist[1]+"\n"\
			+notifylist[2]+"\n"+notifylist[3]+"\n"+notifylist[4]+"\n")
			print "New messages on u413!"+"\n"+notifylist[0]+"\n"+notifylist[1]+"\n"\
			+notifylist[2]+"\n"+notifylist[3]+"\n"+notifylist[4]+"\n"
			notify.show()
			time.sleep(10)
			f_old = f
		except KeyboardInterrupt:
			print "Ending notify..."
			exit()
		except:
			time.sleep(10)
			continue
		
	return 0

if __name__ == '__main__':
	main()
