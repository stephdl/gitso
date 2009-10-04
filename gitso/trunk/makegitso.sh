#! /bin/bash

##########
# Gisto - Gitso is to support others
# 
# Copyright 2008, 2009: Aaron Gerber, Derek Buranen
#
# Gitso is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Gitso is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with Gitso.  If not, see <http://www.gnu.org/licenses/>.
##########


DMG="Gitso_0.6.dmg"
DEB="gitso_0.6_all.deb"
TARGZ="gitso_0.6_all.tar.gz"
SRC="gitso_0.6_src.tar.bz2"
RPM="gitso-0.6-1.i586.rpm"
RPMOUT="gitso_0.6-1_opensuse.i586.rpm"

function mksrc {
		P=`pwd`
		TMP_PKG="../pkg"
		rm -rf $TMP_PKG
		mkdir -p $TMP_PKG/trunk/
		cp -r ./ $TMP_PKG/trunk/
 		find $TMP_PKG/trunk -name ".svn" -exec rm -rf {} 2>&1 > /dev/null ';' 2>&1 > /dev/null
		mv $TMP_PKG/trunk $TMP_PKG/gitso-0.6
		tar -cj -C $TMP_PKG/ gitso-0.6 > $P/$SRC
		rm -rf $TMP_PKG
}

CLEAN="yes"
RPMNAME="opensuse"
echo -n "Starting makegitso:"

if [ "$1" = "" ]; then
	echo -n ".."
elif test "$1" = "--no-clean"; then
	CLEAN="no"
elif test "$1" = "--fedora"; then
	RPMNAME="fedora"
	RPMOUT="gitso_0.6-1_fedora.i386.rpm"
elif test "$1" = "--opensuse"; then
	RPMNAME="opensuse"
else
	echo -e "Usage makegitso.sh: [ --no-clean | --fedora | --opensuse | --help ]"
	echo -e "\tOptions:"
	echo -e "\t--no-clean\tDo not remove the build directory."
	echo -e "\t--fedora\tMake Build for Fedora."
	echo -e "\t--opensuse\tMake Build for OpenSUSE."
	echo -e "\t--help  \tThese options."
	exit 0
fi

if [ "$2" = "" ]; then
	echo ".."
elif test "$2" = "--no-clean"; then
	CLEAN="no"
	echo ".."
elif test "$2" = "--fedora"; then
	RPMNAME="fedora"
	RPMOUT="gitso_0.6-1_fedora.i386.rpm"
	echo ".."
elif test "$2" = "--opensuse"; then
	RPMNAME="opensuse"
	echo ".."
else
	echo -e "Usage makegitso.sh: [ --no-clean | --fedora | --opensuse | --help ]"
	echo -e "\tOptions:"
	echo -e "\t--no-clean\tDo not remove the build directory."
	echo -e "\t--help  \tThese options."
	exit 0
fi

if [ "`uname -a | grep Darwin`" != "" ]; then
	if test `which py2applet`; then
		echo -e "Creating Gitso.app "
		rm -f setup.py
		rm -rf dist
		
		# To Make cotvnc
		# cvs -z3 -d:pserver:anonymous@cotvnc.cvs.sourceforge.net:/cvsroot/cotvnc co -P cotvnc
		#
		# cd cotvnc
		# patch -p0 < [Gitso-path]/arch/osx/cotvnc-gitso.diff
		#
		# Then in xCode build cotvnc
		# find build/Development/
		# rename Chicken Of The VNC.app to cotvnc.app
		# remove cotvnc.app/Contents/Resources/*non English.lproj
		# rename cotvnc.app/Contents/MacOS/Chicken Of The VNC to cotvnc.app/Contents/MacOS/cotvnc
		# 
		# Patch was made with: diff -aurr . ../cotvnc-gitso/ > cotvnc-gitso.diff
		#
		
		echo -e ".."
		py2applet --make-setup Gitso.py
		
		echo -e ".."
		
		# To manually include the wx libraries, I'm not sure we need them...
		# python setup.py py2app --includes=wx --packages=wx
		
		python setup.py py2app
		rm setup.py
		
		echo -e ".."
		cp arch/osx/Info.plist dist/Gitso.app/Contents/
		
		cp COPYING dist/Gitso.app/Contents/Resources/
		cp PythonApplet.icns dist/Gitso.app/Contents/Resources/
		
		tar xvfz arch/osx/OSXvnc.tar.gz
		mv OSXvnc dist/Gitso.app/Contents/Resources/

		tar xvfz arch/osx/cotvnc.app.tar.gz
		mv cotvnc.app dist/Gitso.app/Contents/Resources/
		
		cp icon.ico dist/Gitso.app/Contents/Resources/
		cp icon.png dist/Gitso.app/Contents/Resources/
		cp __init__.py dist/Gitso.app/Contents/Resources/
		cp ArgsParser.py dist/Gitso.app/Contents/Resources/
		cp Processes.py dist/Gitso.app/Contents/Resources/
		cp ConnectionWindow.py dist/Gitso.app/Contents/Resources/
		cp AboutWindow.py dist/Gitso.app/Contents/Resources/
		cp GitsoThread.py dist/Gitso.app/Contents/Resources/
		
		cp arch/osx/libjpeg-copyright.txt dist/Gitso.app/Contents/Frameworks/
		cp arch/osx/osxnvc_echoware-copyright.txt dist/Gitso.app/Contents/Resources/OSXvnc/
		cp arch/osx/cotvnc-copyright.txt dist/Gitso.app/Contents/Resources/cotvnc.app/contents/Resources
		cp arch/osx/osxvnc-copyright.txt dist/Gitso.app/Contents/Resources/OSXvnc/
		
		echo -e " [done]\n"
		
		echo -e "Creating Gitso.dmg "
		rm -f $DMG
		
		mkdir dist/Gitso
		cp arch/osx/dmg_DS_Store dist/Gitso/.DS_Store
		ln -s /Applications/ dist/Gitso/Applications
		
		mv "dist/Gitso.app" "dist/Gitso/"
		cp -r arch/osx/Readme.rtfd dist/Gitso/Readme.rtfd
		
		echo -e "..."
		hdiutil create -srcfolder dist/Gitso/ $DMG
		echo -e "... [done]\n"
	else
		echo -e "Error, you need py2applet to be installed."
	fi
	
