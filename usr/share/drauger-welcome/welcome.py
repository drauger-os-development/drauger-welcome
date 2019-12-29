#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  welcome.py
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
from os import system
from subprocess import Popen
message_show="""
  Thank you again for using Drauger OS. Would you like to uninstall drauger-welcome?
  """

with open("/usr/drauger/os-info.txt") as f:
	s = f.read()
class Menu_tut(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Drauger OS Tutorial")

		self.box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(self.box)

		self.label = Gtk.Label()
		self.label.set_markup(message_show)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.box.pack_start(self.label, True, True, 0)

		self.button1 = Gtk.Button.new_with_label(label="Yes")
		self.button1.connect("clicked", self.onyesclicked)
		self.box.pack_start(self.button1, True, True, 0)

		self.button2 = Gtk.Button.new_with_label(label="No")
		self.button2.connect("clicked", self.onnoclicked)
		self.box.pack_start(self.button2, True, True, 0)

	def onyesclicked(self, widget):
		self.hide()
		Menu_tut.x=0
		return Menu_tut.x

	def onnoclicked(self, widget):
		self.hide()
		Menu_tut.x=1
		return Menu_tut.x

def tutorial_menu():
	window = Menu_tut()
	window.set_decorated(True)
	window.set_resizable(True)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.connect("delete-event", Gtk.main_quit)
	window.show_all()
	Gtk.main()
	return(Menu_tut.x)

class welcome(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Welcome to Drauger OS")
		self.grid=Gtk.Grid(orientation=Gtk.Orientation.VERTICAL,)
		self.add(self.grid)

		self.label = Gtk.Label()
		self.label.set_markup("<b>" + """
Drauger OS %s
 """ % (s) + "</b>")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 2, 1, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup("""
   Welcome and thank you for choosing Drauger OS.
   We hope you'll enjoy gaming on it as much as we did developing it.
   Please make yourself familiar with the new features, layout, and the documentation.
   Please, don't hesitate to send us your feedback, it is greatly appreciated!

   Default Admin Password is: 'toor'
 """)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 2, 4, 1)

		self.label = Gtk.Label()
		self.label.set_markup("""
   Drauger OS website
 """)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 3, 1, 1)

		self.button1 = Gtk.Button.new_from_icon_name("cs-network",3)
		self.button1.connect("clicked", self.onwebclicked)
		self.grid.attach(self.button1, 1, 4, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup("""
   View the README file
 """)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 4, 3, 1, 1)

		self.button2 = Gtk.Button.new_from_icon_name("document",3)
		self.button2.connect("clicked", self.onnextclicked)
		self.grid.attach(self.button2, 4, 4, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup("""
   Take the Drauger OS Tutorial
   (Recommended for new users)
 """)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 5, 1, 1)

		self.button3 = Gtk.Button.new_from_icon_name("dictionary",3)
		self.button3.connect("clicked", self.ontutclicked)
		self.grid.attach(self.button3, 1, 6, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup("""
   Find Help
 """)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 7, 1, 1)

		self.button5 = Gtk.Button.new_from_icon_name("help",3)
		self.button5.connect("clicked", self.onhelpclicked)
		self.grid.attach(self.button5, 1, 8, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup("""
   Additional Drivers
 """)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 4, 7, 1, 1)

		self.button5 = Gtk.Button.new_from_icon_name("jockey",3)
		self.button5.connect("clicked", self.ondriveclicked)
		self.grid.attach(self.button5, 4, 8, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup("""
   Language Support
 """)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 9, 1, 1)

		self.button6 = Gtk.Button.new_from_icon_name("preferences-desktop-locale",3)
		self.button6.connect("clicked", self.onlanguageclicked)
		self.grid.attach(self.button6, 1, 10, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup("""
   Donate
 """)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 4, 9, 2, 1)

		self.button7 = Gtk.Button.new_from_icon_name("money-manager-ex",3)
		self.button7.connect("clicked", self.ondonateclicked)
		self.grid.attach(self.button7, 4, 10, 2, 1)

		self.label = Gtk.Label()
		self.label.set_markup("""
   Keyboard Shortcuts
 """)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 4, 5, 1, 1)

		self.button8 = Gtk.Button.new_from_icon_name("keyboard",3)
		self.button8.connect("clicked", self.onshortcutclicked)
		self.grid.attach(self.button8, 4, 6, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup("""
   Uninstall drauger-welcome
 """)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 4, 11, 2, 1)

		self.button9 = Gtk.Button.new_from_icon_name("delete",3)
		self.button9.connect("clicked", self.onuninstallclicked)
		self.grid.attach(self.button9, 4, 12, 2, 1)

		self.label = Gtk.Label()
		self.label.set_markup("""
	Join the CYGO network and
	Drauger OS Forums
	""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 11, 1, 1)

		self.button10 = Gtk.Button.new_from_icon_name("CYGO",3)
		self.button10.connect("clicked", self.onCYGOclicked)
		self.grid.attach(self.button10, 1, 12, 1, 1)

	def onCYGOclicked(self, button):
		Popen(["/usr/share/drauger-welcome/verifier"])

	def onnextclicked(self, button):
		Popen(["/usr/bin/xdg-open","https://draugeros.org/docs/README.pdf"])

	def onwebclicked(self, button):
		Popen(["/usr/bin/xdg-open","https://draugeros.org/go"])

	def ontutclicked(self,button):
		Popen(["/usr/bin/python3","/usr/share/drauger-welcome/tut.py"])

	def onhelpclicked(self, button):
		Popen(["/usr/bin/xdg-open","https://draugeros.org/go/wiki"])

	def ondriveclicked(self, button):
		Popen(["/usr/bin/software-properties-gtk","--open-tab=4"])

	def onlanguageclicked(self, button):
		Popen(["gnome-language-selector"])

	def ondonateclicked(self, button):
		Popen(["/usr/bin/xdg-open","https://paypal.me/pools/c/89GtByYaTT"])

	def onshortcutclicked(self, button):
		Popen(["/usr/bin/python3","/usr/share/drauger-welcome/shortcuts.py"])

	def onuninstallclicked(self, button):
		#have an uninstall comfirmation dialouge then uninstall based in the answer
		x=tutorial_menu()
		if x==0:
			try:
				system("/usr/share/drauger-welcome/u.sh")
			except:
				system("/usr/share/drauger-welcome/log-out 2 /usr/share/drauger-welcome/welcome.py '/etc/drauger-welcome/u.sh has failed. See error log entry for u.sh for more info.' 'drauger-welcome' 'UNKNOWN' 'UNKNOWN'")

def welcome_show():
	window = welcome()
	window.set_decorated(True)
	window.set_resizable(True)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.connect("delete-event", Gtk.main_quit)
	window.show_all()
	Gtk.main()

try:
	welcome_show()
except:
	system("/usr/share/drauger-welcome/log-out 2 /usr/share/drauger-welcome/welcome.py 'Unknown error. Function welcome_show has failed.' 'drauger-welcome' 'UNKNOWN' 'UNKNOWN'")
