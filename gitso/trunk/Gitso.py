#! /usr/bin/env python

"""
Gisto - Gitso is to support others

Gitso is a utility to facilitate the connection of VNC

@author: Aaron Gerber ('gerberad')
@author: Derek Buranen ('burner') <derek@buranen.info>
@copyright: 2007-2008
"""

import wx
import ConnectionWindow, ArgsParser

if __name__ == "__main__":
	app = wx.PySimpleApp()
	args = ArgsParser.ArgsParser()
	ConnectionWindow.ConnectionWindow(None, -1, "Gitso", args.GetPaths())
	app.MainLoop()
	del app
