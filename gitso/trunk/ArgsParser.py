#! /usr/bin/env python

"""
Gisto - Gitso is to support others

Gitso is a utility to facilitate the connection of VNC

@author: Aaron Gerber ('gerberad')
@author: Derek Buranen ('burner') <derek@buranen.info>
@copyright: 2007-2008
"""

import os, sys, signal, os.path
class ArgsParser:
	def __init__(self):
		# Initialize Self.paths here.
		self.paths = dict()
		self.paths['resources'] = os.path.join(sys.path[0], "./")
		self.paths['preferences'] = ''
		self.paths['copyright'] = ''
		self.paths['main'] = ''
		self.paths['listen'] = False
		self.paths['connect'] = ''
		
		if sys.platform.find('linux') != -1:
			self.paths['main'] = os.path.join(sys.path[0], '..', 'share', 'gitso')
			self.paths['copyright'] = os.path.join(sys.path[0], '..', 'share', 'doc', 'gitso', 'copyright')
		else:
			self.paths['main'] = os.path.join(sys.path[0])
			self.paths['copyright'] = os.path.join(sys.path[0], 'copyright')
		
		#for i in range(1, len(sys.argv)):
		i = 1
		while i < len(sys.argv):
			if sys.argv[i] == '--dev': # --dev
				if sys.platform == "darwin":
					self.paths['resources'] = 'arch/osx/'
				elif sys.platform == "w32":
					self.paths['resources'] = 'arch/win32/'
				else:
					self.paths['resources'] = 'arch/linux/'
					self.paths['main'] = os.path.join(sys.path[0])
					self.paths['copyright'] = os.path.join(sys.path[0], 'copyright')

			elif sys.argv[i] == '--listen': # --listen
				if self.paths['connect'] <> "":
					print "Error: --connect and --listen can not be used at the same time."
					self.HelpMenu()
				self.paths['listen'] = True

			elif sys.argv[i] == '--connect': # --connect
				i = i + 1
				if i >= len(sys.argv) or self.paths['listen']:
					print "Error: --connect and --listen can not be used at the same time."
					self.HelpMenu()
				
				if sys.argv[i][0] + sys.argv[i][1] <> "--":
					self.paths['connect'] = sys.argv[i]
				else:
					print "Error: '" + sys.argv[i] + "' is host with '--connect'."
					self.HelpMenu()

			else:
				print "Error: '" + sys.argv[i] + "' is not a valid argument."
				self.HelpMenu()

			i = i + 1
		
		if sys.platform == "darwin":
				self.paths['preferences'] = os.path.join(os.path.expanduser("~"), "Library", "Application Support", "Gitso")
				if os.path.exists(self.paths['preferences']) != True:
						os.makedirs(self.paths['preferences'], 0700)
				self.paths['preferences'] = os.path.join(self.paths['preferences'], "hosts")
		elif sys.platform == "win32":
				self.paths['preferences'] = os.path.join(os.path.expanduser("~"), "Local Settings", "Application Data", ".gitso-hosts")
		else:
				self.paths['preferences'] = os.path.join(os.path.expanduser("~"), ".gitso-hosts")

	#Help Menu
	def HelpMenu(self):
		print "Usage: " + os.path.basename(sys.argv[0]) + " [OPTION]"
		print "   OPTIONS"
		print "   --dev\t\tSet self.paths for development."
		print "   --listen\t\tlisten for incoming connections."
		print "   --connect {IP|DN}\tConnects to host (support giver)."
		print "   --list {URL|LIST}\tAlternative Support list."
		print "   --help\t\tThis Menu."
		exit(0)
	
	def GetPaths(self):
		return self.paths
