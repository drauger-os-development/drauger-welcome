#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  tut.py
#  
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
from ctypes import cdll, byref, create_string_buffer

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
		self.check=self.check+1

def notify_show():
	window = notify()
	window.set_decorated(False)
	window.set_resizable(True)
	window.set_opacity(0.0)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.show_all()
	Gtk.main() 
	window.connect("delete-event", Gtk.main_quit)

notify_show()
