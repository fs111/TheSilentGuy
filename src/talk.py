# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE

COMMAND = ".talk"

process = Popen(["espeak -s 40  -p 99  -v en "], shell=True,
          stdin=PIPE, stdout=PIPE, close_fds=True)

def sayitoutloud(what):
    """writes the text to the stdin of the espeak process"""
    process.stdin.write(what + "\n")



def talk(phenny, input):
    """Callback that phenny calls when somone issues the .talk command"""
    input = input.replace(COMMAND, "") 
    sayitoutloud(input)


talk.commands = ["talk"]
talk.example = [".talk what"]
