from distutils.core import setup
import py2exe

setup(name="Gitso",
  windows=["Gitso.py"],
  data_files=[(".",
    ["icon.ico"])],
)
