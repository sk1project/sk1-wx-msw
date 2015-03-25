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

import wal

from sk1 import _, config
from sk1.resources import icons

from generic import PrefPanel

class GeneralPrefs(PrefPanel):

	pid = 'General'
	name = _('General')
	title = _('General application preferences')
	icon_id = icons.PD_PROPERTIES

	def __init__(self, app, dlg, fmt_config=None):
		PrefPanel.__init__(self, app, dlg)

	def build(self):
		title = _('Create new document on start')
		self.newdoc_check = wal.Checkbox(self, title, config.new_doc_on_start)
		self.pack(self.newdoc_check, fill=True, padding=5)

		self.built = True

	def apply_changes(self):
		config.new_doc_on_start = self.newdoc_check.get_value()

	def restore_defaults(self):
		defaults = config.get_defaults()
		self.newdoc_check.set_value(defaults['new_doc_on_start'])
