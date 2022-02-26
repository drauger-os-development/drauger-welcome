#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main_ui.py
#
#  Copyright 2022 Thomas Castleman <contact@draugeros.org>
#  Additional contributors: Logan L Johnson <logan@cygo.network>
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
import os
import subprocess
import json
import shlex
import apt

LANG = os.getenv("LANG").split(".")
LANG = LANG[0]

try:
    try:
        with open("/etc/drauger-locales/%s/drauger-installer.conf" % (LANG),
                  "r") as FILE:
            contents = FILE.read()
        contents = contents.split("\n")
        for each in range(len(contents)):
            contents[each] = list(contents[each])
        for length in range(len(contents) - 1, -1, -1):
            if ((contents[length] == []) or (contents[length][0] == "#")):
                del(contents[length])
        for each in range(len(contents)):
            contents[each] = "".join(contents[each])
    except FileNotFoundError:
        with open("/etc/drauger-locales/%s/drauger-installer.json" % (LANG),
                  "r") as FILE:
            contents = json.read(FILE)
        if "data" in contents.keys():
            contents = contents["data"]
    for each in contents:
        if type(contents) == dict:
            each = [each, contents[each]]
        if (each[0] == "message_show_remove"):
            message_show_remove = each[1]
        elif (each[0] == "message_show_tutorial"):
            message_show_tutorial = each[1]
        elif (each[0] == "message_show_multi_desktop"):
            message_show_multi_desktop = each[1]
        elif (each[0] == "welcome"):
            welcome_label = each[1]
        elif (each[0] == "website"):
            website = each[1]
        elif (each[0] == "README"):
            README = each[1]
        elif (each[0] == "tutorial_label"):
            tutorial_label = each[1]
        elif (each[0] == "help_button"):
            help_button = each[1]
        elif (each[0] == "drivers"):
            drivers = each[1]
        elif (each[0] == "lang_sup"):
            lang_sup = each[1]
        elif (each[0] == "donate"):
            donate = each[1]
        elif (each[0] == "shortcuts"):
            shortcuts = each[1]
        elif (each[0] == "uninstall"):
            uninstall = each[1]
        elif (each[0] == "CYGO"):
            CYGO = each[1]
        elif (each[0] == "start_up_label"):
            start_up_label = each[1]
        elif (each[0] == "YES"):
            YES = each[1]
        elif (each[0] == "NO"):
            NO = each[1]
        elif (each[0] == "lang_sup2"):
            lang_sup2 = each[1]
        elif (each[0] == "font"):
            font = each[1]
        elif (each[0] == "Back"):
            Back = each[1]
        elif (each[0] == "access_label"):
            access_label = each[1]
        elif (each[0] == "multi_0"):
            multi_0 = each[1]
        elif (each[0] == "multi_1"):
            multi_1 = each[1]
        elif (each[0] == "HELP"):
            HELP = each[1]
        elif (each[0] == "help_yourself"):
            help_yourself = each[1]
        elif (each[0] == "TITLE_sc"):
            TITLE_sc = each[1]
        elif (each[0] == "sc_0"):
            sc_0 = each[1]
        elif (each[0] == "sc_1"):
            sc_1 = each[1]
        elif (each[0] == "sc_2"):
            sc_2 = each[1]
        elif (each[0] == "sc_3"):
            sc_3 = each[1]
        elif (each[0] == "sc_4"):
            sc_4 = each[1]
        elif (each[0] == "sc_5"):
            sc_5 = each[1]
        elif (each[0] == "Next"):
            Next = each[1]
        elif (each[0] == "Exit"):
            Exit = each[1]
        elif (each[0] == "tut_0"):
            tut_0 = each[1]
        elif (each[0] == "tut_1"):
            tut_1 = each[1]
        elif (each[0] == "tut_2"):
            tut_2 = each[1]
        elif (each[0] == "tut_3"):
            tut_3 = each[1]
        elif (each[0] == "tut_4"):
            tut_4 = each[1]
        elif (each[0] == "tut_5"):
            tut_5 = each[1]
        elif (each[0] == "multi_ask"):
            multi_ask = each[1]
        elif (each[0] == "lang_sup3"):
            lang_sup3 = each[1]
        elif (each[0] == "lang_sup4"):
            lang_sup4 = each[1]

