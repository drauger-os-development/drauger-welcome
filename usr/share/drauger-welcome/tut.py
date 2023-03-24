#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  tut.py
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
from __future__ import print_function
import sys
from os import path, getenv
import subprocess
import urllib3
import drauger_welcome.main_ui as main_ui
import drauger_welcome.alerts as alerts


# Make it easier for us to print to stderr
def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def get_support(url):
    """Check for support with the central EOL designation file"""
    # get data
    data = url.request("GET",
                       "https://download-optimizer.draugeros.org/docs/EOL.txt")
    data = data.data.decode().split("\n")
    # filter comments
    for each in range(len(data) - 1, -1, -1):
        if data[each] == "":
            del data[each]
        elif data[each][0] == "#":
            del data[each]
    # parse remaining data
    for each in enumerate(data):
        data[each[0]] = each[1].split(" - ")
    data = dict(data)
    return data


def get_release():
    """Get Drauger OS release"""
    # first source
    with open("/usr/drauger/os-info.txt", "r") as file:
        data_1 = file.read()
    if data_1[-1] == "\n":
        data_1 = data_1[:-1].split(" ")[0]
    # second source
    data_2 = subprocess.check_output(["lsb_release", "-rs"]).decode()[:-1]
    # third source
    with open("/etc/os-release", "r") as file:
        data_3 = file.read().split("\n")
    data_3 = [each for each in data_3 if "VERSION" in each]
    data_3 = dict([each.split("=") for each in data_3])
    data_3 = data_3["VERSION_ID"].strip("\"")
    # check to see if sources agree
    if data_1 in (data_2, data_3):
        return data_1
    if data_2 == data_3:
        return data_2
    return "UNKNOWN"


def has_support(url):
    """Check to see if the current release has support
    0: has support
    1: Support ending soon
    2: No support, upgrading possible
    3: No support, available to download
    4: No support, cannot download
    """
    try:
        support_policy = get_support(url)
    except urllib3.exceptions.MaxRetryError:
        return 0
    release = get_release()
    if release == "UNKNOWN":
        return 4
    try:
        support_policy = support_policy[release]
    except (KeyError, IndexError):
        return 0
    if support_policy == "AEL":
        return 1
    if support_policy == "EWR":
        return 2
    if support_policy == "EBA":
        return 3
    return 4


HOME = getenv("HOME")
http = urllib3.PoolManager()
support_status = has_support(http)
# check if system-installer will be running, if it is, do not show the welcome screen
with open("/proc/cmdline", "r") as cmdline_file:
    cmdline = cmdline_file.read()
if "system-installer" in cmdline:
    # Not wanted to be running ootb
    if support_status == 2:
        # notify of lack of support
        alerts.post_alert("No Longer Supported", f"""<b>WARNING</b>
Your current version of Drauger OS ({ get_release() }) is no
longer supported. In order to remedy this, please upgrade to
the next version by run these commands in a terminal:

<tt>
sudo apt update
sudo apt install drauger-upgrade-script
upgrade-drauger
</tt>
""")
    elif support_status == 3:
        alerts.post_alert("No Longer Supported, Upgrade No Longer Available", f"""<b>WARNING</b>
Your current version of Drauger OS ({ get_release() }) is no
longer supported, and upgrading to the next version must be
done manually, or you must install a new OS.

You have been warned.
""")
    elif support_status == 4:
        alerts.post_alert("Extremely Old Release", f"""<b>WARNING</b>
Your current version of Drauger OS ({ get_release() }) is extremely old
and no longer supported. No updates are available. Upgrading is extremely
risky, as is continuing to run this version of Drauger OS.

Here be dragons. Proceed at your own peril.
<b>You have been warned.</b>
""")
    elif support_status == 1:
        post_alert("Support Ending Soon", """<b>NOTICE</b>
Your current version of Drauger OS (7.6) is going to
be losing support soon. In order to avoid this, and upgrade to the
new version, please run these commands in a terminal at your
earliest convenience:

<tt>
sudo apt update
sudo apt install drauger-upgrade-script
upgrade-drauger
</tt>
""")
    sys.exit(0)
if ((not path.exists(HOME + "/.drauger-tut")) and (not path.exists("/etc/system-installer/oem-post-install.flag"))):
    try:
        main_ui.welcome_show()
    except Exception as e:
        subprocess.Popen("/usr/share/drauger-welcome/log-out 2 /usr/share/drauger-welcome/tut.py \"Error: %s . main_ui.py has failed.\"" % (e))
# Notify of lack of support
if support_status == 2:
    # notify of lack of support
    alerts.post_alert("No Longer Supported", f"""<b>WARNING</b>
Your current version of Drauger OS ({ get_release() }) is no
longer supported. In order to remedy this, please upgrade to
the next version by run these commands in a terminal:

<tt>
sudo apt update
sudo apt install drauger-upgrade-script
upgrade-drauger
</tt>
""")
elif support_status == 3:
    alerts.post_alert("\tNo Longer Supported, Upgrade No Longer Available\t", f"""<b>WARNING</b>
Your current version of Drauger OS ({ get_release() }) is no
longer supported, and upgrading to the next version must be
done manually, or you must install a new OS.

You have been warned.
""")
elif support_status == 4:
    alerts.post_alert("Extremely Old Release", f"""<b>WARNING</b>
Your current version of Drauger OS ({ get_release() }) is extremely old
and no longer supported. No updates are available. Upgrading is extremely
risky, as is continuing to run this version of Drauger OS.

Here be dragons. Proceed at your own peril.
<b>You have been warned.</b>
""")
elif support_status == 1:
    alerts.post_alert("Support Ending Soon", """<b>NOTICE</b>
Your current version of Drauger OS (7.6) is going to
be losing support soon. In order to avoid this, and upgrade to the
new version, please run these commands in a terminal at your
earliest convenience:

<tt>
sudo apt update
sudo apt install drauger-upgrade-script
upgrade-drauger
</tt>
""")
