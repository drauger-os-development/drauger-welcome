#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  core.py
#  

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, Pango
from ctypes import cdll, byref, create_string_buffer
from os import system
from time import sleep

class Menu_tut_init(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Drauger OS Tutorial")
        
        self.box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)
        
        self.label = Gtk.Label()
        self.label.set_markup("""<b>
    Thank you for downloading and installing Drauger OS! Would you like the tutorial to show you around?    
    </b>""")
        self.label.set_justify(Gtk.Justification.CENTER)
        self.box.pack_start(self.label, True, True, 0)
        
        self.button1 = Gtk.Button.new_with_label(label="Yes")
        self.button1.connect("clicked", self.onyesclicked)
        self.box.pack_start(self.button1, True, True, 0)
        
        self.button2 = Gtk.Button.new_with_label(label="No")
        self.button2.connect("clicked", self.onnoclicked)
        self.box.pack_start(self.button2, True, True, 0)
        
    def onyesclicked(self, button):
        Gtk.main_quit()
        Menu_tut_init.x=0
        return(Menu_tut_init.x)

    def onnoclicked(self, button):
        Gtk.main_quit()
        Menu_tut_init.x=1
        return(Menu_tut_init.x)

def tutorial_init():
	window = Menu_tut_init()
	window.set_decorated(True)
	window.set_resizable(True)
	window.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(1,1,1,1))
	window.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse("black"))
	window.set_opacity(0.0)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.show_all()
	Gtk.main() 
	window.connect("delete-event", Gtk.main_quit)
	return(Menu_tut_init.x)
	 
class Menu_tut_abort(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Drauger OS Tutorial")
        
        self.box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(self.box)
        
        self.label = Gtk.Label()
        self.label.set_markup("""<b>    Are you sure you do not want to take the tutorial? 
Drauger OS can be confusing if this is your first time. If you do not want to take the tutorial, 
then you may uninstall it to help save space, or save it for later.    
        </b>""")
        self.label.set_justify(Gtk.Justification.CENTER)
        self.box.pack_start(self.label, True, True, 0)
        
        self.button1 = Gtk.Button.new_with_label(label="Yes, but leave it for later.")
        self.button1.connect("clicked", self.onyes_keepclicked)
        self.box.pack_start(self.button1, True, True, 0)
        
        self.button1 = Gtk.Button.new_with_label(label="Yes, and uninstall the tutorial.")
        self.button1.connect("clicked", self.onyes_delclicked)
        self.box.pack_start(self.button1, True, True, 0)
        
        self.button2 = Gtk.Button.new_with_label(label="No, I changed my mind.")
        self.button2.connect("clicked", self.onnoclicked)
        self.box.pack_start(self.button2, True, True, 0)
        
    def onyes_delclicked(self, button):
        Menu_tut_abort.x=1
        Gtk.main_quit()
        return(Menu_tut_abort.x)
    
    def onyes_keepclicked(self, button):
        Menu_tut_abort.x=2
        Gtk.main_quit()
        return(Menu_tut_abort.x)

    def onnoclicked(self, button):
        Menu_tut_abort.x=3
        Gtk.main_quit()
        return(Menu_tut_abort.x)

def tutorial_abort():
	window = Menu_tut_abort()
	window.set_decorated(True)
	window.set_resizable(True)
	window.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(1,1,1,1))
	window.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse("black"))
	window.set_opacity(0.0)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.show_all()
	Gtk.main() 
	window.connect("delete-event", Gtk.main_quit)
	return(Menu_tut_abort.x)  

class error(Gtk.Window):
	
	def __init__(self):
		Gtk.Window.__init__(self, title="Drauger OS Tutorial")
		self.box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(self.box)
		
		self.label = Gtk.Label()
		self.label.set_markup("<b>We are sorry. Drauger OS Tutorial has experienced an error. Exiting...</b>")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.box.pack_start(self.label, True, True, 0)
		
		self.button1 = Gtk.Button.new_with_label(label="Exit")
		self.button1.connect("clicked", self.onexitclicked)
		self.box.pack_start(self.button1, True, True, 0)
        
	def onexitclicked(self, button):
		Gtk.main_quit()

def error_show():
	window = error()
	window.set_decorated(True)
	window.set_resizable(True)
	window.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(1,1,1,1))
	window.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse("black"))
	window.set_opacity(0.0)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.show_all()
	Gtk.main() 
	window.connect("delete-event", Gtk.main_quit)

class notify(Gtk.Window):
	
	def __init__(self):
		Gtk.Window.__init__(self, title="Drauger OS Tutorial")
		self.box=Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
		self.add(self.box)
		
		self.label = Gtk.Label()
		self.label.set_markup("<b>Tutorial Uninstalled</b>")
		self.label.set_justify(Gtk.Justification.CENTER)
		self.box.pack_start(self.label, True, True, 0)
		
		self.button1 = Gtk.Button.new_with_label(label="Exit")
		self.button1.connect("clicked", self.onexitclicked)
		self.box.pack_start(self.button1, True, True, 0)
        
	def onexitclicked(self, button):
		Gtk.main_quit()

def notify_show():
	window = notify()
	window.set_decorated(True)
	window.set_resizable(True)
	window.override_background_color(Gtk.StateType.NORMAL, Gdk.RGBA(1,1,1,1))
	window.modify_fg(Gtk.StateFlags.NORMAL, Gdk.color_parse("black"))
	window.set_opacity(0.0)
	window.set_position(Gtk.WindowPosition.CENTER)
	window.show_all()
	Gtk.main() 
	window.connect("delete-event", Gtk.main_quit)
		        
def menu():
	c=tutorial_init()
	back=c
	if c==0:
		#run tutorial
		system("python3 /opt/drauger-welcome/tut.py")
	elif c==1:
		g=tutorial_abort()
		menu2(g)
	else:
		#error dialoge
		error_show()
		exit(2)

def menu2(g):
	if g==1:
		#get password
		print("uninstall and exit")
		system("/opt/drauger-welcome/u.sh")
		notify_show()
		exit(1)
	elif g==2:
		#notify of exit and keep
		print("exit")
		system("echo '1' >> $HOME/.drauger-tut")
		exit(0)
	elif g==3:
		#run opening again and loop
		print("loop")
		menu()
	else:
		#error dialoge
		error_show()
		print("error1")
		exit(2)

menu()
