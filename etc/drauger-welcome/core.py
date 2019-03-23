#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  core.py
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
		system("/usr/bin/python3 /etc/drauger-welcome/tut.py")
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
		system( /etc/drauger-welcome/u.sh")
		notify_show()
		exit(1)
	elif g==2:
		#notify of exit and keep
		print("exit")
		system("/bin/echo '1' >> $HOME/.drauger-tut")
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
