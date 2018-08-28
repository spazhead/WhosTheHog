import requests
import sys
from time import sleep

class EdgeRouter(object):
	def __init__(self, host, username, password, sid):
		self.host = host
		self.username = username
		self.password = password
		self.sid = sid
		self.progress = 0.0

	def go(self):
		sleep(2)
		while self.progress < 1.0:
			self.progress += 0.01
			print(self.sid, 'progress', self.progress)
			sleep(0.2)
		print(self.sid, 'status', 'done')

host = sys.argv[1]
username = sys.argv[2]
password = sys.argv[3]
sid = sys.argv[4]
er = EdgeRouter(host, username, password, sid)
er.go()

