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
import ConnectionWindow, GitsoThread

#Help Menu
def help_menu():
	print "Usage: " + os.path.basename(sys.argv[0]) + " [OPTION]"
	print "   OPTIONS"
	print "   --dev\t\tSet paths for development."
	print "   --host {IP|DN}\tConnects to host (support giver)."
	print "   --list {URL|LIST}\tAlternative Support list."
	print "   --help\t\tThis Menu."
	exit(0)

# Initialize Paths here.
paths = dict()
paths['resources'] = os.path.join(sys.path[0], "./")
paths['preferences'] = ''
paths['copyright'] = ''
paths['main'] = ''

if sys.platform.find('linux') != -1:
	paths['main'] = os.path.join(sys.path[0], '..', 'share', 'gitso')
	paths['copyright'] = os.path.join(sys.path[0], '..', 'share', 'doc', 'gitso', 'copyright')
else:
	paths['main'] = os.path.join(sys.path[0])
	paths['copyright'] = os.path.join(sys.path[0], 'copyright')

if len(sys.argv) == 2:
	if sys.argv[1] == '--dev':
		if sys.platform == "darwin":
			paths['resources'] = 'arch/osx/'
		elif sys.platform == "w32":
			paths['resources'] = 'arch/win32/'
		else:
			paths['resources'] = 'arch/linux/'
			paths['main'] = os.path.join(sys.path[0])
			paths['copyright'] = os.path.join(sys.path[0], 'copyright')
	else:
		help_menu()
elif len(sys.argv) > 2:
	help_menu()

if sys.platform == "darwin":
    paths['preferences'] = os.path.join(os.path.expanduser("~"), "Library", "Application Support", "Gitso")
    if os.path.exists(paths['preferences']) != True:
        os.makedirs(paths['preferences'], 0700)
    paths['preferences'] = os.path.join(paths['preferences'], "hosts")
elif sys.platform == "win32":
    paths['preferences'] = os.path.join(os.path.expanduser("~"), "Local Settings", "Application Data", ".gitso-hosts")
else:
    paths['preferences'] = os.path.join(os.path.expanduser("~"), ".gitso-hosts")

if __name__ == "__main__":
	app = wx.PySimpleApp()
	ConnectionWindow.ConnectionWindow(None, -1, "Gitso", paths)
	app.MainLoop()
	del app
