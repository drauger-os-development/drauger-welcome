#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  main_ui.py
#
#  Copyright 2020 Thomas Castleman <contact@draugeros.org>
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
from os import system, path, getenv, remove
from subprocess import Popen, check_output, check_call, CalledProcessError
import json

LANG = getenv("LANG").split(".")
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
        elif (each[0] == "tut_6"):
            tut_6 = each[1]
        elif (each[0] == "multi_ask"):
            multi_ask = each[1]
        elif (each[0] == "lang_sup3"):
            lang_sup3 = each[1]
        elif (each[0] == "lang_sup4"):
            lang_sup4 = each[1]

except FileNotFoundError:
    message_show_remove = "\n\tThank you again for using Drauger OS. Would you like to uninstall drauger-welcome?\t\n"
    message_show_tutorial = "\n\tThank you for downloading and installing Drauger OS, the free Linux gaming OS.\t\n"
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
    tut_0 = "\n\tIn this tutorial, you will recive a quick introduction regarding how to work Drauger OS.  \n"
    tut_1 = "\n\tThe bars on the top, left, and bottom of your screen are your desktop panels.\t\n\tThe left contains quick access to some the most commonly used apps and widgets.\t\n\tThe top one contains the the main menu, on the far left when you click on the Drauger OS logo,\t\n\tand the log out menu on the far right under your username.\t\n\tThe bottom pannel gives you a quick view of what's on each desktop, but more on that later.\t\n"
    tut_2 = "\n\tIn order to see any apps in the left desktop panel that are not\t\n\tcurrently on display, simply click on the drop down arrow underneath\t\n\tthe icon\t\n"
    tut_3 = "\n\tIn order to see any apps not on the left desktop panel, click the Drauger OS Logo\t\n\ton the far left of the top panel.\t\n"
    tut_4 = "\n\tDrauger OS also has support for not only keyboards and mice,\t\n\tas well as touchpads and touchscreens,\t\n\tit also has support for most Xbox and Xbox 360 controllers,\t\n\tas well as some Playstation controllers.\t\n"
    tut_5 = "\n\tFinally, the four rectangles on the bottom of your screen are the four current desktops.\t\n\tYou may not be able to see them very well considering they blend into the default wallpaper.\t\n"
    tut_6 = "\n\tIf you wish to learn more about how to use the Drauger OS desktop, please visit:\n\t<a href=\"https://draugeros.org/go/wiki/basics-of-the-drauger-os-desktop/\"> https://draugeros.org/go/wiki/basics-of-the-drauger-os-desktop/ </a>\n\t"
    multi_ask = "\n\tWould you like to learn more about multiple desktops?\t\n"
    lang_sup3 = "\n\tInstall locale packages.\t\n"
    lang_sup4 = "\n\tMulti-lingual support settings.\t\n"
    Open = "Open"


