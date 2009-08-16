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

import wx
import os, sys, signal, os.path

class Processes:
	def __init__(self, window, paths):
		self.returnPID = 0
		self.window = window
		self.paths = paths

	def getSupport(self, host):
		if sys.platform == 'darwin':
			self.returnPID = os.spawnl(os.P_NOWAIT, '%sOSXvnc/OSXvnc-server' % self.paths['resources'], '%sOSXvnc/OSXvnc-server' % self.paths['resources'], '-connectHost', '%s' % host)
		elif sys.platform.find('linux') != -1:
			self.returnPID = os.spawnlp(os.P_NOWAIT, 'x11vnc', 'x11vnc','-nopw','-ncache','20','-solid','black','-connect','%s' % host)
		elif sys.platform == 'win32':
			import subprocess
                        self.returnPID = subprocess.Popen(['WinVNC.exe'])
			print "Launched WinVNC.exe, waiting to run -connect command..."
			import time
			time.sleep(3)
			
			if self.paths['mode'] == 'dev':
				subprocess.Popen(['%sWinVNC.exe' % self.paths['resources'], '-connect', '%s' % host])
			else:
				subprocess.Popen(['WinVNC.exe', '-connect', '%s' % host])
		else:
			print 'Platform not detected'
		return self.returnPID
	
	def giveSupport(self):
		if sys.platform == 'darwin':
			vncviewer = '%scotvnc.app/Contents/MacOS/cotvnc' % self.paths['resources']
			print vncviewer
			self.returnPID = os.spawnlp(os.P_NOWAIT, vncviewer, vncviewer, '--listen')
		elif sys.platform.find('linux') != -1:
			self.returnPID = os.spawnlp(os.P_NOWAIT, 'vncviewer', 'vncviewer', '-bgr233', '-listen')                
		elif sys.platform == 'win32':
			import subprocess
			print self.paths['resources']
			if self.paths['mode'] == 'dev':
				self.returnPID = subprocess.Popen(['%svncviewer.exe' % self.paths['resources'], '-listen'])
			else:
				self.returnPID = subprocess.Popen(['vncviewer.exe', '-listen'])
		else:
			print 'Platform not detected'
		return self.returnPID

	def KillPID(self):
		"""
		Kill VNC instance, called by the Stop Button or Application ends.
		
		@author: Derek Buranen
		@author: Aaron Gerber
		"""
		if self.returnPID != 0:
			print "Processes.KillPID(" + str(self.returnPID) + ")"
			if sys.platform == 'win32':
				import win32api
				PROCESS_TERMINATE = 1
				handle = win32api.OpenProcess(PROCESS_TERMINATE, False, self.returnPID.pid)
				win32api.TerminateProcess(handle, -1)
				win32api.CloseHandle(handle)
			else:
				os.kill(self.returnPID, signal.SIGKILL)
			self.returnPID = 0
		return

