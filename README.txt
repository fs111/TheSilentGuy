Welcome to TheSilentGuy, a talking (as in sound) IRC bot.

It is a little toy project build in the Hackerspace Brussels (hsbxl)[0], which
is basically a plugin for the phenny[1] IRC bot. espeak [2] is used as the
text-to-speech engine, since that is the easiest to use from python. You create
a subprocess and write to stdin of that process. Right now the plugin can do
two things:

* it announces every user that joins a channel that phenny is connected to
  with the sentence "Dudes, $nick has joined the channel" (this requires some
  changes in the phenny code base that can be found in the "patches" directory

* it defines the ".talk" command which can be used by all admins of the bot to
  force to say custom things

The license of this module is the MIT license (see COPYING.txt)

To patch phenny to be able to use the module download the latest phenny from
[1] go into the toplevel directory and run:

patch -p0 < patches/phenny-bot-username-access-in-plugins.patch

In case you want to run phenny on IPv6, and srsly who does not? you can also
apply the patch for IPv6 connectivity (only). Thanks to askarel (check out
askarel.be) for the IPv6 patch.

patch -p0 < patches/phenny-bot-IPv6-patch_irc.py.patch

after that add the "src" dir to the "extra" list like so:

extra = ['/path/to/TheSilentGuy/src']

Now all people configured as admins are able to use ".talk" command.


--
[0] http://hackerspace.be/TheSilentGuy
[1] http://inamidst.com/phenny/
[2] http://espeak.sourceforge.net/
