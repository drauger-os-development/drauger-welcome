#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  shortcuts.py
#  
#  Copyright 2019 Thomas Castleman <draugeros@gmail.com>
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
from gi.repository import Gtk, Gdk, Pango

class main_window(Gtk.Window):
	
	def __init__(self):
		Gtk.Window.__init__(self, title="Drauger OS Keyboard Shortcuts")
		self.grid=Gtk.Grid(orientation=Gtk.Orientation.VERTICAL,)
		self.add(self.grid)

		self.label = Gtk.Label()
		self.label.set_markup( """
Keyboard Shortcuts for Drauger OS
 """)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 1, 2, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
Ctrl+Alt+T
 """)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 2, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
Open Terminal
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 2, 2, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
Ctrl+Alt+F
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 3, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
	Toggle Full Screen on an App
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 2, 3, 1, 1)

		self.button1 = Gtk.Button.new_with_label(label="<-- Back")
		self.button1.connect("clicked", self.onbackclicked)
		self.grid.attach(self.button1, 2, 20, 1, 1)

	def onbackclicked(self, button):
		self.hide()
		exit()

def show_shortcuts():
	window = main_window()
	window.set_decorated(True)
	window.set_resizable(True)
	window.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(1,1,1,1))
	window.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse("black"))
	window.set_opacity(0.0)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.show_all()
	Gtk.main() 
	window.connect("delete-event", Gtk.main_quit)

show_shortcuts()