HOME = getenv("HOME")
if (not path.exists("%s/.drauger-tut" % (HOME))):
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
        self.grid = Gtk.Grid(orientation=Gtk.Orientation.VERTICAL,)
        self.add(self.grid)
        self.set_icon_from_file("/usr/share/icons/Drauger/scalable/menus/drauger_os-logo.svg")

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
        self.button10.connect("clicked", self.onCYGOclicked)
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
        version = check_output(["lsb_release", "-rs"]).decode()
        Popen(["xdg-open",
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
        self.grid.attach(self.label, 1, 1, 3, 1)

        self.button1 = Gtk.Button.new_with_label(label=YES)
        self.button1.connect("clicked", self.onuninstallclicked)
        self.grid.attach(self.button1, 1, 2, 1, 1)

        self.button2 = Gtk.Button.new_with_label(label=NO)
        self.button2.connect("clicked", self.reset)
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
        system_font = check_output(["xfconf-query", "--channel", "xsettings",
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
        Popen("xfce4-accessibility-settings")

    def set_font(self, widget):
        Popen(["xfconf-query", "--channel", "xsettings", "--property",
               "/Gtk/FontName", "--set", self.font_button.get_font()])

    def onCYGOclicked(self, button):
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
        lang = getenv("LANG").split(".")
        lang = lang[0]
        lang = lang.split("_")
        lang = "-".join(lang).lower()
        if lang[0:2] == "en":
            check_call(["notify-send", "--app-name='Drauger Welcome'",
                        "--icon=/usr/share/icons/Drauger/scalable/menus/drauger_os-logo.svg",
                        "Locale packages do not need to be installed."])
        else:
            package_name = "drauger-locale-" + lang
            packages = check_output(["apt", "search",
                                     "drauger-locale"]).decode()
            packages = packages.split("\n")
            for each in range(len(packages) - 1, -1, -1):
                if packages[each][:15] != "drauger-locale-":
                    del packages[each]
                else:
                    packages[each] = packages[each].split("/")[0]
            if package_name in packages:
                try:
                    check_call(["pkexec", "apt", "--force-yes", "install",
                               package_name])
                    check_call(["notify-send", "--app-name='Drauger Welcome'",
                                "--icon=/usr/share/icons/Drauger/scalable/menus/drauger_os-logo.svg",
                                "%s installed." % (package_name)])
                except CalledProcessError:
                    check_call(["notify-send", "--app-name='Drauger Welcome'",
                                "--icon=/usr/share/icons/Drauger/scalable/menus/drauger_os-logo.svg",
                                "Locale package could not be installed."])

    def onnextclicked(self, button):
        if self.check == 0:
            self.label.set_text(multi_0)
        elif self.check == 1:
            self.label.set_text(multi_1)
        elif self.check == 2:
            self.removal_conf("clicked")
        else:
            check_call(["/usr/share/drauger-welcome/log-out", "2",
                        "/usr/share/drauger-welcome/multi_desktop.py",
                        "Unknown error. Variable self.check in function onnextclicked in class notify outside expected range",
                        "drauger-welcome", "UNKNOWN", "UNKNOWN"])
            exit(2)
        self.check = self.check + 1

    def onwebclicked(self, button):
        Popen(["/usr/bin/xdg-open", "https://draugeros.org/go"])

    def onhelpclicked(self, button):

        self.clear_window()

        self.label = Gtk.Label()
        self.label.set_markup(HELP)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 1, 3, 3, 1)

        self.label2 = Gtk.Label()
        self.label2.set_markup("""
Telegram
""")
        self.label2.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label2, 1, 4, 1, 1)

        self.label3 = Gtk.Label()
        self.label3.set_markup("""
Discord
""")
        self.label3.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label3, 3, 4, 1, 1)

        self.label5 = Gtk.Label()
        self.label5.set_markup(help_yourself)
        self.label5.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label5, 1, 1, 3, 1)

        self.label6 = Gtk.Label()
        self.label6.set_markup("""
myDrauger Support System
""")
        self.label6.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label6, 2, 4, 1, 1)

        self.button2 = Gtk.Button.new_with_label(label="%s Telegram" % (Open))
        self.button2.connect("clicked", self.open_telegram)
        self.grid.attach(self.button2, 1, 5, 1, 1)

        self.button3 = Gtk.Button.new_with_label(label="%s Discord" % (Open))
        self.button3.connect("clicked", self.open_discord)
        self.grid.attach(self.button3, 3, 5, 1, 1)

        self.button5 = Gtk.Button.new_with_label(label="%s Drauger OS Wiki" % (Open))
        self.button5.connect("clicked", self.open_wiki)
        self.grid.attach(self.button5, 1, 2, 3, 1)

        self.button6 = Gtk.Button.new_with_label(label="%s myDrauger" % (Open))
        self.button6.connect("clicked", self.open_mydrauger)
        self.grid.attach(self.button6, 2, 5, 1, 1)

        self.button1 = Gtk.Button.new_with_label(label=Back)
        self.button1.connect("clicked", self.reset)
        self.grid.attach(self.button1, 1, 20, 1, 1)

        width = self.get_size()[0]
        width = int(width * 0.025)
        self.button5.set_margin_start(width)
        self.button5.set_margin_end(width)
        self.button2.set_margin_start(width)
        self.button2.set_margin_end(width)
        self.button3.set_margin_start(width)
        self.button3.set_margin_end(width)
        self.button6.set_margin_end(width)
        self.button6.set_margin_start(width)
        self.button1.set_margin_start(width)
        self.button1.set_margin_end(width)
        self.button1.set_margin_top(width)
        self.button1.set_margin_bottom(width)
        print(self.button1.get_size_request())
        # self.button1.set_margin_top(int(width / 2))
        # self.button1.set_margin_bottom(int(width / 2))

        self.show_all()

    def open_discord(self, button):
        Popen(["xdg-open", "https://discord.gg/JW8FGrc"])

    def open_mydrauger(self, button):
        Popen(["xdg-open", "https://draugeros.org/go/my"])

    def open_telegram(self, button):
        Popen(["xdg-open", "https://t.me/draugeros"])

    def open_wiki(self, button):
        Popen(["xdg-open", "https://draugeros.org/go/wiki"])

    def ondriveclicked(self, button):
        Popen(["/usr/bin/software-properties-gtk", "--open-tab=4"])

    def onlanguageclicked(self, button):
        Popen(["gnome-language-selector"])

    def ondonateclicked(self, button):
        Popen(["/usr/bin/xdg-open", "https://paypal.me/pools/c/89GtByYaTT"])

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
            check_call("/usr/share/drauger-welcome/u.sh")
        except CalledProcessError:
            check_call(["/usr/share/drauger-welcome/log-out",
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
        self.grid.attach(self.label, 1, 1, 3, 1)

        self.button1 = Gtk.Button.new_with_label(label=Next)
        self.button1.connect("clicked", self.onclicked)
        self.grid.attach(self.button1, 3, 2, 1, 1)

        self.button2 = Gtk.Button.new_with_label(label=Back)
        self.button2.connect("clicked", self.onclicked)
        self.grid.attach(self.button2, 1, 2, 1, 1)

        self.button3 = Gtk.Button.new_with_label(label=Exit)
        self.button3.connect("clicked", self.reset)
        self.grid.attach(self.button3, 2, 2, 1, 1)

        self.show_all()

    def onclicked(self, button):
        if (button.get_label() == Next):
            self.check = self.check + 1
        elif (button.get_label() == Back):
            self.check = self.check - 1
        if self.check == -1:
            self.label.set_text(message_show_tutorial)
        elif self.check == 0:
            self.label.set_text(tut_0)
        elif self.check == 1:
            self.label.set_text(tut_1)
        elif self.check == 2:
            self.label.set_text(tut_2)
        elif self.check == 3:
            self.label.set_text(tut_3)
        elif self.check == 4:
            self.label.set_text(tut_4)
        elif self.check == 5:
            self.label.set_text(tut_5)
        elif self.check == 6:
            self.label.set_markup(tut_6)
        elif self.check == 7:
            self.multi_desktop("clicked")

    def multi_desktop(self, button):

        self.clear_window()

        self.label = Gtk.Label()
        self.label.set_markup(multi_ask)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 1, 1, 3, 1)

        self.button1 = Gtk.Button.new_with_label(label=YES)
        self.button1.connect("clicked", self.onmultiyesclicked)
        self.grid.attach(self.button1, 1, 2, 1, 1)

        self.button2 = Gtk.Button.new_with_label(label=NO)
        self.button2.connect("clicked", self.onmultinoclicked)
        self.grid.attach(self.button2, 3, 2, 1, 1)

        self.show_all()

    def onmultiyesclicked(self, button):
        self.clear_window()
        self.check = 0

        self.label = Gtk.Label()
        self.label.set_markup(message_show_multi_desktop)
        self.label.set_justify(Gtk.Justification.CENTER)
        self.grid.attach(self.label, 1, 1, 3, 1)

        self.button1 = Gtk.Button.new_with_label(label=Next)
        self.button1.connect("clicked", self.onnextclicked)
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
            if (path.exists("%s/.drauger-tut" % (HOME))):
                remove("%s/.drauger-tut" % (HOME))
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
        check_call(["/usr/share/drauger-welcome/log-out",
                    "2 /usr/share/drauger-welcome/main_ui.py",
                    "Unknown error. Function welcome_show has failed.",
                    "drauger-welcome", "UNKNOWN", "UNKNOWN"])
