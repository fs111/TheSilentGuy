#!/usr/bin/env python
# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE
COMMAND = ".talk"

class Speaker:

    def __init__(self):
        self.process = Popen(["espeak -s 40  -p 99  -v en "], shell=True,
          stdin=PIPE, stdout=PIPE, close_fds=True) 

    def sayitoutloud(self, what):
        self.process.stdin.write(what + "\n")

speaker = Speaker()


def announce(phenny, input, origin):
    """Callback that phenny calls when somone issues the .talk command"""
    speaker.sayitoutloud("Dudes, %s has joined the channel" % origin.nick)

# tell phenny what to do
announce.rule = "(.*)"
announce.event = "JOIN"
announce.with_origin = True


def talk(phenny, input, origin):
    """Callback that phenny calls when somone issues the .talk command"""
    if origin.nick in phenny.config.admins:
        input = input.replace(COMMAND, "") 
        speaker.sayitoutloud(input)
    
# tell phenny what to do
talk.commands = ["talk"]
talk.example = ".talk what"
talk.with_origin = True
