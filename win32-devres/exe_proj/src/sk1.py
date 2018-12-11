#! /usr/bin/python
#
#     Copyright (C) 2016-2018 by Igor E. Novikov
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import sys

RESTRICTED = ('UniConvertor', 'Python', 'ImageMagick')


def get_path_var():
    paths = os.environ["PATH"].split(os.pathsep)

    def check_path(path):
        for item in RESTRICTED:
            if item in path:
                return False
        return True

    return os.pathsep.join([path for path in paths if check_path(path)])


cur_path = os.path.dirname(sys.executable)
if not cur_path or not os.path.exists(cur_path):
    cur_path = os.getcwd()

sys.path.insert(0, os.path.join(cur_path, 'libs'))
sys.path.insert(0, os.path.join(cur_path, 'stdlib'))

bindir = os.path.join(cur_path, 'dlls') + os.pathsep
magickdir = os.path.join(cur_path, 'dlls', 'modules') + os.pathsep

os.environ["PATH"] = magickdir + bindir + get_path_var()
# ImageMagick non-ascii path issue fix
magickdir = magickdir.decode(sys.getfilesystemencoding()).encode('utf-8')
os.environ["MAGICK_CODER_MODULE_PATH"] = magickdir
os.environ["MAGICK_CODER_FILTER_PATH"] = magickdir
os.environ["MAGICK_CONFIGURE_PATH"] = magickdir
os.environ["MAGICK_HOME"] = magickdir

for item in range(1, len(sys.argv)):
    if not os.path.dirname(sys.argv[item]):
        sys.argv[item] = os.path.join(os.getcwd(), sys.argv[item])

os.chdir(os.path.join(cur_path, 'dlls'))

import sk1

sk1.sk1_run()
