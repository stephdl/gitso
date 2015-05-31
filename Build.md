If you are just curious about using Gitso, there is no need to build it from Source. Please see the [Downloads Page](http://code.google.com/p/gitso/downloads/list).

If you're interested in digging around in the code or submitting a patch, I'd recommend grabbing a snapshot from [SVN](http://code.google.com/p/gitso/source/checkout).
Patches are definitely welcome! However, if you want to create a specialized build for yourself, I'd recomment download the [latest stable version of the source](http://gitso.googlecode.com/files/gitso_0.6_src.tar.bz2).

## Instructions: ##
  * [Mac OS X](BuildOSX.md)
  * [Windows](BuildWin32.md)
  * [Linux (Ubuntu, Fedora, OpenSUSE)](BuildLinux.md)

## How it Works ##
Using Python and wxWidgets, Gitso utilizes other applications for the actual VNC work:

  * Getting support relies on x11vnc -connect (varies per platform).
  * Giving support relies on vncviewer -listen (varies per platform).

## Command line options ##
There are a number of command line switches that Gitso supports.
  * **--dev** This should be used when calling gitso from the source. This enables the code to look in the appropriate place for various assets.
  * **--listen** Gitso will start and automatically listen for connections (AKA give support)..
  * **--connect IP** Gitso will start and automatically try to connect to the IP address.
  * **--list list\_file** Gitso will look to this external list, can be local or via HTTP for the hosts lists. Ex: You could add a list to your web server so every time the user connected with this option, they would get an up-to-date support list from your server.
    * **list\_file** Should be something like http://www.myserver.com/path/to/support_ips.txt
    * **support\_ips.txt** Should be a comma separated list of IP's. These will then show up in the menu of support IP addresses in Gitso.
  * **--version** Show the current release of Gitso.
  * **--help** Show these options.