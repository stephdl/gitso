#! /usr/bin/env python

import os, sys, signal, os.path

class Processes:
	def __init__(self, paths):
		self.returnPID = 0
		self.paths = paths

	def getSupport(self, host):
		if sys.platform == 'darwin':
			self.returnPID = os.spawnl(os.P_NOWAIT, '%sOSXvnc/OSXvnc-server' % self.paths['resources'], '%sOSXvnc/OSXvnc-server' % self.paths['resources'], '-connectHost', '%s' % host)
		elif sys.platform.find('linux') != -1:
			self.returnPID = os.spawnlp(os.P_NOWAIT, 'x11vnc', 'x11vnc','-nopw','-ncache','20','-solid','black','-connect','%s' % host)
		elif sys.platform == 'win32':
			self.returnPID = os.spawnl(os.P_NOWAIT, '%s\\WinVNC.exe' % os.environ['WINDIR'], '%s\\WinVNC.exe' % os.environ['WINDIR'])
			print "Launched WinVNC.exe, waiting to run -connect command..."
			import time
			time.sleep(3)
			self.returnPID = os.spawnl(os.P_NOWAIT, '%s\\WinVNC.exe' % os.environ['WINDIR'], '%s\\WinVNC.exe' % os.environ['WINDIR'], '-connect', '%s' % host)
		else:
			print 'Platform not detected'
		return self.returnPID
	
	def giveSupport(self):
		if sys.platform == 'darwin':
			if os.path.exists("/Applications/Utilities/X11.app") :
				os.spawnl(os.P_WAIT, '/usr/bin/open', '/usr/bin/open', '/Applications/Utilities/X11.app')
				dlg = wx.MessageDialog(self, "If it doesn't open shortly, please start it manually.", "Please wait while X11.app starts", wx.OK|wx.CENTRE|wx.ICON_INFORMATION)
				dlg.ShowModal()
				self.returnPID = os.spawnlp(os.P_NOWAIT, '%svncviewer/vncviewer' % self.paths['resources'], '%svncviewer/vncviewer' % self.paths['resources'], '-listen', '0')
			else:
				dlg = wx.MessageDialog(self, "We were unable to find X11.app in /Applications/Utilities", "To Give Support you need X11.app", wx.OK|wx.CENTRE|wx.ICON_ERROR)
				dlg.ShowModal()
		elif sys.platform.find('linux') != -1:
			self.returnPID = os.spawnlp(os.P_NOWAIT, 'vncviewer', 'vncviewer', '-listen')                
		elif sys.platform == 'win32':
			self.returnPID = os.spawnl(os.P_NOWAIT, "%s\\vncviewer.exe" % os.environ['WINDIR'], '%s\\vncviewer.exe' % os.environ['WINDIR'], '-listen' )
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
				#import win32api
				#handle = win32api.OpenProcess(1, 0, pid)
				#return (0 != win32api.TerminateProcess(handle, 0))
				print "windows doesn't kill processes yet"
			else:
				os.kill(self.returnPID, signal.SIGKILL)
				self.returnPID = 0
		return

