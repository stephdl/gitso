from distutils.core import setup
import py2exe
import urllib
OPTIONS = {'argv_emulation': True}

setup(name="Gitso",
  windows=["Gitso.py"],
  py_modules = ['AboutWindow', 'ConnectionWindow', 'ArgsParser', 'GitsoThread', 'Processes'],
)


