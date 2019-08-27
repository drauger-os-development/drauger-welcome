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
from os import system

message_show="""
  Thank you for downloading and installing Drauger OS, the free, open-sourced, Linux gaming OS.  
  """

class Menu_tut1(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Drauger OS Tutorial")

		self.box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(self.box)

		self.label = Gtk.Label()
		self.label.set_markup("""
  Would you like to learn more about multiple desktops?  
  """)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.box.pack_start(self.label, True, True, 0)

		self.button1 = Gtk.Button.new_with_label(label="Yes")
		self.button1.connect("clicked", self.onyesclicked)
		self.box.pack_start(self.button1, True, True, 0)

		self.button2 = Gtk.Button.new_with_label(label="No")
		self.button2.connect("clicked", self.onnoclicked)
		self.box.pack_start(self.button2, True, True, 0)

	def onyesclicked(self, button):
		self.hide()
		system("/usr/bin/python3 /etc/drauger-welcome/multi_desktop.py")
		tutorial_menu2()
		
	def onnoclicked(self, button):
		self.hide()
		tutorial_menu2()
		
class Menu_tut2(Gtk.Window):

	def __init__(self):
		Gtk.Window.__init__(self, title="Drauger OS Tutorial")

		self.box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(self.box)

		self.label = Gtk.Label()
		self.label.set_markup("""
  Thank you again for using Drauger OS. Would you like to uninstall this tutorial?  
  """)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.box.pack_start(self.label, True, True, 0)

		self.button1 = Gtk.Button.new_with_label(label="Yes")
		self.button1.connect("clicked", self.onyesclicked)
		self.box.pack_start(self.button1, True, True, 0)

		self.button2 = Gtk.Button.new_with_label(label="No")
		self.button2.connect("clicked", self.onnoclicked)
		self.box.pack_start(self.button2, True, True, 0)

	def onyesclicked(self, button):
		self.hide()
		system("/etc/drauger-welcome/u.sh")
		exit()

	def onnoclicked(self, button):
		self.hide()
		exit()

def tutorial_menu1():
	window = Menu_tut1()
	window.set_decorated(True)
	window.set_resizable(True)
	window.set_opacity(0.0)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.show_all()
	Gtk.main() 
	window.connect("delete-event", Gtk.main_quit)
	
def tutorial_menu2():
	window = Menu_tut2()
	window.set_decorated(True)
	window.set_resizable(True)
	window.set_opacity(0.0)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.show_all()
	Gtk.main() 
	window.connect("delete-event", Gtk.main_quit)
	
class notify(Gtk.Window):
	
	def __init__(self):
		self.check = -1 
		Gtk.Window.__init__(self, title="Drauger OS Tutorial")
		self.grid = Gtk.Grid(orientation=Gtk.Orientation.VERTICAL,)
		self.add(self.grid)
		
		self.label = Gtk.Label()
		self.label.set_markup(message_show)
		self.label.set_justify(Gtk.Justification.CENTER)
		self.grid.attach(self.label, 1, 1, 3, 1)
		
		self.button1 = Gtk.Button.new_with_label(label="Next -->")
		self.button1.connect("clicked", self.onclicked)
		self.grid.attach(self.button1, 3, 2, 1, 1)
		
		self.button2 = Gtk.Button.new_with_label(label="<-- Previous")
		self.button2.connect("clicked", self.onclicked)
		self.grid.attach(self.button2, 1, 2, 1, 1)
		
		self.button3 = Gtk.Button.new_with_label(label="EXIT TUTORIAL")
		self.button3.connect("clicked", self.onexit)
		self.grid.attach(self.button3, 2, 2, 1, 1)
		
	def onexit(self, button):
		Gtk.main_quit()
		print("User requested tutorial abort.")
		exit(1)
			
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
			self.hide()
			tutorial_menu1()
			
def notify_show():
	window = notify()
	window.set_decorated(True)
	window.set_resizable(True)
	window.set_opacity(0.0)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.show_all()
	Gtk.main() 
	window.connect("delete-event", Gtk.main_quit)

try:
	notify_show()
except:
	from os import system
	system("/etc/drauger-welcome/log-out 2 /etc/drauger-welcome/tut.py 'Unknown error. Function notify_show failed' 'drauger-welcome' 'UNKNOWN' 'UNKNOWN'")
	exit(2)
