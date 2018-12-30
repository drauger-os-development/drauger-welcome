#!/bin/sh
# -*- coding: utf-8 -*-
#
#  u.sh
#  
#  Copyright 2018 Thomas Castleman <draugeros@gmail.com>
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
( pkexec apt -y purge drauger-welcome | zenity --progress --pulsate --auto-close --no-cancel --text="Removing drauger-welcome . . ." && notify-send "drauger-welcome has been removed" ) || zenity --error --no-wrap --text=zenity --error --no-wrap --text="An error was encountered removing drauger-welcome. Error code $? was thrown from apt.\nPlease run \"sudo apt purge drauger-welcome\" in a terminal in order to remove it."