elif test "`uname -a 2>&1 | grep Linux | grep -v which`"; then
	if test "`which dpkg 2>&1 | grep -v which`"; then
	BUILDPATH="gitso"
	TARGZPATH="Gitso"
	echo -n "Creating $DEB"
	rm -rf $BUILDPATH

	# Deb version of Gitso.
	mkdir -p $BUILDPATH/DEBIAN
	mkdir -p $BUILDPATH/usr/bin
	mkdir -p $BUILDPATH/usr/share/applications
	mkdir -p $BUILDPATH/usr/share/doc/$BUILDPATH
	mkdir -p $BUILDPATH/usr/share/$BUILDPATH
	mkdir -p $BUILDPATH/usr/share/man/man1

	echo -n ".."
	cp arch/linux/control $BUILDPATH/DEBIAN
	cp arch/linux/gitso $BUILDPATH/usr/bin/
	chmod 755 $BUILDPATH/usr/bin/gitso
	cp Gitso.py $BUILDPATH/usr/share/$BUILDPATH/
	cp ConnectionWindow.py $BUILDPATH/usr/share/$BUILDPATH/
	cp AboutWindow.py $BUILDPATH/usr/share/$BUILDPATH/
	cp GitsoThread.py $BUILDPATH/usr/share/$BUILDPATH/
	cp Processes.py $BUILDPATH/usr/share/$BUILDPATH/
	cp ArgsParser.py $BUILDPATH/usr/share/$BUILDPATH/
	cp __init__.py $BUILDPATH/usr/share/$BUILDPATH/
	cp hosts.txt $BUILDPATH/usr/share/$BUILDPATH/
	cp icon.ico $BUILDPATH/usr/share/$BUILDPATH/
	cp icon.png $BUILDPATH/usr/share/$BUILDPATH/

	echo -n ".."
	cp arch/linux/gitso.desktop $BUILDPATH/usr/share/applications/
	cp arch/linux/README.txt $BUILDPATH/usr/share/doc/$BUILDPATH/README
	cp COPYING $BUILDPATH/usr/share/doc/$BUILDPATH/
	gzip -cf arch/linux/changelog > $BUILDPATH/usr/share/doc/$BUILDPATH/changelog.gz
	gzip -cf arch/linux/gitso.1 > $BUILDPATH/usr/share/man/man1/gitso.1.gz

	echo -n ".."
	dpkg -b $BUILDPATH/ $DEB 2>&1 > /dev/null
	
	echo -e " [done]"

	# Standalone version of Gitso.
	echo -n "Creating $TARGZ"
	rm -rf $TARGZPATH
	
	cp -r $BUILDPATH $TARGZPATH
	rm -rf $TARGZPATH/DEBIAN

	echo -n ".."
	cp arch/linux/README-stand-alone.txt $TARGZPATH/README
	cp arch/linux/run-gitso.sh $TARGZPATH/
	mv $TARGZPATH/usr/bin $TARGZPATH/bin
	mv $TARGZPATH/usr/share $TARGZPATH/share
	rm -rf $TARGZPATH/usr/
	
	echo -n "."
	tar -cvzf $TARGZ $TARGZPATH 2>&1 > /dev/null
	
	echo -e " [done]\n"

	echo -n "Creating gitso $SRC...."
	mksrc
	echo -e " [done]\n"


	if [ "$CLEAN" = "yes" ]; then
		rm -rf $BUILDPATH
		rm -rf $TARGZPATH
		find . -name "*.pyc" -exec rm {} ';'
	fi
	elif test "`which rpm 2>&1 | grep -v which`"; then
		if [ "$RPMNAME" = "fedora" ]; then
			SPEC="gitso_rpm_fedora.spec"
			# Before installing the .rpm
			# You need to install http://dl.atrpms.net/all/x11vnc-0.9.3-3.fc9.i386.rpm
			# yum --nogpgcheck install gitso_0.6-1_fedora.i386.rpm 
		else
			SPEC="gitso_rpm.spec"
		fi
		# RPM version of Gitso
		echo "Creating $RPM"
		BUILD_DIR=`pwd`
		export BUILD_DIR="$BUILD_DIR/build"
		TMP="$BUILD_DIR/rpm/tmp"
		BUILD_ROOT="$BUILD_DIR/rpm/tmp/gitso-root"

		mkdir -p $BUILD_DIR/rpm/{BUILD,RPMS/$ARCH,RPMS/noarch,SOURCES,SRPMS,SPECS,tmp}
		mkdir -p $BUILD_ROOT

		mksrc

		cp $SRC $BUILD_DIR/rpm/SOURCES/$SRC

		cp arch/linux/$SPEC $TMP
	  perl -e 's/%\(echo \$HOME\)/$ENV{'BUILD_DIR'}/g;' -pi $TMP/$SPEC

		rpmbuild -ba $TMP/$SPEC
		find $BUILD_DIR/rpm/RPMS -name "*.rpm" -exec cp {} $RPMOUT ';'

		echo -e " [done]\n"
		if [ "$CLEAN" = "yes" ]; then
			rm -rf $BUILD_DIR
			find . -name "*.pyc" -exec rm {} ';'
		fi
	
	fi
fi
