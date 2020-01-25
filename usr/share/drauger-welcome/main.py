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
message_show_remove="""
  Thank you again for using Drauger OS. Would you like to uninstall drauger-welcome?
  """

message_show_tutorial="""
  Thank you for downloading and installing Drauger OS, the free, open-sourced, Linux gaming OS.
  """

message_show_multi_desktop="""
  Having multiple desktops is the ability to switch back and forth between two "desktops."
  This ability makes it so that you can hide windows and tabs for apps on one desktop while you work in another.
  """

with open("/usr/drauger/os-info.txt") as f:
	s = f.read()

class welcome(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Welcome to Drauger OS")
		self.grid=Gtk.Grid(orientation=Gtk.Orientation.VERTICAL,)
		self.add(self.grid)

		self.reset("clicked")

	def reset(self,button):

		self.clear_window()

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
		self.button3.connect("clicked", self.tutorial)
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
		self.button9.connect("clicked", self.removal_conf)
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

		self.show_all()

	def removal_conf(self, button):

		self.clear_window()

		self.label = Gtk.Label()
		self.label.set_markup(message_show_remove)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 1, 3, 1)

		self.button1 = Gtk.Button.new_with_label(label="Yes")
		self.button1.connect("clicked", self.onuninstallclicked)
		self.grid.attach(self.button1, 1, 2, 1, 1)

		self.button2 = Gtk.Button.new_with_label(label="No")
		self.button2.connect("clicked", self.reset)
		self.grid.attach(self.button2, 3, 2, 1, 1)

		self.show_all()

	def onCYGOclicked(self, button):
		Popen(["/usr/share/drauger-welcome/verifier"])

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
			self.removal_conf("clicked")
		else:
			system("/usr/share/drauger-welcome/log-out 2 /usr/share/drauger-welcome/multi_desktop.py 'Unknown error. Variable self.check in function onnextclicked in class notify outside expected range' 'drauger-welcome' 'UNKNOWN' 'UNKNOWN'")
			exit(2)
		self.check = self.check + 1

	def onwebclicked(self, button):
		Popen(["/usr/bin/xdg-open","https://draugeros.org/go"])

	def onhelpclicked(self, button):
		Popen(["/usr/bin/xdg-open","https://draugeros.org/go/wiki"])

	def ondriveclicked(self, button):
		Popen(["/usr/bin/software-properties-gtk","--open-tab=4"])

	def onlanguageclicked(self, button):
		Popen(["gnome-language-selector"])

	def ondonateclicked(self, button):
		Popen(["/usr/bin/xdg-open","https://paypal.me/pools/c/89GtByYaTT"])

	def onshortcutclicked(self, button):

		self.clear_window()

		self.label = Gtk.Label()
		self.label.set_markup( """
Keyboard Shortcuts for Drauger OS
 """)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 1, 3, 1)

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
		self.grid.attach(self.label, 3, 2, 1, 1)

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
		self.grid.attach(self.label, 3, 3, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
Ctrl+Alt+M
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 4, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
	Launch Audacious
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 3, 4, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
Alt+F
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 5, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
	Launch File Manager
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 3, 5, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
Super L
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 6, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
	Show Application Menu
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 3, 6, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
Ctrl+Alt+L
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 7, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
	Lock Screen
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 3, 7, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
F10
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 8, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
	Toggle Mute
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 3, 8, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
F11
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 9, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
	Lower Volume
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 3, 9, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
F12
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 10, 1, 1)

		self.label = Gtk.Label()
		self.label.set_markup( """
	Increase Volume
""")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 3, 10, 1, 1)

		self.button1 = Gtk.Button.new_with_label(label="<-- Back")
		self.button1.connect("clicked", self.reset)
		self.grid.attach(self.button1, 1, 20, 1, 1)

		self.show_all()

	def onuninstallclicked(self, button):
		#have an uninstall comfirmation dialouge then uninstall based in the answer
		try:
			system("/usr/share/drauger-welcome/u.sh")
		except:
			system("/usr/share/drauger-welcome/log-out 2 /usr/share/drauger-welcome/main.py '/etc/drauger-welcome/u.sh has failed. See error log entry for u.sh for more info.' 'drauger-welcome' 'UNKNOWN' 'UNKNOWN'")

	def onyesclicked(self, button):
		self.onuninstallclicked("clicked")

	def onnoclicked(self, button):
		self.reset("clicked")

	def tutorial(self,button):

		self.clear_window()
		self.check = -1

		self.label = Gtk.Label()
		self.label.set_markup(message_show_tutorial)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 1, 3, 1)

		self.button1 = Gtk.Button.new_with_label(label="Next -->")
		self.button1.connect("clicked", self.onclicked)
		self.grid.attach(self.button1, 3, 2, 1, 1)

		self.button2 = Gtk.Button.new_with_label(label="<-- Previous")
		self.button2.connect("clicked", self.onclicked)
		self.grid.attach(self.button2, 1, 2, 1, 1)

		self.button3 = Gtk.Button.new_with_label(label="EXIT TUTORIAL")
		self.button3.connect("clicked", self.reset)
		self.grid.attach(self.button3, 2, 2, 1, 1)

		self.show_all()

	def onclicked(self, button):
		if (button.get_label() == "Next -->"):
			self.check = self.check + 1
		elif (button.get_label() == "<-- Previous"):
			self.check = self.check - 1
		if self.check == -1:
			self.label.set_text("""
  Thank you for downloading and installing Drauger OS, the free, open-sourced, Linux gaming OS.
  """)
		elif self.check == 0:
			self.label.set_text("""
  In this tutorial, you will recive a quick introduction into how to work Drauger OS.
  """)
		elif self.check == 1:
			self.label.set_text("""
The two bars in the middle of your screen are your desktop panels.
  The top contains quick access to all the most commonly used apps and widgets.
The bottom one contains the buttons for the windows you currently have open, as well as
buttons for things such as shuting down, logging out, etc.
""")
		elif self.check == 2:
			self.label.set_text("""
  In order to see any apps in the top desktop panel that are not
  currently on display, simply click on the drop down arrow underneath
  the icon
  """)
		elif self.check == 3:
			self.label.set_text("""
  In order to see any apps not on the top desktop panel, click the Drauger OS Logo
  on the far left of the panel.
  """)
		elif self.check == 4:
			self.label.set_text("""
  Drauger OS also has support for not only keyboards and mice,
  as well as touchpads and touchscreens,
  it also has support for most Xbox and Xbox 360 controllers,
  as well as some Playstation controllers.
  """)
		elif self.check == 5:
			self.label.set_text("""
  For more info on gamepad support, please go to the command line and run `xboxdrv --help-devices`
  """)
		elif self.check == 6:
			self.label.set_text("""
  Finally, the four rectangles on the far right of the top desktop panel are the four current desktops.
  """)
		elif self.check == 7:
			self.label.set_markup("""
  If you wish to learn more about how to use the Drauger OS desktop, please visit:
  <a href="https://www.draugeros.org/go/wiki/basics-of-the-drauger-os-desktop/"> https://www.draugeros.org/go/wiki/basics-of-the-drauger-os-desktop/ </a>
  """)
		elif self.check == 8:
			self.multi_desktop("clicked")

	def multi_desktop(self,button):

		self.clear_window()

		self.label = Gtk.Label()
		self.label.set_markup("""
  Would you like to learn more about multiple desktops?
  """)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 1, 3, 1)

		self.button1 = Gtk.Button.new_with_label(label="Yes")
		self.button1.connect("clicked", self.onmultiyesclicked)
		self.grid.attach(self.button1, 1, 2, 1, 1)

		self.button2 = Gtk.Button.new_with_label(label="No")
		self.button2.connect("clicked", self.onmultinoclicked)
		self.grid.attach(self.button2, 3, 2, 1, 1)

		self.show_all()

	def onmultiyesclicked(self, button):
		self.clear_window()
		self.check = 0

		self.label = Gtk.Label()
		self.label.set_markup(message_show_multi_desktop)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 1, 3, 1)

		self.button1 = Gtk.Button.new_with_label(label="Next")
		self.button1.connect("clicked", self.onnextclicked)
		self.grid.attach(self.button1, 3, 2, 1, 1)

		self.show_all()

	def onmultinoclicked(self, button):
		self.removal_conf("clicked")

	def exit(self,button):
		Gtk.main_quit("delete-event")
		print(1)
		exit(1)

	def clear_window(self):
		children = self.grid.get_children()
		for each in children:
			self.grid.remove(each)

def welcome_show():
	window = welcome()
	window.set_decorated(True)
	window.set_resizable(False)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.connect("delete-event", welcome.exit)
	window.show_all()
	Gtk.main()

try:
	welcome_show()
except:
	system("/usr/share/drauger-welcome/log-out 2 /usr/share/drauger-welcome/welcome.py 'Unknown error. Function welcome_show has failed.' 'drauger-welcome' 'UNKNOWN' 'UNKNOWN'")