import sys

SCRIPT = "src\\sk1.py"

if len(sys.argv) == 1:
    sys.argv += ['py2exe', ]
elif len(sys.argv) == 2:
    sys.argv[1] = 'py2exe'
    SCRIPT = "src\\sk1_portable.py"

print SCRIPT

from distutils.core import setup
import py2exe

from glob import glob

data_files = [("Microsoft.VC90.CRT", glob(r'C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]

INCLUDES = ['os', 'sys']

setup(
    options={'py2exe': {'bundle_files': 3,
        'compressed': True,
        'includes': INCLUDES,
    }},
    windows=[{'script': SCRIPT,
        "icon_resources": [(1, "src\\sk1.ico")]
    }],
    data_files=data_files,
    zipfile=None,
    name="sK1",
    version="2.0RC3",
    description="Vector graphics editor",
)
