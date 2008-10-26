#! /bin/bash

if [ "$1" = "" ]; then
	CLEAN="yes"
elif test "$1" = "--no-clean"; then
	CLEAN="no"
else
	echo -e "Usage makegitso.sh: [ --no-clean | --help ]"
	echo -e "\tOptions:"
	echo -e "\t--no-clean\tDo not remove the build directory."
	echo -e "\t--help  \tThese options."
	exit 0
fi

if test `uname -a | grep Darwin`; then
	if test `which py2applet`; then
		echo -e "Creating Gitso.app "
		rm -f setup.py
		rm -rf dist
		
		echo -e ".."
		py2applet --make-setup Gitso.py
		
		echo -e ".."
		python setup.py py2app
		
		echo -e ".."
		cp arch/osx/Info.plist dist/Gitso.app/Contents/
		cp copyright dist/Gitso.app/Contents/Resources/
		cp PythonApplet.icns dist/Gitso.app/Contents/Resources/
		
		tar xvfz arch/osx/OSXvnc.tar.gz
		mv OSXvnc dist/Gitso.app/Contents/Resources/

		tar xvfz arch/osx/vncviewer.tar.gz
		mv vncviewer dist/Gitso.app/Contents/Resources/
		echo -e " [done]\n"
		
		echo -e "Creating Gitso.dmg "
		rm -f Gitso.dmg
		
		mkdir dist/Gitso
		cp arch/osx/dmg_DS_Store dist/Gitso/.DS_Store
		ln -s /Applications/ dist/Gitso/Applications
		
		mv "dist/Gitso.app" "dist/Gitso/"
		cp -r arch/osx/Readme.rtfd dist/Gitso/Readme.rtfd
		
		echo -e "..."
		hdiutil create -srcfolder dist/Gitso/ Gitso.dmg
		echo -e "... [done]\n"
	else
		echo -e "Error, you need py2applet to be installed."
	fi
	
elif test "`uname -a 2>&1 | grep Linux | grep -v which`"; then
	DEB="gitso_0.6_all.deb"
	TARGZ="gitso_0.6_all.tar.gz"
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
	cp copyright $BUILDPATH/usr/share/doc/$BUILDPATH/
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

	if [ "$CLEAN" = "yes" ]; then
		rm -rf $BUILDPATH
		rm -rf $TARGZPATH
		find . -name "*.pyc" -exec rm {} ';'
	fi

fi