except FileNotFoundError:
    message_show_remove = "\n\tThank you again for using Drauger OS. Would you like to uninstall drauger-welcome?\t\n"
    message_show_tutorial = """
\tThank you for downloading and installing Drauger OS, the free Linux gaming OS.\t

\tIn this tutorial, you will recive a quick introduction regarding how to work Drauger OS.\t
"""
    message_show_multi_desktop = "Having multiple desktops is the ability to switch back and forth between two 'desktops'.\n\tThis ability enables you to hide windows and tabs for apps on one desktop while you work in another.\t\n"
    welcome_label = "Welcome! <b>Thank you for choosing Drauger OS.</b>\n\tWe hope you'll enjoy gaming on it as much as we enjoyed developing it.\n\tPlease make yourself familiar with the new features, layout, and documentation.\n\tPlease, don't hesitate to send us your feedback, it's greatly appreciated!\n\n\tThe default admin password is <b>'toor'.</b>"
    website = "\n\tDrauger OS website\t\n"
    README = "\n\tView the README file\t\n"
    tutorial_label = "\n\tTake the Drauger OS Tutorial\t\n\t(Recommended for new users)\t\n"
    help_button = "\n\tFind Help\t\n"
    drivers = "\n\tAdditional Drivers\t\n"
    lang_sup = "\n\tAccessibility Settings\t\n"
    donate = "\n\tDonate\t\n"
    shortcuts = "\n\tKeyboard Shortcuts\t\n"
    uninstall = "\n\tUninstall drauger-welcome\t\n"
    start_up_label = "Show at start up"
    YES = "Yes"
    NO = "No"
    lang_sup2 = "\n\t\tLanguage Support\t\t\n"
    font = "\n\t\tFont Settings\t\t\n"
    Back = "<-- Back"
    access_label = "\t\tSystem Accessibility Settings\t\t"
    multi_0 = "\n\tThis allows for greater organization, privacy, control,\t\n\tand productivity.\t"
    multi_1 = "\n\tTo switch from one desktop to another, click on any of the rectangles at the bottom of the screen,\t\n\tor, hit Ctrl+Alt+Right to move right and Ctrl+Alt+Left to move left.\t\n"
    HELP = "\t\nIf you can't find a solution, let us know using one\t\n\tof these methods, and we will try our best to assist!\t\n"
    help_yourself = "\n\tIf you are having a problem, try checking our wiki, or other online\t\n\tsources for a solution to it\t\n"
    TITLE_sc = "\n\tKeyboard shortcuts for Drauger OS\t\n"
    sc_0 = "\n\tOpen Terminal\t\n"
    sc_1 = "\n\tToggle Full Screen on an App\t\n"
    sc_2 = "\n\tLaunch Audacious\t\n"
    sc_3 = "\n\tLaunch File Manager\t\n"
    sc_4 = "\n\tShow Application Menu\t\n"
    sc_5 = "\n\tLock Screen\t\n"
    Next = "Next -->"
    Exit = "Exit"
    tut_1 = """
\tThe bars on the top, left, and bottom of your screen are your desktop panels.\t
"""
    tut_2 = """
\tThis top bar provides the applications menu (the Drauger OS logo), clock, and power menu (accessed by clicking your username)\t
"""
    tut_3 = """
\tThis left bar contains links, or launchers, for Steam, Firefox, and the Software Center.\t
\tAlso, under the launchers for Steam and the Software Center, the arrows pointing to your right open sub-menus.\t
\tThese allow you quicker access to other, related, apps.\t
"""
    tut_4 = """
\tFinally, this bottom panel provides you with a quick view of what is on each virtual desktop,\t
\tas well as the ability to switch between them using your mouse.\t

\tMore on virtual desktops later.\t
"""
    tut_5 = """
\tIf you wish to learn more about how to use the Drauger OS desktop, please visit:
\t<a href="https://draugeros.org/go/wiki/basics-of-the-drauger-os-desktop/"> https://draugeros.org/go/wiki/basics-of-the-drauger-os-desktop/ </a>
\t"""
    multi_ask = "\n\tWould you like to learn more about multiple desktops?\t\n"
    lang_sup3 = "\n\tInstall locale packages.\t\n"
    lang_sup4 = "\n\tMulti-lingual support settings.\t\n"
    Open = "Open"


HOME = os.getenv("HOME")
if (not os.path.exists("%s/.drauger-tut" % (HOME))):
    show_at_start_up = True
else:
    show_at_start_up = False

try:
    with open("/usr/drauger/os-info.txt") as f:
        s = f.read()
except Exception:
    s = "TEST"

