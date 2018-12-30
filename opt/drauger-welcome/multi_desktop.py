#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  tut.py
#  
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
from ctypes import cdll, byref, create_string_buffer

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
		Gtk.main_quit()

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

message_show="""
  Having multiple desktops is the ability to switch back and forth between two "desktops."  
  This ability makes it so that you can hide windows and tabs for apps on one desktop while you work in another.  
  """
notify_show()
message_show="""
  This allows for greater organization, privacy, control,  
  and productivity.  
  """
notify_show()
message_show="""
  To switch from one desktop to another, click on the rectangle that is grey between the two  
  on the far right of the top desktop panel.  
  """
notify_show()
