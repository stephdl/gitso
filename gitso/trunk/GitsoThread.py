#! /usr/bin/env python

import threading, time
import os, sys, signal, os.path
import Processes

class GitsoThread(threading.Thread):
	def __init__(self, window, paths):
		self.window = window
		self.paths = paths
		self.host = ""
		self.process = Processes.Processes(paths)
		threading.Thread.__init__(self)
		
	def run(self):
		if self.host <> "":
			print "In Thread -- Starting getSupport()"
			self.process.getSupport(self.host)
		else:
			print "In Thread -- Starting giveSupport()"
			self.process.giveSupport()

	def setHost(self, host=""):
		self.host = host
		
	def kill(self):
		self.process.KillPID()
		
