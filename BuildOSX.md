### Build Gitso ###
  1. Install Developer Tools (Xcode) from the OS X System CD
  1. Install [py2app](http://pypi.python.org/pypi/py2app/)
    * From the command line type:
      * curl -O http://peak.telecommunity.com/dist/ez_setup.py
      * sudo python ez\_setup.py -U setuptools
      * sudo easy\_install -U py2app
  1. From within the src directory:
  1. Update hosts.txt to have preset options for the client. Hosts are comma separated and optional.
  1. Run:./makegitso.pl --> Gitso.dmg

### Notes ###
  1. If you get a python gdb error try typing the following at the command line:
    * defaults write com.apple.versioner.python Prefer-32-Bit -bool yes