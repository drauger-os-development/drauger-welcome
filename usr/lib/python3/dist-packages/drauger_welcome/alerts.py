#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  alerts.py
#
#  Copyright 2023 Thomas Castleman <contact@draugeros.org>
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
"""Explain what this program does here!!!"""
from __future__ import print_function
import sys
import json
import os
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


def __eprint__(*args, **kwargs):
    """Make it easier for us to print to stderr"""
    print(*args, file=sys.stderr, **kwargs)


if sys.version_info[0] == 2:
    __eprint__("Please run with Python 3 as Python 2 is End-of-Life.")
    exit(2)


class Alert(Gtk.Window):
    """Alert window"""
    def __init__(self, window_title, message, msg_type):
        """Initialize Window"""
        Gtk.Window.__init__(self, title=window_title)
        self.grid = Gtk.Grid(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.grid)
        self.icon = "/usr/share/icons/Drauger/scalable/menus/drauger_os-logo.svg"
        self.set_icon_from_file(self.icon)

        self.HOME = os.getenv("HOME")
        with open(f"{ self.HOME }/.config/drauger-welcome/no-show.json",
                  "r") as file:
            self.show_settings = json.load(file)

        self.msg_type = msg_type

        self.reset(window_title, message)

    def reset(self, window_title, message):
        """Create Window contents"""
        label = Gtk.Label()
        label.set_markup(f"<b>{ window_title }</b>")
        label.set_justify(Gtk.Justification.CENTER)
        label = self._set_default_margins(label)
        self.grid.attach(label, 1, 1, 8, 1)

        label1 = Gtk.Label()
        label1.set_markup(message)
        label1.set_justify(Gtk.Justification.CENTER)
        label1 = self._set_default_margins(label1)
        self.grid.attach(label1, 1, 2, 8, 1)

        start_up = Gtk.CheckButton.new_with_label("Do not show this alert again")
        start_up.set_active(not self.show_settings[self.msg_type])
        start_up.connect("toggled", self.start_up_toggle)
        start_up = self._set_default_margins(start_up)
        self.grid.attach(start_up, 1, 3, 2, 1)

        button = Gtk.Button.new_with_label("Close")
        button.connect("clicked", self.exit)
        button = self._set_default_margins(button)
        self.grid.attach(button, 8, 3, 1, 1)

    def start_up_toggle(self, widget):
        """Control whether to show this alert or not"""
        active = not widget.get_active()
        self.show_settings[self.msg_type] = active
        with open(f"{ self.HOME }/.config/drauger-welcome/no-show.json",
                  "w") as file:
            json.dump(self.show_settings, file, indent=2)
        with open(f"{ self.HOME }/.config/drauger-welcome/no-show.json",
                  "r") as file:
            self.show_settings = json.load(file)

    def _set_default_margins(self, widget):
        """Set default margin size"""
        widget.set_margin_start(10)
        widget.set_margin_end(10)
        widget.set_margin_top(10)
        widget.set_margin_bottom(10)
        return widget

    def exit(self, button):
        """Exit"""
        Gtk.main_quit("delete-event")
        self.destroy()
        self.data = 1
        return 1


def post_alert(title, message, msg_type):
    window = Alert(title, message, msg_type)
    window.set_decorated(False)
    window.set_resizable(False)
    window.set_position(Gtk.WindowPosition.CENTER)
    window.connect("delete-event", Alert.exit)
    window.show_all()
    Gtk.main()
