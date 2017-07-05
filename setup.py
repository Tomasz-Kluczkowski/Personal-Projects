import cx_Freeze
import sys
import os.path

PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')

# os.environ['TCL_LIBRARY'] = "K:\\PYTHON\\Python36\\tcl\\tcl8.6"
# os.environ['TK_LIBRARY'] = "K:\\PYTHON\\Python36\\tcl\\tk8.6"


base = None

if sys.platform == "win32":
    base = "Win32GUI"

include_files = ["Database/", "Resources/", "Debug/",
                 os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tk86t.dll'),
                 os.path.join(PYTHON_INSTALL_DIR, 'DLLs', 'tcl86t.dll'),
                 ]
includes = [] # ["weather_backend", "controller"]
excludes = ["PyQt5"]
packages = ["tkinter"]
executables = [cx_Freeze.Executable("weather_gui.py", base=base,
                                    icon="Resources\\Icons\\app_icon.ico")]

cx_Freeze.setup(
    name='Weather App',
    version='1.0',
    description='Weather report application',
    author='Tomasz Kluczkowski',
    author_email='tomaszk1@hotmail.co.uk',
    options={'build_exe': {'includes': includes,
                           'excludes': excludes,
                           'packages': packages,
                           'include_files': include_files}},
    executables=executables)