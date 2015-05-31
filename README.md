# About #
This project is no longer active. If there is interest from the community to continue support, that'd be awesome. But that thus far, has not happened.

## Gitso is to support others. ##

Gitso is a frontend to reverse VNC connections.  It is meant to be a simple two-step process that connects one person to another's screen.  First, the support person offers to give support.  Second, the person who needs help connects and has their screen remotely visible. Because Gitso is cross-platform (Linux, OS X and Windows) and uses a reverse VNC connection, it greatly simplifies the process of getting support.

<table>
<tr>
<td valign='top'>
<h2>Gitso 0.6 (Feb 21, 2010)</h2>
<ul><li>Complete rewrite of processes.<br>
</li><li>Stop VNC Processes (Windows)<br>
</li><li>Support loading remote hosts file.<br>
</li><li>Command line switches<br>
<ul><li>--dev<br>
</li><li>--listen<br>
</li><li>--connect IP<br>
</li><li>--list list_file<br>
</li><li>--version<br>
</li><li>--help<br>
</li></ul></li><li>manpage for (Linux)<br>
</li><li>Support for .rpms<br>
</li><li>Native VNC listener! (OS X)<br>
</li><li>Better process management, user gets notified if connection is broken.<br>
</li><li>Licensing Updates (across the board).<br>
</li><li>Many bug fixes.</li></ul>

<a href='https://github.com/stephdl/gitso/blob/master/wiki/History.wiki'>Release History</a>
</td>
<td valign='top'>
<h2>Downloads</h2>
<a href='https://github.com/stephdl/gitso-download'> See all downloads</a>.<br>
<ul><li>Mac OS X:<br>
<ul><li><a href='https://github.com/stephdl/gitso-download/blob/master/Gitso_0.6_mac_Leopard.dmg'> Gitso 0.6 (10.5 Leopard)</a>.<br>
</li><li><a href='https://github.com/stephdl/gitso-download/blob/master/gitso_0.6_mac_SnowLeopard.dmg'> Gitso 0.6 (10.6 Snow Leopard)</a>.<br>
</li></ul></li><li>Windows:<br>
<ul><li><a href='https://github.com/stephdl/gitso-download/blob/master/gitso_0.6_install.exe'>Gitso 0.6 Windows XP and higher</a>.<br>
</li></ul></li><li>Linux:<br>
<ul><li><a href='https://github.com/stephdl/gitso-download/blob/master/gitso_0.6.2_all.deb'>Gitso 0.6.2 Debian_Ubuntu</a>
</li><li><a href='https://github.com/stephdl/gitso-download/blob/master/gitso_0.6-1_fedora.i386.rpm'>Gitso 0.6 Fedora</a>.<br>
</li><li><a href='https://github.com/stephdl/gitso-download/blob/master/gitso_0.6-1_opensuse.i586.rpm'>Gitso 0.6 OpenSUSE</a>.<br>
</li><li><a href='https://github.com/stephdl/gitso-download/blob/master/gitso_0.6_linux_all.tar.gz'>Gitso 0.6 Platform Independent</a>.<br>
<ul><li>You will need to manually install the following:<br>
<ul><li>x11vnc<br>
</li><li>vncviewer<br>
</li><li>wxPython<br>
</td>
</tr>
</table></li></ul></li></ul></li></ul></li></ul>


Using Gitso <br>
  * <a href='https://github.com/stephdl/gitso/blob/master/wiki/Howto.wiki'> Instructions</a><br>


Building Gitso<br>
  * <a href='https://github.com/stephdl/gitso/blob/master/wiki/Build.wiki'> Instructions</a><br>


Screenshots
<table>
<tr>
<td>
<img src='https://github.com/stephdl/gitso/blob/master/wiki/ScreenshotLinux.png' />
</td>
<td>
<img src='https://github.com/stephdl/gitso/blob/master/wiki/ScreenshotMacOS.png' />
</td>
<td>
<img src='https://github.com/stephdl/gitso/blob/master/wiki/Screenshotwindows.png' />
</td>
</tr>
</table>

## Based On ##
  * OS X
    * [Chicken of the VNC 2.0 b4](http://sourceforge.net/projects/cotvnc/files/cotvnc/Chicken%20of%20the%20VNC%202.0b4/cotvnc-20b4.dmg/download) ([Source](http://sourceforge.net/projects/cotvnc/files/cotvnc/Chicken%20of%20the%20VNC%202.0b4/cotvnc-20b4-source.tgz/download))
    * OS X uses [OSXvnc 3.0](http://sourceforge.net/projects/osxvnc/) ([Source](http://sourceforge.net/project/showfiles.php?group_id=64523))
  * Windows
    * Windows uses [TightVNC 1.3.10](http://www.tightvnc.com/) ([Source](http://downloads.sourceforge.net/vnc-tight/tightvnc-1.3.10_winsrc.tar.bz2))

## Roadmap ##
### 0.8 ###
  * Support for display names, instead of IP only.
  * Enable NatPMP (needs testing)
  * Add localizations (patches exist).
  * Add preferences for low-res/optimizations.
  * Add preferences for SSH Tunneling and ports.
  * Upgrade VNC (Windows --> TightVNC 2.0 && Linux --> vnc4server?)
  * Get Gitso into a Ubuntu repository:
    * https://bugs.launchpad.net/ubuntu/+bug/319444
    * https://wiki.ubuntu.com/PackagingGuide


## Links ##
  * http://podcast.ubuntu-uk.org/?p=157 (~ min 28 - 35)
  * http://tinyapps.org/weblog/misc/200810110700_gitso_remote_support.html
  * http://linuxerie.midiblogs.com/archive/2008/09/25/gisto-passer-les-routeurs-avec-vnc.html
  * http://www.luthi.eu/blog/2008/10/remote-support-made-simple-with-gitso
  * http://mac.softpedia.com/get/Utilities/Gitso.shtml
  * http://ubuntuforums.org/showthread.php?t=1202905
  * http://forum.ultravnc.info/viewtopic.php?t=14092
  * http://www.getdeb.net/software/Gitso
