#! /usr/bin/env python

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
			time.sleep(.5)

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
		
		if sys.platform == 'darwin' or sys.platform.find('linux') != -1:
			connection = os.popen('netstat -an | grep 5500 | grep ESTABLISHED').readlines()
			listen = os.popen('netstat -an | grep 5500 | grep LISTEN').readlines()
		elif sys.platform == 'win32':
			#XP PRO only -- Need to fix the case where there is no process, it'll still return 1 line.
			#info = os.popen('WMIC PROCESS ' + str(self.pid) + ' get Processid').readlines()
			# possibly
			connection = os.popen('netstat -a | find "ESTABLISHED" | find "5500"').readlines()
			listen = os.popen('netstat -a | find "LISTEN" | find "5500"').readlines()
		else:
			print 'Platform not detected'
			connection = array()
			listen = array()
		
		if len(connection) == 0 and len(listen) == 0:
			return False
		else:
			return True

