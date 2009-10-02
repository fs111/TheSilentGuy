# -*- coding: utf-8 -*-
from subprocess import Popen, PIPE

p = Popen(["espeak -s 40  -p 99  -v en "], shell=True,
          stdin=PIPE, stdout=PIPE, close_fds=True)

COMMAND = ".talk"

def sayitoutloud(what):
    p.stdin.write(what + "\n")



def talk(phenny, input):
    input = input.replace(COMMAND, "") 
    sayitoutloud(input)


talk.commands = ["talk"]
talk.example = [".talk what"]
