#!/bin/sh
# -*- coding: utf-8 -*-
#
#  tut.sh
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
if [ ! -e "$HOME"/.drauger-tut ]; then
	if [ $(/usr/bin/pgrep Systemback && /bin/echo "True" || /bin/echo "False") == "True" ]; then
		exit 2
	else
		/usr/bin/touch $HOME/.drauger-tut || /etc/drauger-welcome/log-out 2 /etc/drauger-welcome/tut.sh "Could not make $HOME/.drauger-tut Please check file permissions." "drauger-welcome" "$PWD" "$0"
		( /usr/bin/python3 /etc/drauger-welcome/welcome.py || /etc/drauger-welcome/log-out.sh 2 /etc/drauger-welcome/tut.sh 'Unknown error. welcome.py has failed. Check error logs for more info.' ) &
		( /bin/bash $HOME/.dxvk/setup.sh || /etc/drauger-welcome/log-out 2 /etc/drauger-welcome/tut.sh 'Unknown error. Variable c in function menu outside expected range' "drauger-welcome" "$PWD" "$0" ) &
		
	fi
else
	exit 2
fi
