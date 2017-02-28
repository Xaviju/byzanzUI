#!/usr/bin/env python

import gi, subprocess, shlex
gi.require_version('Gtk', '3.0')

from gi.repository import Gtk

class Handler:
    def on_main_window_destroy(self, *args):
        Gtk.main_quit(*args)

    def on_record_clicked(self, button):
        loading_spinner = builder.get_object("loading_spinner")
        duration = builder.get_object("duration").get_text()
        delay = builder.get_object("delay").get_text() or 1
        offsetX = builder.get_object("offsetX").get_text()
        offsetY = builder.get_object("offsetY").get_text()
        captureWidth = builder.get_object("captureWidth").get_text()
        captureHeight = builder.get_object("captureHeight").get_text()
        recordMouse = "-c" if builder.get_object("recordMouse").get_active() else ''
        recordAudio = "-a" if builder.get_object("recordAudio").get_active() else ''
        captureLocation = builder.get_object("captureLocation").get_uri() or '.'
        fileName = builder.get_object("fileName").get_text()
        uri = captureLocation + '/' + fileName

        command_line = "byzanz-record -d {0} --delay={1} {2} {3} -x {4} -y {5} -w {6} -h {7} -v {8}".format(duration, delay, recordMouse, recordAudio, offsetX, offsetY, captureWidth, captureHeight, uri)

        cmd = shlex.split(command_line)

        process = subprocess.run(cmd, stdout=subprocess.PIPE, encoding="utf-8")

builder = Gtk.Builder()
builder.add_from_file("byzanzUI.glade")
builder.connect_signals(Handler())

window = builder.get_object("main_window")
window.show_all()

Gtk.main()
