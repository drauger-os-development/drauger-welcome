#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  tut.py
#
#  Copyright 2019 Thomas Castleman <contact@draugeros.org>
#
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#
#
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

message_show="""
  Having multiple desktops is the ability to switch back and forth between two "desktops."
  This ability makes it so that you can hide windows and tabs for apps on one desktop while you work in another.
  """

class notify(Gtk.Window):

	def __init__(self):
		self.check=0
		Gtk.Window.__init__(self, title="Drauger OS Tutorial")
		self.box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(self.box)

		self.label = Gtk.Label()
		self.label.set_markup(message_show)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.box.pack_start(self.label, True, True, 0)

		self.button1 = Gtk.Button.new_with_label(label="Next")
		self.button1.connect("clicked", self.onnextclicked)
		self.box.pack_start(self.button1, True, True, 0)

	def onnextclicked(self, button):
		if self.check == 0:
			self.label.set_text("""
  This allows for greater organization, privacy, control,
  and productivity.
  """)
		elif self.check == 1:
			self.label.set_text("""
  To switch from one desktop to another, click on the rectangle that is grey between the two
  on the far right of the top desktop panel.
  """)
		elif self.check == 2:
			self.hide()
			exit()
		else:
			from os import system
			system("/etc/drauger-welcome/log-out 2 /etc/drauger-welcome/multi_desktop.py 'Unknown error. Variable self.check in function onnextclicked in class notify outside expected range' 'drauger-welcome' 'UNKNOWN' 'UNKNOWN'")
			exit(2)
		self.check=self.check+1

def notify_show():
	window = notify()
	window.set_decorated(False)
	window.set_resizable(True)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.connect("delete-event", Gtk.main_quit)
	window.show_all()
	Gtk.main()

try:
	notify_show()
except:
	from os import system
	system("/etc/drauger-welcome/log-out 2 /etc/drauger-welcome/multi_desktop.py 'Unknown error. Function notify_show failed. 'drauger-welcome' 'UNKNOWN' 'UNKNOWN'")
