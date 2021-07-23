#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  tut.py
#
#  Copyright 2021 Thomas Castleman <contact@draugeros.org>
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
from __future__ import print_function
from sys import stderr
from os import path, getenv
from subprocess import Popen
import main_ui

# Make it easier for us to print to stderr
def eprint(*args, **kwargs):
	print(*args, file=stderr, **kwargs)

HOME = getenv("HOME")
# check if system-installer will be running, if it is, do not show the welcome screen
with open("/proc/cmdline", "r") as cmdline_file:
            cmdline = cmdline_file.read()[:-1].split(" ")
if "system-installer" in cmdline:
            # Not wanted to be running ootb
            sys.exit(0)
if ((not path.exists(HOME + "/.drauger-tut")) and (not path.exists("/etc/system-installer/oem-post-install.flag"))):
	try:
		main_ui.welcome_show()
	except Exception as e:
		Popen("/usr/share/drauger-welcome/log-out 2 /usr/share/drauger-welcome/tut.py \"Error: %s . main_ui.py has failed.\"" % (e))
else:
	exit(2)
