# -*- coding: utf-8 -*-
#
#  Setup script for sK1 2.x on MS Windows
#
#  Copyright (C) 2016-2018 by Ihor E. Novikov
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

"""
Usage:
--------------------------------------------------------------------------
 to build package:	   python setup-sk1-msw.py build
--------------------------------------------------------------------------
 to create portable distribution:   python setup-sk1-msw.py bdist_portable
--------------------------------------------------------------------------
 to create MSI distribution:   python setup-sk1-msw.py bdist_msi
--------------------------------------------------------------------------
 Help on available distribution formats: --help-formats
"""

import datetime
import os
import platform
import shutil
import sys
from zipfile import ZIP_DEFLATED

sys.path.insert(0, '../sk1-wx')

import utils
from utils import fsutils, build

sys.path.insert(1, os.path.abspath('../sk1-wx/src'))

from uniconvertor import appconst


def get_os_prefix():
    if platform.architecture()[0] == '32bit':
        return 'win32'
    return 'win64'


def get_res_path():
    return get_os_prefix() + '-devres'


def get_build_suffix():
    if platform.architecture()[0] == '32bit':
        return '.win32-2.7'
    return '.win-amd64-2.7'


def is_64bit():
    return get_build_suffix() == '.win-amd64-2.7'


# Upload 64bit environment variables
if is_64bit():
    exec compile('envs=' + open('amd64.json', 'rb').read(), '<string>', 'exec')
    os.environ.update(envs)

############################################################
# Flags
############################################################
UPDATE_MODULES = False
PORTABLE_PACKAGE = False
MSI_PACKAGE = False
CLEAR_BUILD = False

############################################################
# Package description
############################################################
NAME = appconst.APPNAME
VERSION = appconst.VERSION + appconst.REVISION
DESCRIPTION = 'Vector graphics editor for prepress'
AUTHOR = 'Ihor E. Novikov'
AUTHOR_EMAIL = 'sk1.project.org@gmail.com'
MAINTAINER = AUTHOR
MAINTAINER_EMAIL = AUTHOR_EMAIL
LICENSE = 'GPL v3'
URL = 'https://sk1project.net'
DOWNLOAD_URL = URL
CLASSIFIERS = [
    'Development Status :: 5 - Stable',
    'Environment :: Desktop',
    'Intended Audience :: End Users/Desktop',
    'License :: OSI Approved :: LGPL v2',
    'License :: OSI Approved :: GPL v3',
    'Operating System :: POSIX',
    'Operating System :: MacOS :: MacOS X',
    'Operating System :: Microsoft :: Windows',
    'Programming Language :: Python',
    'Programming Language :: C',
    "Topic :: Multimedia :: Graphics :: Editors :: Vector-Based",
]
LONG_DESCRIPTION = '''
sK1 is an open source vector graphics editor similar to CorelDRAW, 
Adobe Illustrator, or Freehand. First of all sK1 is oriented for prepress 
industry, therefore works with CMYK colorspace and produces CMYK-based PDF 
and postscript output.
sK1 Project (https://sk1project.net),
Copyright (C) 2004-%s by Ihor E. Novikov 
''' % str(datetime.date.today().year)

############################################################
# Build data
############################################################
src_path = '../sk1-wx/src'
res_path = get_res_path()
include_path = os.path.join(res_path, 'include')
lib_path = [os.path.join(res_path, 'libs'), ]
modules = []

dirs = utils.fsutils.get_dirs_tree('../sk1-wx/src/sk1/share')
share_dirs = []
for item in dirs:
    path = item.split('/sk1/')[1]
    share_dirs.append(os.path.join(path, '*.*'))

package_data = {
    'sk1': share_dirs,
}

EXCLUDES = ['sword', ]

############################################################
# Main build procedure
############################################################

if len(sys.argv) == 1:
    print 'Please specify build options!'
    print __doc__
    sys.exit(0)

if len(sys.argv) > 1:
    if sys.argv[1] == 'bdist_portable':
        PORTABLE_PACKAGE = True
        CLEAR_BUILD = True
        sys.argv[1] = 'build'

    elif sys.argv[1] == 'bdist_msi':
        MSI_PACKAGE = True
        CLEAR_BUILD = True
        sys.argv[1] = 'build'

    elif sys.argv[1] == 'build_update':
        UPDATE_MODULES = True
        CLEAR_BUILD = True
        sys.argv[1] = 'build'

data_files = scripts = []

############################################################
# Native extensions
############################################################
from native_mods import make_modules

modules += make_modules(src_path, include_path, lib_path)

