# -*- coding: utf-8 -*-
#
#	Copyright (C) 2015 by Igor E. Novikov
#
#	This program is free software: you can redistribute it and/or modify
#	it under the terms of the GNU General Public License as published by
#	the Free Software Foundation, either version 3 of the License, or
#	(at your option) any later version.
#
#	This program is distributed in the hope that it will be useful,
#	but WITHOUT ANY WARRANTY; without even the implied warranty of
#	MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#	GNU General Public License for more details.
#
#	You should have received a copy of the GNU General Public License
#	along with this program.  If not, see <http://www.gnu.org/licenses/>.

CPL12 = '\xdd\xdc'
CPL8 = '\xdc\xdc'

CPLdd = '\xcd\xdd'#?
CPLdc = '\xcd\xdc',#?
CPLbc = '\xcd\xbc',#?

CPL7 = '\xcc\xdc'
CPL6 = '\xcc\xbc'

CPL_IDs = [CPL12, CPL8, CPL7, CPL6]


CDR_COLOR_SPOT = 1
CDR_COLOR_CMYK = 2
CDR_COLOR_CMYK255 = 3
CDR_COLOR_CMY = 4
CDR_COLOR_BGR = 5
CDR_COLOR_HSB = 6
CDR_COLOR_HLS = 7
CDR_COLOR_BW = 8
CDR_COLOR_GRAY = 9
#=10
CDR_COLOR_YIQ = 11
CDR_COLOR_LAB = 12
#=13
#=14
CDR_COLOR_HEXACHROME = 15
#=16
CDR_COLOR_CMYK2 = 17
CDR_COLOR_LAB2 = 18
#=19
CDR_COLOR_REGISTRATION = 20
CDR_COLOR_SPOT2 = 21

CDR_COLOR_NAMES = {
CDR_COLOR_SPOT:'SPOT',#?
CDR_COLOR_CMYK:'CMYK',
CDR_COLOR_CMYK255:'CMYK255',
CDR_COLOR_CMY:'CMY',
CDR_COLOR_BGR:'BGR',
CDR_COLOR_HSB:'HSB',
CDR_COLOR_HLS:'HLS',
CDR_COLOR_BW:'B&W',#?
CDR_COLOR_GRAY:'GRAY',
CDR_COLOR_YIQ:'YIQ',
CDR_COLOR_LAB:'LAB',
CDR_COLOR_HEXACHROME:'HEXACHROME',
CDR_COLOR_CMYK2:'CMYK255',
CDR_COLOR_LAB2:'LAB2',
CDR_COLOR_REGISTRATION:'REGISTRATION',#?
CDR_COLOR_SPOT2:'SPOT2',#?
}

CDR_COLOR_SIZE = {
CDR_COLOR_SPOT:3,#?
CDR_COLOR_CMYK:4,
CDR_COLOR_CMYK255:4,
CDR_COLOR_CMY:3,
CDR_COLOR_BGR:3,
CDR_COLOR_HSB:4,
CDR_COLOR_HLS:4,
CDR_COLOR_BW:1,#?
CDR_COLOR_GRAY:1,
CDR_COLOR_YIQ:3,
CDR_COLOR_LAB:3,
CDR_COLOR_HEXACHROME:6,
CDR_COLOR_CMYK2:4,
CDR_COLOR_LAB2:3,
CDR_COLOR_REGISTRATION:0,#?
CDR_COLOR_SPOT2:3,#?
}