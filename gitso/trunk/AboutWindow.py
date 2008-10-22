import wx
import os, os.path, sys

class AboutWindow(wx.Frame):
	"""
	About Window for Gitso
	
	@author: Derek Buranen
	@author: Aaron Gerber
	"""
	def __init__(self, parent, id, title, paths):
		"""
		Setup About Window for Gitso
		
		@author: Derek Buranen
		@author: Aaron Gerber
		"""
		wx.Frame.__init__(self, parent, wx.ID_ANY, title, size=(525,400), style=wx.CLOSE_BOX | wx.MINIMIZE_BOX)
		icon = wx.Icon(os.path.join(paths['main'], 'icon.ico'), wx.BITMAP_TYPE_ICO)
		self.SetIcon(icon)
		
		# Create a read-only box
		license = open(paths['copyright'], 'r')

		if sys.platform == 'win32':
			self.SetBackgroundColour(wx.Colour(236,233,216))
		
		self.copyright = wx.TextCtrl(self, -1, license.read(), pos=wx.Point(0, 180), size=wx.Size(525, 160), style=wx.TE_MULTILINE | wx.ST_NO_AUTORESIZE)
		self.copyright.SetEditable(False)
		
		self.text1 = wx.StaticText(self, wx.ID_ANY, 'Gitso', pos=wx.Point(0, 13), size=wx.Size(525, 35), style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_NO_AUTORESIZE)
		font1 = wx.Font(24, wx.NORMAL, wx.NORMAL, wx.BOLD)
		self.text1.SetFont(font1)
		
		self.text2 = wx.StaticText(self, -1, "Gitso is to Support Others", pos=wx.Point(0, 48), size=wx.Size(525, 27), style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_NO_AUTORESIZE)
		self.text3 = wx.StaticText(self, -1, "Version 0.5", pos=wx.Point(0, 72), size=wx.Size(525, 27), style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_NO_AUTORESIZE)
		font2 = wx.Font(16, wx.NORMAL, wx.NORMAL, wx.NORMAL)
		self.text2.SetFont(font2)
		self.text3.SetFont(font2)
		
		self.text4 = wx.StaticText(self, -1, "Copyright 2008", pos=wx.Point(0, 102), size=wx.Size(525, 27), style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_NO_AUTORESIZE)
		self.text5 = wx.StaticText(self, -1, "Aaron Gerber and Derek Buranen", pos=wx.Point(0, 125), size=wx.Size(525, 27), style=wx.ALIGN_CENTER_HORIZONTAL | wx.ST_NO_AUTORESIZE)
		font4 = wx.Font(14, wx.NORMAL, wx.NORMAL, wx.NORMAL)
		self.text4.SetFont(font4)
		self.text5.SetFont(font4)
		
		self.url = wx.HyperlinkCtrl(self, -1, "code.google.com/p/gitso", "http://code.google.com/p/gitso", wx.Point(189, 150))
		
		self.ok = wx.Button(self, wx.ID_OK, "OK", wx.Point(425, 350))
		self.SetDefaultItem(self.ok)
		self.ok.SetFocus()
		wx.EVT_BUTTON(self, wx.ID_OK, self.CloseAbout)
		
		self.SetThemeEnabled(True)
		self.Centre()
		self.Show()
	
	def CloseAbout(self, event):
		self.Close()

