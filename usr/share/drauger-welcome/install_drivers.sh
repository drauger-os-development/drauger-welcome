#!/bin/bash
# -*- coding: utf-8 -*-
#
#  install_drivers.sh
#  
#  Copyright 2022 Thomas Castleman <contact@draugeros.org>
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

# This is here to install drivers as root for the welcome screen
driver_list="$1"
icon="$2"
cmd="apt-get -y -o Dpkg::Options::='--force-confold' --force-yes install"
for each in $driver_list; do
	if "nvidia-driver-" == "${each:0:14}"; then
		if "nvidia-driver-latest" != "$each"; then
			echo -e "blacklist nouveau\noptions nouveau modeset=0" | tee /etc/modprobe.d/blacklist-nvidia-nouveau.conf
		fi
		break
	fi
done
{
	$cmd $driver_list
} || {
	notify-send -i "$icon" \
				-a "Drauger OS Welcome Screen" \
				"Driver Installation Error" \
				"Installing Drivers Encountered An Error. Please contact support."
	exit 2
}

notify-send -i "$icon" \
			-a "Drauger OS Welcome Screen" \
			"Driver Installation Success" \
			"Drivers Successfully Installed. Please Reboot for changes to take effect."
exit 0