############################################################
# Setup routine
############################################################
from distutils.core import setup

abs_path = os.path.abspath(src_path)

setup(
    name=NAME,
    version=VERSION,
    description=DESCRIPTION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    maintainer=MAINTAINER,
    maintainer_email=MAINTAINER_EMAIL,
    license=LICENSE,
    url=URL,
    download_url=DOWNLOAD_URL,
    long_description=LONG_DESCRIPTION,
    classifiers=CLASSIFIERS,
    packages=build.get_source_structure(abs_path, excludes=EXCLUDES),
    package_dir=build.get_package_dirs(abs_path, excludes=EXCLUDES),
    package_data=package_data,
    data_files=data_files,
    scripts=scripts,
    ext_modules=modules)

############################################################
# .py source compiling
############################################################
if not UPDATE_MODULES:
    build.compile_sources()

############################################################
# This section for developing purpose only
# Command 'python setup.py build_update' allows
# automating build and native extension copying
# into package directory
############################################################
if UPDATE_MODULES:
    build.copy_modules(modules, src_path)

############################################################
# Implementation of bdist_portable command
############################################################
if PORTABLE_PACKAGE:
    print 40 * '#'
    print 'PORTABLE_PACKAGE'
    print 40 * '#'
    PKGS = ['sk1', 'uc2', 'wal']
    portable_name = '%s-%s-%s-portable' % (NAME, VERSION, get_os_prefix())
    libdir = os.path.join('build', 'lib' + get_build_suffix())

    os.mkdir(portable_name)

    from zipfile import ZipFile

    portable = os.path.join(get_res_path(), 'portable.zip')
    print 'Extracting', portable
    ZipFile(portable, 'r').extractall(portable_name)
    portable_libs = os.path.join(portable_name, 'libs')
    for item in PKGS:
        src = os.path.join(libdir, item)
        print 'Copying tree', src
        shutil.copytree(src, os.path.join(portable_libs, item))

    if not os.path.isdir('dist'):
        os.mkdir('dist')
    portable = os.path.join('dist', portable_name + '.zip')
    ziph = ZipFile(portable, 'w', ZIP_DEFLATED)

    for root, dirs, files in os.walk(portable_name):
        for item in files:
            if item[-3:] == '.py':
                continue
            path = os.path.join(root, item)
            print 'Compressing', path
            ziph.write(path)
    ziph.close()
    shutil.rmtree(portable_name, True)

############################################################
# Implementation of bdist_msi command
############################################################
if MSI_PACKAGE:
    print 40 * '#'
    print 'MSI_PACKAGE'
    print 40 * '#'
    PKGS = ['sk1', 'uc2', 'wal']
    msi_dir_name = 'msi_build'
    libdir = os.path.join('build', 'lib' + get_build_suffix())
    if os.path.exists(msi_dir_name):
        shutil.rmtree(msi_dir_name, True)
    if os.path.exists('out'):
        shutil.rmtree('out', True)

    os.mkdir(msi_dir_name)

    from zipfile import ZipFile

    portable = os.path.join(get_res_path(), 'portable.zip')
    print 'Extracting', portable
    ZipFile(portable, 'r').extractall(msi_dir_name)

    os.remove(os.path.join(msi_dir_name, 'sk1.exe'))
    exe_file = os.path.join(get_res_path(), 'sk1_msi.zip')
    print 'Extracting', exe_file
    ZipFile(exe_file, 'r').extractall(msi_dir_name)

    msi_libs = os.path.join(msi_dir_name, 'libs')
    for item in PKGS:
        src = os.path.join(libdir, item)
        print 'Copying tree', src
        shutil.copytree(src, os.path.join(msi_libs, item))

    for root, dirs, files in os.walk(msi_dir_name):
        for item in files:
            if item[-3:] == '.py':
                os.remove(os.path.join(root, item))

    mm_name = 'sk1.mm'
    if is_64bit():
        mm_name = 'sk1_x64.mm'
    os.system('mm.cmd %s P' % mm_name)

    src_msi = os.path.join('out', mm_name, 'MSI', 'sk1.msi')
    if not os.path.isfile(src_msi):
        sys.exit(1)

    shutil.rmtree(msi_dir_name, True)
    if not os.path.isdir('dist'):
        os.mkdir('dist')
    msi_name = '%s-%s-%s.msi' % (NAME, VERSION, get_os_prefix())
    dst_msi = os.path.join('dist', msi_name)

    shutil.copy(src_msi, dst_msi)
    shutil.rmtree('out', True)

if CLEAR_BUILD:
    build.clear_msw_build()
