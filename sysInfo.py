#!/usr/bin/env python
#A system info gathering script

import subprocess

uname = "uname"
uname_arg = "-a"
print "Gathering system information with %s command:\n" % uname
subprocess.call([uname, uname_arg])
