import sys

SCRIPT = "src\\uniconvertor.py"

sys.argv += ['py2exe', ]

print SCRIPT

from distutils.core import setup
import py2exe

from glob import glob

data_files = [("Microsoft.VC90.CRT", glob(r'C:\Program Files\Microsoft Visual Studio 9.0\VC\redist\x86\Microsoft.VC90.CRT\*.*'))]

INCLUDES = ['os', 'sys']

setup(
    options={'py2exe': {'bundle_files': 2,
        'compressed': True,
        'includes': INCLUDES,
    }},
    console=[SCRIPT,],
    data_files=data_files,
    zipfile=None,
    name="UniConvertor",
    version="2.0",
    description="Universal vector graphics translator",
)