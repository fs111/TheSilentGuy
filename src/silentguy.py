#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This is a little module for phenny that talks to you, for more details see here:
http://hackerspace.be/TheSilentGuy
http://github.com/fs111/TheSilentGuy

Author: André Kelpe <efeshundertelf at googlemail dot com>
License: GPLv3

"""
from subprocess import Popen, PIPE

COMMAND = ".talk"

ESPEAK_COMMAND = "espeak -s 40  -p 99  -v en"

class Speaker:
    """Class that wraps the espeak subprocess"""

    def __init__(self):
        self.process = Popen([ESPEAK_COMMAND], shell=True,
          stdin=PIPE, close_fds=True)

    def sayitoutloud(self, what):
        """I'm geek and proud! :-)"""
        self.process.stdin.write(what + "\n")

# poor mans singleton
speaker = Speaker()


def announce(phenny, input, origin):
    """Callback that phenny calls when somone choins the channel"""
    speaker.sayitoutloud("Dudes, %s has joined the channel" % origin.nick)
# tell phenny what to do
announce.rule = "(.*)"
announce.event = "JOIN"
announce.with_origin = True



def talk(phenny, input, origin):
    """Callback that phenny calls when somone issues the .talk command"""
    # only admins are allowed to use the .talk command
    if origin.nick in phenny.config.admins:
        input = input.replace(COMMAND, "")
        speaker.sayitoutloud(input)
    else:
        phenny.reply("only admins can use .talk")
# tell phenny what to do
talk.commands = ["talk"]
talk.example = ".talk what"
talk.with_origin = True