class welcome(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Welcome to Drauger OS")
        self.grid = Gtk.Grid(orientation=Gtk.Orientation.VERTICAL)
        self.add(self.grid)
        self.icon = "/usr/share/icons/Drauger/scalable/menus/drauger_os-logo.svg"
        self.set_icon_from_file(self.icon)

        self.drivers = []
        self.reset("clicked")



    def reset(self, button):

        global show_at_start_up

        self.clear_window()

        self.label = Gtk.Label()
        self.label.set_markup("<b>" + """
Drauger OS %s
 """ % (s) + "</b>")
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 1, 1, 8, 1)

        self.label = Gtk.Label()
        self.label.set_markup(welcome_label)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 1, 2, 8, 1)

        self.label1 = Gtk.Label()
        self.label1.set_markup(website)
        self.label1.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label1, 1, 3, 1, 1)

        self.button1 = Gtk.Button.new_from_icon_name("cs-network", 3)
        self.button1.connect("clicked", self.onwebclicked)
        self.grid.attach(self.button1, 1, 4, 1, 1)

        self.label2 = Gtk.Label()
        self.label2.set_markup(README)
        self.label2.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label2, 6, 3, 1, 1)

        self.button2 = Gtk.Button.new_from_icon_name("document", 3)
        self.button2.connect("clicked", self.show_readme)
        self.grid.attach(self.button2, 6, 4, 1, 1)

        self.label3 = Gtk.Label()
        self.label3.set_markup(tutorial_label)
        self.label3.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label3, 1, 5, 1, 1)

        self.button3 = Gtk.Button.new_from_icon_name("dictionary", 3)
        self.button3.connect("clicked", self.tutorial)
        self.grid.attach(self.button3, 1, 6, 1, 1)

        self.label4 = Gtk.Label()
        self.label4.set_markup(help_button)
        self.label4.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label4, 1, 7, 1, 1)

        self.button4 = Gtk.Button.new_from_icon_name("help", 3)
        self.button4.connect("clicked", self.onhelpclicked)
        self.grid.attach(self.button4, 1, 8, 1, 1)

        self.label5 = Gtk.Label()
        self.label5.set_markup(drivers)
        self.label5.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label5, 6, 7, 1, 1)

        self.button5 = Gtk.Button.new_from_icon_name("jockey", 3)
        self.button5.connect("clicked", self.ondriveclicked)
        self.grid.attach(self.button5, 6, 8, 1, 1)

        self.label6 = Gtk.Label()
        self.label6.set_markup(lang_sup)
        self.label6.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label6, 4, 5, 1, 1)

        self.button6 = Gtk.Button.new_from_icon_name("accessibility", 3)
        self.button6.connect("clicked", self.show_accessibility_settings)
        self.grid.attach(self.button6, 4, 6, 1, 1)

        self.label7 = Gtk.Label()
        self.label7.set_markup(donate)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label7, 4, 7, 1, 1)

        self.button7 = Gtk.Button.new_from_icon_name("money-manager-ex", 3)
        self.button7.connect("clicked", self.ondonateclicked)
        self.grid.attach(self.button7, 4, 8, 1, 1)

        self.label8 = Gtk.Label()
        self.label8.set_markup(shortcuts)
        self.label8.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label8, 6, 5, 1, 1)

        self.button8 = Gtk.Button.new_from_icon_name("keyboard", 3)
        self.button8.connect("clicked", self.onshortcutclicked)
        self.grid.attach(self.button8, 6, 6, 1, 1)

        self.label9 = Gtk.Label()
        self.label9.set_markup(uninstall)
        self.label9.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label9, 4, 9, 1, 1)

        self.button9 = Gtk.Button.new_from_icon_name("delete", 3)
        self.button9.connect("clicked", self.removal_conf)
        self.grid.attach(self.button9, 4, 10, 1, 1)

        self.label10 = Gtk.Label()
        self.label10.set_markup(lang_sup2)
        self.label10.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label10, 4, 3, 1, 1)

        self.button10 = Gtk.Button.new_from_icon_name("preferences-desktop-locale", 3)
        self.button10.connect("clicked", self.onlangsupportclicked)
        self.grid.attach(self.button10, 4, 4, 1, 1)

        self.start_up = Gtk.CheckButton.new_with_label(start_up_label)
        self.start_up.set_active(show_at_start_up)
        self.start_up.connect("toggled", self.start_up_toggle)
        self.grid.attach(self.start_up, 1, 13, 2, 1)

        width = self.get_size()[0]
        width = int(width * 0.125)
        self.button10.set_margin_start(width)
        self.button10.set_margin_end(width)
        self.button6.set_margin_start(width)
        self.button6.set_margin_end(width)
        self.button4.set_margin_start(width)
        self.button2.set_margin_end(width)
        self.button3.set_margin_start(width)
        self.button1.set_margin_start(width)
        self.button9.set_margin_end(width)
        self.button9.set_margin_start(width)
        self.button8.set_margin_end(width)
        self.button7.set_margin_end(width)
        self.button7.set_margin_start(width)
        self.button5.set_margin_end(width)
        self.label2.set_margin_end(width)
        self.label8.set_margin_end(width)
        self.label5.set_margin_end(width)
        self.label7.set_margin_end(width)
        self.label7.set_margin_start(width)
        self.label4.set_margin_start(width)
        self.label10.set_margin_start(width)
        self.label9.set_margin_start(width)
        self.label10.set_margin_end(width)
        self.label9.set_margin_end(width)
        self.label9.set_margin_start(width)
        self.label6.set_margin_end(width)
        self.label6.set_margin_start(width)
        self.label1.set_margin_start(width)
        self.start_up.set_margin_start(int(width / 2))
        self.start_up.set_margin_bottom(int(width / 2))

        self.show_all()

    def show_readme(self, widget):
        version = subprocess.check_output(["lsb_release", "-rs"]).decode()
        subprocess.Popen(["xdg-open",
                          f"https://download.draugeros.org/docs/{version}/README.pdf"])

    def start_up_toggle(self, widget):
        global show_at_start_up
        show_at_start_up = self.start_up.get_active()
        print(show_at_start_up)

    def removal_conf(self, button):

        self.clear_window()

        self.label = Gtk.Label()
        self.label.set_markup(message_show_remove)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.label = self._set_default_margins(self.label)
        self.grid.attach(self.label, 1, 1, 3, 1)

        self.button1 = Gtk.Button.new_with_label(label=YES)
        self.button1.connect("clicked", self.onuninstallclicked)
        self.button1 = self._set_default_margins(self.button1)
        self.grid.attach(self.button1, 1, 2, 1, 1)

        self.button2 = Gtk.Button.new_with_label(label=NO)
        self.button2.connect("clicked", self.reset)
        self.button2 = self._set_default_margins(self.button2)
        self.grid.attach(self.button2, 3, 2, 1, 1)

        self.show_all()

    def show_accessibility_settings(self, button):
        self.clear_window()

        self.label = Gtk.Label()
        self.label.set_markup("""
    \t\t<b>%s</b>\t\t\t
""" % (lang_sup))
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 1, 1, 2, 1)

        self.label3 = Gtk.Label()
        self.label3.set_markup(font)
        self.grid.attach(self.label3, 1, 3, 1, 1)

        self.font_button = Gtk.FontButton()
        # get system font and font size
        system_font = subprocess.check_output(["xfconf-query", "--channel", "xsettings",
                                    "--property", "/Gtk/FontName"])
        system_font = list(str(system_font))
        del(system_font[1])
        del(system_font[0])
        length = len(system_font) - 1
        x = 0
        while x <= 2:
            del(system_font[length - x])
            x = x + 1
        system_font = "".join(system_font)
        # set font and size for button
        self.font_button.set_font(system_font)
        self.font_button.connect("font-set", self.set_font)
        self.grid.attach(self.font_button, 2, 3, 1, 1)

        self.label4 = Gtk.Label()
        self.label4.set_markup("%s" % (access_label))
        self.label4.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label4, 1, 4, 1, 1)

        self.button6 = Gtk.Button.new_from_icon_name("accessibility", 3)
        self.button6.connect("clicked", self.goto_accessibility)
        self.grid.attach(self.button6, 2, 4, 1, 1)

        self.button1 = Gtk.Button.new_with_label(label=Back)
        self.button1.connect("clicked", self.reset)
        self.grid.attach(self.button1, 1, 20, 1, 1)

        width = self.get_size()[0]
        height = int(width * 0.025)
        width = int(width * 0.05)
        # self.label4.set_margin_top(height)
        self.label4.set_margin_bottom(height)
        self.label4.set_margin_start(width)
        # self.label4.set_margin_end(width)
        # self.label3.set_margin_end(width)
        self.label3.set_margin_start(width)
        # self.label3.set_margin_top(height)
        self.label3.set_margin_bottom(height)
        self.button6.set_margin_top(height)
        self.button6.set_margin_bottom(height)
        self.button6.set_margin_start(width)
        self.button6.set_margin_end(width)
        self.button1.set_margin_bottom(height)
        self.button1.set_margin_start(width)
        self.button1.set_margin_end(width)
        self.font_button.set_margin_end(width)
        self.font_button.set_margin_start(width)
        self.font_button.set_margin_top(height)
        self.font_button.set_margin_bottom(height)

        self.show_all()

    def goto_accessibility(self, button):
        subprocess.Popen("xfce4-accessibility-settings")

    def set_font(self, widget):
        subprocess.Popen(["xfconf-query", "--channel", "xsettings", "--property",
               "/Gtk/FontName", "--set", self.font_button.get_font()])

    def onlangsupportclicked(self, button):
        self.clear_window()

        self.label = Gtk.Label()
        self.label.set_markup("""
    \t\t<b>%s</b>\t\t\t
""" % (lang_sup2))
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 1, 1, 2, 1)

        self.label1 = Gtk.Label()
        self.label1.set_markup(lang_sup3)
        self.label1.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label1, 1, 2, 2, 1)

        self.button0 = Gtk.Button.new_from_icon_name("system-software-install",
                                                     3)
        self.button0.connect("clicked", self.install_locale_packages)
        self.grid.attach(self.button0, 1, 3, 2, 1)

        self.label2 = Gtk.Label()
        self.label2.set_markup(lang_sup4)
        self.label2.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label2, 1, 4, 2, 1)

        self.button2 = Gtk.Button.new_from_icon_name("preferences-desktop-locale",
                                                     3)
        self.button2.connect("clicked", self.onlanguageclicked)
        self.grid.attach(self.button2, 1, 5, 2, 1)

        self.label3 = Gtk.Label()
        self.label3.set_markup("\n")
        self.label3.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label3, 1, 6, 2, 1)

        self.button1 = Gtk.Button.new_with_label(label=Back)
        self.button1.connect("clicked", self.reset)
        self.grid.attach(self.button1, 1, 20, 1, 1)

        width1 = self.get_size()[0]
        width = int(width1 * 0.125)
        self.button0.set_margin_start(width)
        self.label1.set_margin_start(width)
        self.label2.set_margin_start(width)
        self.label2.set_margin_end(width)
        self.label1.set_margin_end(width)
        self.button0.set_margin_end(width)
        self.button2.set_margin_start(width)
        self.button2.set_margin_end(width)
        self.button1.set_margin_end(width)
        self.button1.set_margin_start(int(width1 * 0.025))
        self.button1.set_margin_bottom(int(width1 * 0.025))

        self.show_all()

    def install_locale_packages(self, button):
        lang = os.getenv("LANG").split(".")
        lang = lang[0]
        lang = lang.split("_")
        lang = "-".join(lang).lower()
        if lang[0:2] == "en":
            subprocess.check_call(["notify-send", "--app-name='Drauger Welcome'",
                        "--icon=/usr/share/icons/Drauger/scalable/menus/drauger_os-logo.svg",
                        "Locale packages do not need to be installed."])
        else:
            package_name = "drauger-locale-" + lang
            packages = subprocess.check_output(["apt", "search",
                                     "drauger-locale"]).decode()
            packages = packages.split("\n")
            for each in range(len(packages) - 1, -1, -1):
                if packages[each][:15] != "drauger-locale-":
                    del packages[each]
                else:
                    packages[each] = packages[each].split("/")[0]
            if package_name in packages:
                try:
                    subprocess.check_call(["pkexec", "apt", "--force-yes", "install",
                               package_name])
                    subprocess.check_call(["notify-send", "--app-name='Drauger Welcome'",
                                "--icon=/usr/share/icons/Drauger/scalable/menus/drauger_os-logo.svg",
                                "%s installed." % (package_name)])
                except subprocess.CalledProcessError:
                    subprocess.check_call(["notify-send", "--app-name='Drauger Welcome'",
                                "--icon=/usr/share/icons/Drauger/scalable/menus/drauger_os-logo.svg",
                                "Locale package could not be installed."])

    def onnextclicked(self, button):
        if self.check == 0:
            self.label.set_markup(multi_0)
        elif self.check == 1:
            self.label.set_markup(multi_1)
        elif self.check == 2:
            self.removal_conf("clicked")
        else:
            subprocess.check_call(["/usr/share/drauger-welcome/log-out", "2",
                        "/usr/share/drauger-welcome/multi_desktop.py",
                        "Unknown error. Variable self.check in function onnextclicked in class notify outside expected range",
                        "drauger-welcome", "UNKNOWN", "UNKNOWN"])
            exit(2)
        self.check = self.check + 1

    def onwebclicked(self, button):
        subprocess.Popen(["/usr/bin/xdg-open", "https://draugeros.org/go"])

    def onhelpclicked(self, button):

        self.clear_window()

        label = Gtk.Label()
        label.set_markup(HELP)
        label.set_justify(Gtk.Justification.CENTER)
        label = self._set_default_margins(label)
        self.grid.attach(label, 1, 3, 3, 1)

        label2 = Gtk.Label()
        label2.set_markup("""
Telegram
""")
        label2.set_justify(Gtk.Justification.CENTER)
        label2 = self._set_default_margins(label2)
        self.grid.attach(label2, 1, 4, 1, 1)

        label3 = Gtk.Label()
        label3.set_markup("""
Discord
""")
        label3.set_justify(Gtk.Justification.CENTER)
        label3 = self._set_default_margins(label3)
        self.grid.attach(label3, 3, 4, 1, 1)

        label5 = Gtk.Label()
        label5.set_markup(help_yourself)
        label5.set_justify(Gtk.Justification.CENTER)
        label5 = self._set_default_margins(label5)
        self.grid.attach(label5, 1, 1, 3, 1)

        label6 = Gtk.Label()
        label6.set_markup("""
myDrauger Support System
""")
        label6.set_justify(Gtk.Justification.CENTER)
        label6 = self._set_default_margins(label6)
        self.grid.attach(label6, 2, 4, 1, 1)

        button2 = Gtk.Button.new_with_label(label="%s Telegram" % (Open))
        button2.connect("clicked", self.open_telegram)
        button2 = self._set_default_margins(button2)
        self.grid.attach(button2, 1, 5, 1, 1)

        button3 = Gtk.Button.new_with_label(label="%s Discord" % (Open))
        button3.connect("clicked", self.open_discord)
        button3 = self._set_default_margins(button3)
        self.grid.attach(button3, 3, 5, 1, 1)

        button5 = Gtk.Button.new_with_label(label="%s Drauger OS Wiki" % (Open))
        button5.connect("clicked", self.open_wiki)
        button5 = self._set_default_margins(button5)
        self.grid.attach(button5, 1, 2, 3, 1)

        button6 = Gtk.Button.new_with_label(label="%s myDrauger" % (Open))
        button6.connect("clicked", self.open_mydrauger)
        button6 = self._set_default_margins(button6)
        self.grid.attach(button6, 2, 5, 1, 1)

        button1 = Gtk.Button.new_with_label(label=Back)
        button1.connect("clicked", self.reset)
        button1 = self._set_default_margins(button1)
        self.grid.attach(button1, 1, 20, 1, 1)

        self.show_all()

    def open_discord(self, button):
        cache = apt.cache.Cache()
        cache.open()
        installed = False
        with cache.actiongroup():
            for each in cache:
                if "discord" == each.name:
                    installed = each.is_installed
                    break
        if not installed:
            check = subprocess.check_output("snap list | awk '{print $1}' | grep 'discord'",
                                            shell=True).decode()[:-1]
            if check == "discord":
                installed = True
        if not installed:
            subprocess.check_call(["snap", "install", "discord"])
        subprocess.Popen(["discord", "https://discord.gg/JW8FGrc"])

    def _set_default_margins(self, widget):
        """Set default margin size"""
        widget.set_margin_start(10)
        widget.set_margin_end(10)
        widget.set_margin_top(10)
        widget.set_margin_bottom(10)
        return widget

    def open_mydrauger(self, button):
        subprocess.Popen(["xdg-open", "https://draugeros.org/go/my"])

    def open_telegram(self, button):
        cache = apt.cache.Cache()
        cache.open()
        installed = False
        with cache.actiongroup():
            for each in cache:
                if "telegram-desktop" == each.name:
                    installed = each.is_installed
                    break
        if not installed:
            check = subprocess.check_output("snap list | awk '{print $1}' | grep 'telegram-desktop'",
                                            shell=True).decode()[:-1]
            if check == "telegram-desktop":
                installed = True
        if not installed:
            subprocess.check_call(["snap", "install", "telegram-desktop"])
        subprocess.Popen(["telegram-desktop", "https://t.me/draugeros"])

    def open_wiki(self, button):
        subprocess.Popen(["xdg-open", "https://draugeros.org/go/wiki"])

    def ondriveclicked(self, button):
        self.clear_window()

        # we need to make a window here to manage drivers
        # start off by getting all our PCI devices
        devices = subprocess.check_output(["lspci", "-qmmnn"]).decode()
        # we need to parse this so that we can check for devices in need of drivers
        # this will do most of that for us
        data = devices.split("\n")
        for each in range(len(data) - 1, -1, -1):
            data[each] = shlex.split(data[each])

        # now we need to get rid of anything that we don't need
        for each in range(len(data) - 1, -1, -1):
            if len(data[each]) < 2:
                del data[each]
                continue
            if "VGA" in data[each][1]:
                continue
            elif data[each][1].lower() == "network controller":
                continue
            elif data[each][1].lower() == "ethernet controller": # these don't always need drivers. But sometimes they do.
                continue
            del data[each]

        # now we have a list of all devices that MIGHT need drivers: GPUs, Wifi cards, Ethernet cards
        # check if they have chips that need drivers or not
        for each in range(len(data) - 1, -1, -1):
            if "VGA" in data[each][1]: # GPUs
                if "nvidia" not in data[each][2].lower():
                    del data[each]
            elif data[each][1].lower() in ("network controller",
                                           "ethernet controller"): # Networking controllers (Wifi & Ethernet)
                if "broadcom" in data[each][2].lower():
                    continue
                elif "realtek" in data[each][2].lower():
                    continue
                del data[each]

        # now we have a list of JUST devices that need drivers
        # now we need to figure out what drivers are suited to what generation of card and handle that accordingly.
        drivers = {}
        for each in data:
            if "nvidia" in each[2].lower():
                if "nvidia" not in drivers:
                    drivers["nvidia"] = []
                device = each[3].split(" ")
                for each1 in device:
                    if each1.isdigit():
                        if len(each1) >= 4:
                            device = each1[:2]
                        else:
                            device = each1[0]
                        break
                if device not in drivers["nvidia"]:
                    drivers["nvidia"] = device
                break
            elif "broadcom" in each[2].lower():
                if "broadcom" not in drivers:
                    drivers["broadcom"] = []
                device = each[3].split(" ")[-1][1:-1]
                if device not in drivers["broadcom"]:
                    drivers["broadcom"].append(device)
                break
            elif "realtek" in each[2].lower():
                if "realtek" not in drivers:
                    drivers["realtek"] = []
                device = each[3].split(" ")[0].lower()
                if device not in drivers["realtek"]:
                    drivers["realtek"].append(device)
                break

        guide = {}
        if "nvidia" in drivers:
            with open("../../../etc/drauger-welcome/nvidia_driver_guide.json",
                      "r") as file:
                      guide.update({"nvidia": json.load(file)})
        if "broadcom" in drivers:
            with open("../../../etc/drauger-welcome/broadcom_driver_guide.json",
                      "r") as file:
                      guide.update({"broadcom": json.load(file)})
        if "realtek" in drivers:
            with open("../../../etc/drauger-welcome/realtek_driver_guide.json",
                      "r") as file:
                      guide.update({"realtek": json.load(file)})

        # we now have all the data and correlations to figure out what driver we need where
        # just need to actually follow the correlations
        to_install = {}
        if "nvidia" in drivers:
            to_install[f"nvidia-driver-{guide['nvidia'][drivers['nvidia']]}"] = {"installed": None, "desc": ""}

        # check and see if the package is already installed. If it is, then the user is good to go
        # so delete the package from the list
        cache = apt.cache.Cache()
        cache.open()
        installed = False
        with cache.actiongroup():
            for pkg in to_install:
                for each in cache:
                    if pkg == each.name:
                        to_install[pkg]["installed"] = each.is_installed
                        to_install[pkg]["desc"] = each.versions[0].description

        # this makes an if-statement later on easier to write
        all_installed = True
        for each in to_install:
            if not to_install[each]["installed"]:
                all_installed = False
                break

        self.drivers = to_install

        label = Gtk.Label()
        label.set_markup("<b>Below are all the drivers we suggest for your system</b>")
        label.set_justify(Gtk.Justification.CENTER)
        label = self._set_default_margins(label)
        self.grid.attach(label, 1, 1, 5, 1)

        label1 = Gtk.Label()
        label1.set_markup("Alternatively, you may use Synaptic Package Manager to install drivers yourself.")
        label1.set_justify(Gtk.Justification.CENTER)
        label1 = self._set_default_margins(label1)
        self.grid.attach(label1, 1, 2, 5, 1)

        label2 = Gtk.Label()
        label2.set_markup("<b>Package Name</b>")
        label2.set_justify(Gtk.Justification.CENTER)
        label2 = self._set_default_margins(label2)
        self.grid.attach(label2, 1, 4, 1, 1)

        label3 = Gtk.Label()
        label3.set_markup("<b>Description</b>")
        label3.set_justify(Gtk.Justification.CENTER)
        label3 = self._set_default_margins(label3)
        self.grid.attach(label3, 3, 4, 1, 1)

        label4 = Gtk.Label()
        label4.set_markup("<b>Installation Status</b>")
        label4.set_justify(Gtk.Justification.CENTER)
        label4 = self._set_default_margins(label4)
        self.grid.attach(label4, 5, 4, 1, 1)

        sep = Gtk.Separator.new(Gtk.Orientation.HORIZONTAL)
        sep = self._set_default_margins(sep)
        self.grid.attach(sep, 1, 5, 5, 1)

        # labels detailing all drivers
        x = 1
        y = 6
        for each in to_install:
            label = Gtk.Label()
            label.set_markup(f"<b>{each}</b>")
            label.set_justify(Gtk.Justification.CENTER)
            label = self._set_default_margins(label)
            self.grid.attach(label, x, y, 1, 1)

            label = Gtk.Label()
            label.set_markup(f"{to_install[each]['desc']}")
            label.set_justify(Gtk.Justification.CENTER)
            label = self._set_default_margins(label)
            self.grid.attach(label, x + 2, y, 1, 1)

            label = Gtk.Label()
            if to_install[each]["installed"]:
                label.set_markup("Installed")
            else:
                label.set_markup("Installed")
            label.set_justify(Gtk.Justification.CENTER)
            label = self._set_default_margins(label)
            self.grid.attach(label, x + 4, y, 1, 1)

            y += 1

        sep = Gtk.Separator.new(Gtk.Orientation.VERTICAL)
        sep = self._set_default_margins(sep)
        self.grid.attach(sep, 2, 4, 1, y)

        sep = Gtk.Separator.new(Gtk.Orientation.VERTICAL)
        sep = self._set_default_margins(sep)
        self.grid.attach(sep, 4, 4, 1, y)

        button1 = Gtk.Button.new_with_label(label=Back)
        button1.connect("clicked", self.reset)
        button1 = self._set_default_margins(button1)
        self.grid.attach(button1, 1, 20, 1, 1)

        if not all_installed:
            button2 = Gtk.Button.new_with_label(label="Install Missing Drivers")
            button2.connect("clicked", self.driver_install_confirmation)
        else:
            button2 = Gtk.Label()
            button2.set_markup("<b>All Drivers Already Installed</b>")
        button2 = self._set_default_margins(button2)
        self.grid.attach(button2, 3, 20, 1, 1)


        button3 = Gtk.Button.new_with_label(label="Open Synaptic")
        button3.connect("clicked", self.open_synaptic)
        button3 = self._set_default_margins(button3)
        self.grid.attach(button3, 5, 20, 1, 1)

        self.show_all()

    def driver_install_confirmation(self, button):
        self.clear_window()

        label = Gtk.Label()
        label.set_markup("<b>Are you sure you want to install the following packages?</b>")
        label = self._set_default_margins(label)
        self.grid.attach(label, 1, 1, 3, 1)

        label2 = Gtk.Label()
        label2.set_markup(", ".join(self.drivers))
        label2 = self._set_default_margins(label2)
        self.grid.attach(label2, 1, 2, 3, 1)

        button = Gtk.Button.new_with_label(label="Cancel")
        button.connect("clicked", self.reset)
        button = self._set_default_margins(button)
        self.grid.attach(button, 1, 3, 1, 1)

        button2 = Gtk.Button.new_with_label(label="Install Missing Drivers")
        button2.connect("clicked", self.install_missing_drivers)
        button2 = self._set_default_margins(button2)
        self.grid.attach(button2, 3, 3, 1, 1)

        self.show_all()

    def install_missing_drivers(self, button):
        # setup
        cmd = ["pkexec", "apt-get", "-y", "-o",
               "Dpkg::Options::='--force-confold'", "--force-yes", "install"]
        # filter down to just uninstalled drivers
        to_install = []
        for each in self.drivers:
            if self.drivers[each]["installed"]:
                continue
            to_install.append(each)
        if len(to_install) <= 0:
            return
        cmd = cmd + to_install
        # this is arguably the easiest way to do this
        pid = os.fork()
        if pid == 0:
            # this will run as a seperate thread. It's safe to call exit()
            try:
                subprocess.check_call(cmd)
            except subprocess.CalledProcessError:
                subprocess.check_call(["notify-send", "-i", self.icon, "-a",
                                       "Drauger OS Welcome Screen",
                                       "Driver Installation Error",
                                       "Installing Drivers Encountered An Error. Please contact support."])
                exit(2)
            subprocess.check_call(["notify-send", "-i", self.icon, "-a",
                                   "Drauger OS Welcome Screen",
                                   "Driver Installation Success",
                                   "Drivers Successfully Installed. Please Reboot for changes to take effect."])
            exit(0)
        self.post_install_window()

    def post_install_window(self):
        self.clear_window()

        label1 = Gtk.Label()
        label1.set_markup("<b>Installing Drivers</b>")
        label1.set_justify(Gtk.Justification.CENTER)
        label1 = self._set_default_margins(label1)
        self.grid.attach(label1, 1, 1, 4, 1)

        label2 = Gtk.Label()
        label2.set_markup("Please give the background process about 10 minutes max in order to install your drivers for you.")
        label2.set_justify(Gtk.Justification.CENTER)
        label2 = self._set_default_margins(label2)
        self.grid.attach(label2, 1, 2, 4, 1)

        label3 = Gtk.Label()
        label3.set_markup("If you do not receive a notification about how installation went, please check System Monitor to see if installation is still ongoing.")
        label3.set_justify(Gtk.Justification.CENTER)
        label3 = self._set_default_margins(label3)
        self.grid.attach(label3, 1, 3, 4, 1)

        button1 = Gtk.Button.new_with_label(label=Back)
        button1.connect("clicked", self.reset)
        button1 = self._set_default_margins(button1)
        self.grid.attach(button1, 1, 20, 1, 1)

        self.show_all()


    def open_synaptic(self, button):
        subprocess.Popen(["synaptic-pkexec"])

    def onlanguageclicked(self, button):
        subprocess.Popen(["gnome-language-selector"])

    def ondonateclicked(self, button):
        subprocess.Popen(["/usr/bin/xdg-open",
               "https://liberapay.com/Drauger_OS_Development/donate"])

    def onshortcutclicked(self, button):
        self.clear_window()

        self.label = Gtk.Label()
        self.label.set_markup("<b>" + TITLE_sc + "</b>")
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 1, 1, 3, 1)

        self.label = Gtk.Label()
        self.label.set_markup("""
<b>Ctrl+Alt+T</b>
 """)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 1, 2, 1, 1)

        self.label = Gtk.Label()
        self.label.set_markup(sc_0)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 3, 2, 1, 1)

        self.label = Gtk.Label()
        self.label.set_markup("""
<b>Ctrl+Alt+F</b>
""")
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 1, 3, 1, 1)

        self.label = Gtk.Label()
        self.label.set_markup(sc_1)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 3, 3, 1, 1)

        self.label = Gtk.Label()
        self.label.set_markup("""
<b>Ctrl+Alt+M</b>
""")
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 1, 4, 1, 1)

        self.label = Gtk.Label()
        self.label.set_markup(sc_2)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 3, 4, 1, 1)

        self.label = Gtk.Label()
        self.label.set_markup("""
<b>Alt+F</b>
""")
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 1, 5, 1, 1)

        self.label = Gtk.Label()
        self.label.set_markup(sc_3)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 3, 5, 1, 1)

        self.label = Gtk.Label()
        self.label.set_markup("""
<b>Left Super</b>
""")
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 1, 6, 1, 1)

        self.label = Gtk.Label()
        self.label.set_markup(sc_4)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 3, 6, 1, 1)

        self.label = Gtk.Label()
        self.label.set_markup("""
<b>Ctrl+Alt+L</b>
""")
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 1, 7, 1, 1)

        self.label = Gtk.Label()
        self.label.set_markup(sc_5)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 3, 7, 1, 1)

        self.button1 = Gtk.Button.new_with_label(label=Back)
        self.button1.connect("clicked", self.reset)
        self.grid.attach(self.button1, 1, 20, 3, 1)

        width = self.get_size()[0]
        width = int(width * 0.25)
        self.button1.set_margin_start(width)
        self.button1.set_margin_end(width)
        self.button1.set_margin_bottom(int(width / 10))

        self.show_all()

    def onuninstallclicked(self, button):
        # have an uninstall comfirmation dialoge then uninstall based on
        # the answer
        try:
            subprocess.check_call("/usr/share/drauger-welcome/u.sh")
        except subprocess.CalledProcessError:
            subprocess.check_call(["/usr/share/drauger-welcome/log-out",
                        "2", "/usr/share/drauger-welcome/main.py",
                        "/etc/drauger-welcome/u.sh has failed. See error log entry for u.sh for more info.",
                        "drauger-welcome", "UNKNOWN", "UNKNOWN"])

    def onyesclicked(self, button):
        self.onuninstallclicked("clicked")

    def onnoclicked(self, button):
        self.reset("clicked")

    def tutorial(self, button):

        self.clear_window()
        self.check = -1

        self.label = Gtk.Label()
        self.label.set_markup(message_show_tutorial)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.label = self._set_default_margins(self.label)
        self.grid.attach(self.label, 1, 1, 3, 1)

        self.button1 = Gtk.Button.new_with_label(label=Next)
        self.button1.connect("clicked", self.onclicked)
        self.button1 = self._set_default_margins(self.button1)
        self.grid.attach(self.button1, 3, 2, 1, 1)

        self.button2 = Gtk.Button.new_with_label(label=Back)
        self.button2.connect("clicked", self.onclicked)
        self.button2 = self._set_default_margins(self.button2)
        self.grid.attach(self.button2, 1, 2, 1, 1)

        self.button3 = Gtk.Button.new_with_label(label=Exit)
        self.button3.connect("clicked", self.reset)
        self.button3 = self._set_default_margins(self.button3)
        self.grid.attach(self.button3, 2, 2, 1, 1)

        self.show_all()

    def onclicked(self, button):
        if (button.get_label() == Next):
            self.check = self.check + 1
        elif (button.get_label() == Back):
            self.check = self.check - 1
        if self.check == -1:
            self.label.set_markup(message_show_tutorial)
        elif self.check == 0:
            self.label.set_markup(tut_1)
        elif self.check == 1:
            self.label.set_markup(tut_2)
        elif self.check == 2:
            self.label.set_markup(tut_3)
        elif self.check == 3:
            self.label.set_markup(tut_4)
        elif self.check == 4:
            self.label.set_markup(tut_5)
        elif self.check == 5:
            self.multi_desktop("clicked")
        elif self.check < -1:
            self.reset("clicked")

    def multi_desktop(self, button):

        self.clear_window()

        self.label = Gtk.Label()
        self.label.set_markup(multi_ask)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.label = self._set_default_margins(self.label)
        self.grid.attach(self.label, 1, 1, 3, 1)

        self.button1 = Gtk.Button.new_with_label(label=YES)
        self.button1.connect("clicked", self.onmultiyesclicked)
        self.button1 = self._set_default_margins(self.button1)
        self.grid.attach(self.button1, 1, 2, 1, 1)

        self.button2 = Gtk.Button.new_with_label(label=NO)
        self.button2.connect("clicked", self.onmultinoclicked)
        self.button2 = self._set_default_margins(self.button2)
        self.grid.attach(self.button2, 3, 2, 1, 1)

        self.show_all()

    def onmultiyesclicked(self, button):
        self.clear_window()
        self.check = 0

        self.label = Gtk.Label()
        self.label.set_markup(message_show_multi_desktop)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.label = self._set_default_margins(self.label)
        self.grid.attach(self.label, 1, 1, 3, 1)

        self.button1 = Gtk.Button.new_with_label(label=Next)
        self.button1.connect("clicked", self.onnextclicked)
        self.button1 = self._set_default_margins(self.button1)
        self.grid.attach(self.button1, 3, 2, 1, 1)

        self.show_all()

    def onmultinoclicked(self, button):
        self.removal_conf("clicked")

    def exit(self, button):
        global show_at_start_up
        global HOME
        Gtk.main_quit("delete-event")
        if (not show_at_start_up):
            with open("%s/.drauger-tut" % (HOME), "w+") as flagfile:
                flagfile.write("")
                flagfile.close()
        else:
            if (os.path.exists("%s/.drauger-tut" % (HOME))):
                os.remove("%s/.drauger-tut" % (HOME))
        print(1)
        exit(1)

    def clear_window(self):
        children = self.grid.get_children()
        for each in children:
            self.grid.remove(each)


def welcome_show():
    window = welcome()
    window.set_decorated(True)
    window.set_resizable(False)
    window.set_position(Gtk.WindowPosition.CENTER)
    window.connect("delete-event", welcome.exit)
    window.show_all()
    Gtk.main()

if __name__ == '__main__':
    try:
        welcome_show()
    except:
        subprocess.check_call(["/usr/share/drauger-welcome/log-out",
                    "2 /usr/share/drauger-welcome/main_ui.py",
                    "Unknown error. Function welcome_show has failed.",
                    "drauger-welcome", "UNKNOWN", "UNKNOWN"])
