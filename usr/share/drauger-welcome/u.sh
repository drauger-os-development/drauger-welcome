#!/bin/bash
# -*- coding: utf-8 -*-
#
#  u.sh
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
function translate ()
{
	VAR="$1"
	CONCAT_1="$2"
	CONCAT_2="$3"
	if [ -d /etc/drauger-locales/"${LANG//.UTF-8/}" ]; then
		FILE=$(grep -v '^#' /etc/drauger-locales/"${LANG//.UTF-8/}"/drauger-welcome.conf)
	else
		FILE="None"
	fi
	if [ "$VAR" == "uninst_notify" ] && [ "$FILE" == "None" ]; then
		uninst_notify="drauger-welcome has been removed"
		return "$uninst_notify"
	elif [ "$VAR" == "uninst_notify" ]; then
		uninst_notify=$(echo "$FILE" | grep "^uninst_notify" | awk -F '"' '{print $2}')
		return "$uninst_notify"
	fi
	if [ "$VAR" == "remove" ] && [ "$FILE" == "None" ]; then
		remove="Removing drauger-welcome . . ."
		return "$remove"
	elif [ "$VAR" == "remove" ]; then
		remove=$(echo "$FILE" | grep "^remove" | awk -F '"' '{print $2}')
		return "$remove"
	fi
	if [ "$VAR" == "error_uninst" ] && [ "$FILE" == "None" ]; then
		error_uninst="An error was encountered removing drauger-welcome. Error code $CONCAT_1 was thrown from apt.\nPlease run 'sudo apt purge drauger-welcome' in a terminal in order to remove it."
		return "$error_uninst"
	elif [ "$VAR" == "error_uninst" ]; then
		error_uninst=$(echo "$FILE" | grep "^error_uninst" | awk -F '"' '{print $2}' | sed "s/\$error/$CONCAT_1/")
		return "$error_uninst"
	fi

}
{
	/usr/bin/pkexec /usr/bin/apt -y purge drauger-welcome | /usr/bin/zenity --progress --pulsate --auto-close --no-cancel --text=$(translate "remove")
	/usr/bin/notify-send --icon="/usr/share/icons/Drauger/scalable/menus/drauger_os-logo.svg" --app-name="Drauger Welcome" $(translate "uninst_notify")
	exit 0
} || {
	error="$?"
	/usr/bin/zenity --error --no-wrap --text=$(translate "error_uninst" $error)
	/usr/share/drauger-welcome/log-out "$error" /usr/share/drauger-welcome/u.sh "apt has throw an error on de-install. Usually a package has been configured wrong and apt is struggling to recover." "drauger-installer" "$PWD" "$0"
	exit 2
}
