#!/usr/bin/env python
#sysInfo.py
#Page 14, "Pyton for Unix/Linux Sys Admin"
#A system info gathering script

import subprocess

def uname_func():

    uname = "uname"
    uname_arg = "-a"
    print "Gathering system information with %s command:\n" % uname
    subprocess.call([uname, uname_arg])

def disk_func():

    diskspace = "df"
    diskspace_arg = "-a"
    print "Gathering diskspace information %s command:\n" % diskspace
    subprocess.call([diskspace, diskspace_arg])


def main():
    uname_func()
    disk_func()

main()
