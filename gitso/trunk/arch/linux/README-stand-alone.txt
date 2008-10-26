Gitso is to support others.

We created Gitso as a frontend to reverse VNC connections. It is meant
to be a simple two-step process that connects one person to another's
screen. First, the support person offers to give support. Second, the
person who needs help connects and has their screen remotely visible.
Because Gitso is cross-platform (Ubuntu, OS X and Windows) and uses a
reverse VNC connection, it greatly simplifies the process of getting support.


Gitso 0.5: "Kill the Undead". (September 5, 2008)

    * Complete rewrite of the interface to wxWidgets (from GTK).
    * Gitso no longer has Zombied VNC processes after it quits.
    * Gitso stops the VNC process when it closes (OS X & Linux)
    * Updated Icon
    * Updated License: GPL 3
    * Added Support to specify a list of hosts when you distribute it.
    * Added History/Clear History of servers
    * Added OS X 10.5 Support (needs testing on 10.4 and 10.3)
          o OS X uses TightVNC 1.3.9 (Source)
          o OS X uses OSXvnc 3.0 (Source) 
    * Added Windows XP Support
          o Windows uses TightVNC 1.3.9 (Source)

+++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Gitso Distro-independent Code.

Note: If you run Ubuntu, it'd be easier to use gitso_0.5_all.deb. However,
if you aren't running Ubuntu proceed.

Requirements:
	x11vnc
	vncviewer
	wxPython

Usage: ./run-gitso.sh [options]
	Options:
	--have-wxpython:	Disable wxPython library check


