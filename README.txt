This is a little toy project build in the Hackerspace Brussels (hsbxl)[0], which is basically
a plugin for the phenny[1] IRC bot. espeak [2] is used as the text-to-speech
engine, since that is the easiest to use from python. You create a subprocess
and write to stdin of that process. Right now the plugin it can do two things:

* it announces every user that joins a channel that phenny is connected to
  with the sentence "Dudes, $nick has joined the channel" (this requires some
  hacks in the phenny code base that can be found in the "bot.diff" file

* it defines the ".talk" command which can be used by all admins of the bot to
  force to say custom things


--
[0] http://hackerspace.be/TheSilentGuy
[1] http://inamidst.com/phenny/
[2] http://espeak.sourceforge.net/
