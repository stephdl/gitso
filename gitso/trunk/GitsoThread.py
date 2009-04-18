#! /usr/bin/env python

"""
Gisto - Gitso is to support others

Gitso is a utility to facilitate the connection of VNC

@author: Aaron Gerber ('gerberad') <gerberad@gmail.com>
@author: Derek Buranen ('burner') <derek@buranen.info>
@copyright: 2008, 2009

Gitso is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Gitso is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Gitso.  If not, see <http://www.gnu.org/licenses/>.
"""

import threading, time
import os, sys, signal, os.path
import Processes

class GitsoThread(threading.Thread):
	def __init__(self, window, paths):
		self.window  = window
		self.paths   = paths
		self.host    = ""
		self.error   = False
		self.pid     = 0
		self.running = True
		self.process = Processes.Processes(self.window, paths)
		threading.Thread.__init__(self)
		
		
	def run(self):
		if self.host <> "":
			self.pid = self.process.getSupport(self.host)
			time.sleep(.5)
			if self.checkStatus():
				self.window.setMessage("Connected.", True)
			else:
				self.window.setMessage("Could not connect.", False)
				self.error = True
		else:
			self.pid = self.process.giveSupport()
			time.sleep(.5)
			if self.checkStatus():
				self.window.setMessage("Server running.", True)
			else:
				self.window.setMessage("Could not start server.", False)
				self.error = True

		print "GitsoThread.run(pid: " + str(self.pid) + ") running..."

		while(self.running and self.checkStatus()):
			time.sleep(.2)

		if not self.error:
			self.window.setMessage("Idle.", False)

		self.kill()

		
	def setHost(self, host=""):
		self.host = host
		
		
	def kill(self):
		self.process.KillPID()
		self.pid = 0
		self.running = False
		
	def checkStatus(self):
		if self.pid == 0:
			return False
		
		connection = []
		listen = []
		if sys.platform == 'darwin' or sys.platform.find('linux') != -1:
			if self.host <> "":
				connection = os.popen('netstat -an | grep 5500 | grep ESTABLISHED').readlines()
			else:
				listen = os.popen('netstat -an | grep 5500 | grep LISTEN').readlines()
		elif sys.platform == 'win32':
			#XP PRO only -- Need to fix the case where there is no process, it'll still return 1 line.
			#info = os.popen('WMIC PROCESS ' + str(self.pid) + ' get Processid').readlines()
			if self.host <> "":
				connection = os.popen('netstat -a | find "ESTABLISHED" | find "5500"').readlines()
			else:
				listen = os.popen('netstat -a | find "LISTEN" | find "5500"').readlines()
		else:
			print 'Platform not detected'
		
		if len(connection) == 0 and len(listen) == 0:
			return False
		else:
			return True

