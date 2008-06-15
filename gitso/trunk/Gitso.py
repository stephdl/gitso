#! /usr/bin/env python

"""
Gisto - Gitso is to support others

Gitso is a utility to facilitate the connection of VNC

@author: Aaron Gerber ('gerberad')
@author: Derek Buranen ('burner') <derek@buranen.info>
@copyright: 2007-2008
"""

import wx
import os, sys, signal, os.path

devPath = ''
preFile = ''

class Connect(wx.Frame):
	"""
	Main Window for Gitso
	
	@author: Derek Buranen
	@author: Aaron Gerber
	"""
	
	def __init__(self, parent, id, title):
		"""
		Setup Application Window
		
        	@author: Derek Buranen
        	@author: Aaron Gerber
        	"""
		if sys.platform.find('linux') != -1:
			width = 165
		else:
			width = 145

		wx.Frame.__init__(self, parent, wx.ID_ANY, title, size=(350,width), style=wx.CLOSE_BOX | wx.MINIMIZE_BOX)
		self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

		if sys.platform != 'darwin':
			print 'set icon'
			#icon = wx.Icon("icon.ico", wx.BITMAP_TYPE_ICO)
			#self.SetIcon(icon)
		
		if sys.platform.find('linux') != -1:
			xval1 = 155
			xval2 = 250
		else:
			xval1 = 180
			xval2 = 265

		#Buttons
		self.connectButton = wx.Button(self, 10, "Start", wx.Point(xval1, 70))
		wx.EVT_BUTTON(self, 10, self.ConnectSupport)
		self.stopButton = wx.Button(self, wx.ID_STOP, "", wx.Point(xval2, 70))
		self.stopButton.Enable(False)
		wx.EVT_BUTTON(self, wx.ID_STOP, self.KillPID)
		self.returnPID = 0
		
		
		# Radio Boxes
		#self.rb = wx.RadioBox(self, 50, "", wx.Point(10, 10), wx.Size(330, 70))
		self.rb1 = wx.RadioButton(self, -1, 'Get Help', (10, 15), style=wx.RB_GROUP)
		self.rb2 = wx.RadioButton(self, -1, 'Give Support', (10, 48))
		self.rb1.SetValue(True)
				
		self.Bind(wx.EVT_RADIOBUTTON, self.RadioToggle, id=self.rb1.GetId())
		self.Bind(wx.EVT_RADIOBUTTON, self.RadioToggle, id=self.rb2.GetId())
		
		
		# the combobox Control
		self.sampleList = []
		self.sampleList = self.getHosts(self.sampleList, os.path.join(sys.path[0], 'hosts.txt'))
		self.sampleList = self.getHosts(self.sampleList, prefFile)
		self.displayHostBox(self.sampleList, "Enter/Select Support Address")
		
		# Menu		
		menuBar = wx.MenuBar()
		fileMenu = wx.Menu()
				
		editMenu = wx.Menu()
		editMenu.Append(11, "&Cut\tCtrl+X", "Cut IP Address")
		editMenu.Append(12, "&Copy\tCtrl+C", "Copy IP Address")
		editMenu.Append(wx.ID_PASTE, "&Paste\tCtrl+V", "Paste IP Address")
		wx.EVT_MENU(self, 11, self.SetClipboard)
		wx.EVT_MENU(self, 12, self.SetClipboard)
		wx.EVT_MENU(self, wx.ID_PASTE, self.GetClipboard)

		fileMenu.Append(13, "&Clear History", "Clear History")
		if sys.platform == 'darwin':
			#OS X deals with the help and file menu in  wonky way.
			fileMenu.Append(wx.ID_ABOUT, "&About", "About Gitso")
			wx.EVT_MENU(self, wx.ID_ABOUT, self.ShowAbout)
		else:		
			fileMenu.Append(wx.ID_EXIT, "&Quit\tCtrl+Q", "Quit Gitso")
			wx.EVT_MENU(self, wx.ID_EXIT, self.OnCloseWindow)

			helpMenu = wx.Menu()
			helpMenu.Append(wx.ID_ABOUT, "&About\tCtrl+A", "About Gitso")
			wx.EVT_MENU(self, wx.ID_ABOUT, self.ShowAbout)

		wx.EVT_MENU(self, 13, self.clearHistory)

		menuBar.Append(fileMenu, "&File")
		menuBar.Append(editMenu, "&Edit")
		
		if sys.platform.find('linux') != -1:
			menuBar.Append(helpMenu, "&Help")


		self.SetMenuBar(menuBar)
		
		self.statusBar = self.CreateStatusBar(2)
		self.statusBar.SetStatusText("Status:", 0)
		self.statusBar.SetStatusWidths([50, 300])
		
		self.SetDefaultItem(self.hostField)
		self.hostField.SetFocus()
		
		self.SetThemeEnabled(True)
		self.Centre()
		self.Show(True)


	def RadioToggle(self, event):
		"""
		Toggles Radio Buttons
		
		@author: Derek Buranen
		@author: Aaron Gerber
		"""
		if self.rb1.GetValue():
			self.hostField.Enable(True)
		else:
			self.hostField.Enable(False)

				
	def ConnectSupport(self, event):
		"""
		Call VNC in a thread.
		
		@author: Derek Buranen
		@author: Aaron Gerber
		"""
		if self.rb1.GetValue(): # Get Help
			if self.validHost(self.hostField.GetValue().strip()) and self.hostField.GetValue() != "Enter/Select Support Address":
				self.connectButton.Enable(False)
				self.stopButton.Enable(True)
				self.statusBar.SetStatusText("Started", 1)
				
				host = self.hostField.GetValue().strip()
				self.sampleList = []
				self.sampleList = self.getHosts(self.sampleList, os.path.join(sys.path[0], 'hosts.txt'))
				self.sampleList = self.getHosts(self.sampleList, prefFile)
				if self.sampleList.count(host) == 0:
					self.saveHost(prefFile, host)
					self.sampleList.append(host)
					self.hostField.Destroy()
					self.displayHostBox(self.sampleList, host)
				
				if sys.platform == 'darwin':
					self.returnPID = os.spawnl(os.P_NOWAIT, '%sOSXvnc/OSXvnc-server' % devPath, 'OSXvnc-server', '-connectHost', '%s' % host)
				elif sys.platform.find('linux') != -1:
					self.returnPID = os.spawnlp(os.P_NOWAIT, 'x11vnc', 'x11vnc', '-connect' , '%s' % host)
				elif sys.platform == 'win32':
					print 'win32 not implemented yet.'
				else:
					print 'platform not detected'
			else:
				self.statusBar.SetStatusText("Invalid Support Address", 1)
		else: # Give Suppport
			self.connectButton.Enable(False)
			self.stopButton.Enable(True)
			self.statusBar.SetStatusText("Started", 1)
			
			if sys.platform == 'darwin':
				if os.path.exists("/Applications/Utilities/X11.app") :
					os.spawnl(os.P_WAIT, '/usr/bin/open', 'open', '/Applications/Utilities/X11.app')
					dlg = wx.MessageDialog(self, "If it doesn't open shortly, please start it manually.", "Please wait while X11.app starts", wx.OK|wx.CENTRE|wx.ICON_INFORMATION)
					dlg.ShowModal()
					self.returnPID = os.spawnlp(os.P_NOWAIT, '%svncviewer/vncviewer' % devPath, 'vncviewer', '-listen', '0')
				else:
					dlg = wx.MessageDialog(self, "We were unable to find X11.app in /Applications/Utilities", "To Give Support you need X11.app", wx.OK|wx.CENTRE|wx.ICON_ERROR)
					dlg.ShowModal()
					self.statusBar.SetStatusText("X11.app not found.", 1)
					self.connectButton.Enable(True)
					self.stopButton.Enable(False)
			elif sys.platform.find('linux') != -1:
				self.returnPID = os.spawnlp(os.P_NOWAIT, 'vncviewer', 'vncviewer', '-listen')
			elif sys.platform == 'win32':
				print 'win32 not implemented yet.'
			else:
				print 'platform not detected'

		
	def ShowAbout(self,e):
		"""
		Display About Dialog
		
		@author: Derek Buranen
        @author: Aaron Gerber
		"""
		about = AboutWindow(self, wx.ID_ABOUT, "About Gitso")


	def clearHistory(self, event):
		handle = open(prefFile, 'w')
		handle.write("")
		handle.close()
		
		text = self.hostField.GetValue()
		self.hostField.Destroy()
		self.sampleList = []
		self.sampleList = self.getHosts(self.sampleList, os.path.join(sys.path[0], 'hosts.txt'))
		self.sampleList = self.getHosts(self.sampleList, prefFile)
		self.displayHostBox(self.sampleList, text)


	def GetClipboard(self, menu, data=None):
		"""
		Paste clipboard text in Support Entry Field
		
		@author: Derek Buranen
		@author: Aaron Gerber
		"""
		do = wx.TextDataObject()
		wx.TheClipboard.Open()
		clip = wx.TheClipboard.GetData(do)
		wx.TheClipboard.Close()
		
		if clip:
			self.hostField.SetValue(do.GetText())


	def SetClipboard(self, menu, data=None):
		"""
		Set the value of the clipboard
		
		@author: Derek Buranen
		@author: Aaron Gerber
		"""
		self.clipdata = wx.TextDataObject()
		self.clipdata.SetText(self.hostField.GetValue())
		wx.TheClipboard.Open()
		wx.TheClipboard.SetData(self.clipdata)
		wx.TheClipboard.Close()
		if menu.GetId() == 11:
			self.hostField.SetValue("")
        

	def KillPID(self, data=None):
		"""
		Kill VNC instance, called by the Stop Button or Application ends.
		
        @author: Derek Buranen
		@author: Aaron Gerber
		"""
		if self.returnPID != 0:
			os.kill(self.returnPID, signal.SIGKILL)
			self.returnPID = 0
			self.connectButton.Enable(True)
			self.stopButton.Enable(False)
			self.statusBar.SetStatusText("Idle", 1)
		else:
			self.statusBar.SetStatusText("Idle", 1)
		return


	def OnCloseWindow(self, evt):
		self.KillPID(self)
		self.Destroy()
		

	def validHost(self, host):
		if host != "" and host.find(";") == -1 and host.find("/") == -1 and host.find("'") == -1 and host.find("`") == -1 and len(host) > 6:
			return True
		else:
			return False

			
	def getHosts(self, arr, file):
		list = arr
		if os.path.exists(file):
			handle = open(file, 'r')
			fileList = handle.read()
			parsedlist = fileList.split(",")
			for i in range(0, len(parsedlist)):
				if self.validHost(parsedlist[i].strip()):
					list.append(parsedlist[i].strip())
			handle.close()
		return list


	def saveHost(self, file, host):
		handle = open(file, 'a')
		handle.write(", %s" % host)
		handle.close()
	
	def displayHostBox(self, list, text):
		self.hostField = wx.ComboBox(self, 30, "", wx.Point(105, 12), wx.Size(230, -1), list, wx.CB_DROPDOWN)
		self.hostField.SetValue(text)

