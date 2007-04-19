#!/usr/bin/env python
# Copyright (c) 2007
#      Aaron Gerber ('gerberad')
#      Derek Buranen ('bur[n]er') <xburnerx@gmail.com>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, write to:
# 	The Free Software Foundation, Inc.,
# 	51 Franklin Street, Fifth Floor
# 	Boston, MA  02110-1301, USA.

import pygtk
pygtk.require('2.0')
import gtk
import os
import signal
import webbrowser

class Connect:

	# Make sure the URLs are clickable
	def openURL(func, url):
		webbrowser.open_new(url)

	gtk.about_dialog_set_url_hook(openURL)
	

	# Callback: radioToggle
 	#               : EVENT - Radio buttons toggled
	def radioToggle(self, widget, data=None):
		value = (data, ("OFF", "ON")[widget.get_active()])
		if value[0] == "_Get Help":
			if value[1] == "ON":
				self.GetSupportEntry.set_sensitive(True)
				self.GetSupportEntry.grab_focus()
		elif value[0] == "Give _Support":
			if value[1] == "ON":
				self.GetSupportEntry.set_sensitive(False)
    
    
	# Callback: connectSupport
	#               : EVENT - Connect button was pressed
	def connectSupport(self, widget, data=None):
		if self.GetSupportRadio.get_active()  == True:
			self.connectButton.set_sensitive(False)
			self.stopButton.set_sensitive(True)
			self.statusLabel.set_text(self.statusLabelText[1])
			self.returnPID = os.spawnlp(os.P_NOWAIT, 'x11vnc', 'x11vnc', "-connect %s" % self.GetSupportEntry.get_text())
		else:
			self.connectButton.set_sensitive(False)
			self.stopButton.set_sensitive(True)
			self.statusLabel.set_text(self.statusLabelText[1])
			self.returnPID = os.spawnlp(os.P_NOWAIT, 'vncviewer', 'vncviewer', '-listen')

    
    # Callback: showAbout
    #               : EVENT - About Gitso selected
	def showAbout(self, widget, data=None):
		license = open('aboutlicense.txt', 'r')
		aboutDialog = gtk.AboutDialog()
		aboutDialog.set_name("Gitso")
		aboutDialog.set_version("0.1.1")
		aboutDialog.set_authors(["Derek Buranen", "Aaron Gerber"])
		aboutDialog.set_license(license.read())
		aboutDialog.set_website('http://code.google.com/p/gitso')
		aboutDialog.set_website_label('http://code.google.com/p/gitso')
		aboutDialog.set_copyright("2007 Derek Buranen, Aaron Gerber")
		aboutDialog.set_comments("Gitso Is To Support Others")
		license.close()
		aboutDialog.run()
		aboutDialog.destroy()

    
    # Callback: getClipboard
    #               : EVENT - Paste menu item selected
	def getClipboard(self, menu, data=None):
		self.GetSupportEntry.set_text(self.clipboard.wait_for_text())
		return

    
    # Callback: getClipboard
    #               : EVENT - Copy menu item selected
	def setClipboard(self, menu, data=None):
		self.clipboard.set_text(self.GetSupportEntry.get_text())
		return

        
    # Callback: killPID
    #               : EVENT - Stop is pressed or Applications ends
	def killPID(self, data=None):
		if self.returnPID != 0:
			self.connectButton.set_sensitive(True)
			self.stopButton.set_sensitive(False)
			os.kill(self.returnPID, signal.SIGKILL)
			self.statusLabel.set_text(self.statusLabelText[0])
			self.returnPID = 0
		return


    # Callback: deleteEvent
    #               : EVENT - "Close" option is selected - title bar or button
    #               : TODO - Add "Close" button
    #               : TODO - "quit" promt dialog
    #               : TODO - Close VNC connection
	def deleteEvent(self, widget, event, data=None):
        # If you return FALSE in the "deleteEvent" signal handler,
        # GTK will emit the "destroy" signal. Returning TRUE means
        # you don't want the window to be destroyed.
        # This is useful for popping up 'are you sure you want to quit?' dialog
		print "Close Window"
		return False
        
        
    # Callback: destroy
    #               : EVENT - Gtk_widget_destroy() is called on the window, or return FALSE in "deleteEvent"
	def destroy(self, widget, data=None):
		print "Quit Application"
		self.killPID(self)
		gtk.main_quit()

	def get_main_menu(self, window):
		accel_group = gtk.AccelGroup()

		# This function initializes the item factory.
		# Param 1: The type of menu - can be MenuBar, Menu,
		#          or OptionMenu.
		# Param 2: The path of the menu.
		# Param 3: A reference to an AccelGroup. The item factory sets up
		#          the accelerator table while generating menus.
		item_factory = gtk.ItemFactory(gtk.MenuBar, "<main>", accel_group)

		# This method generates the menu items. Pass to the item factory
		#  the list of menu items
		item_factory.create_items(self.menu_items)

		# Attach the new accelerator group to the window.
		window.add_accel_group(accel_group)

		# need to keep a reference to item_factory to prevent its destruction
		self.item_factory = item_factory
		# Finally, return the actual menu bar created by the item factory.
		return item_factory.get_widget("<main>")


    # Run Loop: Initilize program
	def __init__(self):
		#initializing various variables
		self.returnPID = 0
		self.statusLabelText = ('Status: Idle', 'Status: Started')
    	
		# create a new window
		self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		self.window.set_title("Gitso")
		self.window.connect("delete_event", self.deleteEvent)
		self.window.connect("destroy", self.destroy)
		self.window.set_border_width(0)
        
		self.clipboard = gtk.clipboard_get(gtk.gdk.SELECTION_CLIPBOARD)

		self.menu_items = (
			('/_File',            None,         None,        0, '<Branch>' ),
			('/File/Connect',     None,         self.connectSupport, 0, '<StockItem>', gtk.STOCK_CONNECT),
			('/File/_Quit',       '<control>Q', self.destroy, 0, '<StockItem>', gtk.STOCK_QUIT),
			('/_Edit/_Copy',      None,         self.setClipboard, 0, '<StockItem>',gtk.STOCK_COPY),
			('/_Edit/_Paste',     None,         self.getClipboard, 0, '<StockItem>',gtk.STOCK_PASTE),
			('/_Help',            None,         None, 0, '<Branch>'),
			('/Help/_About',      None,         self.showAbout, 0, '<StockItem>',gtk.STOCK_ABOUT),
			)
       	
		self.MenuBar = self.get_main_menu(self.window)

       
		# Initialize IP Textbox
		self.GetSupportEntry = gtk.Entry(50)
		self.GetSupportEntry.set_text("IP address")
		self.GetSupportEntry.show()

		# Initialize Radio Buttons.
		self.GiveSupportRadio = gtk.RadioButton(None, "Give _Support", use_underline=True)
		self.GetSupportRadio  = gtk.RadioButton(self.GiveSupportRadio, "_Get Help", use_underline=True)
        
		self.GiveSupportRadio.connect("toggled", self.radioToggle, "Give _Support")
		self.GetSupportRadio.connect("toggled", self.radioToggle, "_Get Help")
        
		self.GetSupportRadio.set_active(True)
		self.GiveSupportRadio.show()
		self.GetSupportRadio.show()

        
        #### ToDo :: Connect Button -- Default ##########
        #self.button.grab_default()
        ####################################
        # Initialize Connect Button Bar
		self.connectButton = gtk.Button("OK", gtk.STOCK_CONNECT)
		self.connectButton.connect("clicked", self.connectSupport)
		self.connectButton.show()
		self.stopButton = gtk.Button("Stop", gtk.STOCK_STOP)
		self.stopButton.connect("clicked", self.killPID)
		self.stopButton.set_sensitive(False)
		self.stopButton.show()
		self.statusLabel = gtk.Label(self.statusLabelText[0])
		self.statusLabel.show()


        # Initialize Boxes
		self.mainVBox            =  gtk.VBox(False, 0)
		self.interfaceVBox      = gtk.VBox(False, 0)
		self.menuHBox           = gtk.HBox(False, 0)
		self.getSupportHBox  = gtk.HBox(False, 0)
		self.giveSupportHBox = gtk.HBox(False, 0)
		self.buttonHBox          = gtk.HBox(False, 0)


        # VBox MenuBar
		self.menuHBox.pack_start(self.MenuBar, True, True, 0)
		self.mainVBox.pack_start(self.menuHBox, False, False, 0)
		self.MenuBar.show()
        
        # VBox cell 1
		self.getSupportHBox.pack_start(self.GetSupportRadio, True, True, 8)
		self.getSupportHBox.pack_start(self.GetSupportEntry, True, True, 8)
		self.interfaceVBox.pack_start(self.getSupportHBox, True, True, 4)

        # VBox cell 2
		self.giveSupportHBox.pack_start(self.GiveSupportRadio, True, True, 8)
		self.interfaceVBox.pack_start(self.giveSupportHBox, True, True, 0)

        # VBox cell 3
		self.buttonHBox.pack_start(self.statusLabel, False, False, 8)
		self.buttonHBox.pack_end(self.stopButton, False, False, 8)
		self.buttonHBox.pack_end(self.connectButton, False, False, 8)
		self.interfaceVBox.pack_start(self.buttonHBox, False, False, 0)

        # Show main window and initialize focus
		self.GetSupportEntry.grab_focus()
		self.mainVBox.pack_end(self.interfaceVBox, False, False, 8)

		self.mainVBox.show()
		self.interfaceVBox.show()
		self.menuHBox.show()
		self.getSupportHBox.show()
		self.giveSupportHBox.show()
		self.buttonHBox.show()
        
		self.window.add(self.mainVBox)
		self.window.show()

	# Run Loop: Main run loop
	def main(self):
		gtk.main()

# If the program is run directly or passed as an argument to the python
# interpreter then create a "Connect" instance and show it
if __name__ == "__main__":
	hello = Connect()
	hello.main()
