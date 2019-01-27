#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  tut.py
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
from ctypes import cdll, byref, create_string_buffer
from os import system

message_show=""

class notify(Gtk.Window):
	
	def __init__(self):
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
		self.hide()

def notify_show():
	window = notify()
	window.set_decorated(False)
	window.set_resizable(True)
	window.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(1,1,1,1))
	window.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse("black"))
	window.set_opacity(0.0)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.show_all()
	Gtk.main() 
	window.connect("delete-event", Gtk.main_quit)
	
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
        
    def onyesclicked(self, button):
        self.hide()
        Menu_tut.x=0
        return(Menu_tut.x)

    def onnoclicked(self, button):
        self.hide()
        Menu_tut.x=1
        return(Menu_tut.x)

def tutorial_menu():
	window = Menu_tut()
	window.set_decorated(True)
	window.set_resizable(True)
	window.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(1,1,1,1))
	window.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse("black"))
	window.set_opacity(0.0)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.show_all()
	Gtk.main() 
	window.connect("delete-event", Gtk.main_quit)
	return(Menu_tut.x)

message_show="""
  Thank you for downloading and installing Drauger OS, the free, open-sourced, Linux gaming OS.  
  """
notify_show()
message_show="""
  In this tutorial, you will recive a quick introduction into how to work Drauger OS.  
  """
notify_show()
message_show="""
The two bars in the middle of your screen are your desktop panels. 
  The top contains quick access to all the most commonly used apps and widgets.   
The bottom one contains the buttons for the windows you currently have open, as well as
buttons for things such as shuting down, logging out, etc.
"""
notify_show()
message_show="""
  In order to see any apps in the top desktop panel that are not  
  currently on display, simply click on the drop down arrow underneath  
  the icon  
  """
notify_show()
message_show="""
  In order to see any apps not on the top desktop panel, click the Drauger OS Logo
  on the far left of the panel.  
  """
notify_show()
message_show="""
  Drauger OS also has support for not only keyboards and mice,  
  as well as touchpads and touchscreens,  
  it also has support for most Xbox and Xbox 360 controllers,  
  as well as some Playstation controllers. 
  """
notify_show()
message_show="""
  For more info on gamepad support, please go to the command line and run `xboxdrv --help-devices`  
  """
notify_show()
message_show="""
  Finally, the four rectangles on the far right of the top desktop panel are the four current desktops.  
  """
notify_show()
message_show="""
  Would you like to learn more about multiple desktops?  
  """
x=tutorial_menu()
if x==0:
	system("python3 /opt/drauger-welcome/multi_desktop.py")
message_show="""
  Thank you again for using Drauger OS. Would you like to uninstall this tutorial?  
  """
x=tutorial_menu()
if x==0:
	system("/opt/drauger-welcome/u.sh")