class AboutWindow(wx.Frame):
	"""
	About Window for Gitso
	
	@author: Derek Buranen
	@author: Aaron Gerber
	"""
	def __init__(self, parent, id, title):
		"""
		Setup About Window for Gitso
		
		@author: Derek Buranen
		@author: Aaron Gerber
		"""
		wx.Frame.__init__(self, parent, wx.ID_ANY, title, size=(525,400), style=wx.CLOSE_BOX | wx.MINIMIZE_BOX)
		
		# Create a read-only box
		if sys.platform == "linux":
			license = open(os.path.join(sys.path[0], '..', 'share', 'doc', 'gitso', 'copyright'), 'r')
		else:
			license = open('copyright', 'r')
			
		self.copyright = wx.TextCtrl(self, -1, license.read(), pos=wx.Point(0, 180), size=wx.Size(525, 160), style=wx.TE_MULTILINE)
		self.copyright.SetEditable(False)
				
		self.text1 = wx.StaticText(self, wx.ID_ANY, 'Gitso', pos=wx.Point(0, 20), size=wx.Size(525, -1), style=wx.ALIGN_CENTER_HORIZONTAL)
		font1 = wx.Font(24, wx.NORMAL, wx.NORMAL, wx.BOLD)
		self.text1.SetFont(font1)

		self.text2 = wx.StaticText(self, -1, "Gitso is to Support Others", pos=wx.Point(0, 50), size=wx.Size(525, -1), style=wx.ALIGN_CENTER_HORIZONTAL)
		self.text3 = wx.StaticText(self, -1, "Version 0.5", pos=wx.Point(0, 72), size=wx.Size(525, -1), style=wx.ALIGN_CENTER_HORIZONTAL)
		font2 = wx.Font(16, wx.NORMAL, wx.NORMAL, wx.NORMAL)
		self.text2.SetFont(font2)
		self.text3.SetFont(font2)
		
		self.text4 = wx.StaticText(self, -1, "Copyright 2008", pos=wx.Point(0, 105), size=wx.Size(525, -1), style=wx.ALIGN_CENTER_HORIZONTAL)
		self.text5 = wx.StaticText(self, -1, "Aaron Gerber and Derek Buranen", pos=wx.Point(0, 125), size=wx.Size(525, -1), style=wx.ALIGN_CENTER_HORIZONTAL)
		font4 = wx.Font(14, wx.NORMAL, wx.NORMAL, wx.NORMAL)
		self.text4.SetFont(font4)
		self.text5.SetFont(font4)
		
		self.url = wx.HyperlinkCtrl(self, -1, "code.google.com/p/gitso", "http://code.google.com/p/gitso", wx.Point(186, 150))
		
		self.ok = wx.Button(self, wx.ID_OK, "OK", wx.Point(425, 350))
		self.SetDefaultItem(self.ok)
		self.ok.SetFocus()
		wx.EVT_BUTTON(self, wx.ID_OK, self.CloseAbout)

		self.SetThemeEnabled(True)
		self.Centre()
		self.Show()
		
		
	def CloseAbout(self, event):
		self.Close()


if len(sys.argv) == 2:
	if sys.argv[1] == '--macdev':
		devPath = 'arch/osx/'
		
if sys.platform == "darwin":
	prefFile = os.path.join(os.path.expanduser("~"), "Library", "Application Support", "Gitso")
	if os.path.exists(prefFile) != True:
		os.makedirs(prefFile, 0700)
	prefFile = os.path.join(prefFile, "hosts")
elif sys.platform == "win32":
	# I don't know where the best place is for this.
	prefFile = os.path.join(os.path.expanduser("~"), ".gitso-hosts")
else:
	prefFile = os.path.join(os.path.expanduser("~"), ".gitso-hosts")

app = wx.PySimpleApp()
Connect(None, -1, "Gitso")
app.MainLoop()
