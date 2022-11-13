#!/usr/bin/python3
# Deleting archives
import os
from fabric.api import *


def do_clean(number=0):
    """
	Deletes out dated archives.
    	Args:
	number: number of archives to keep
    """
    env.hosts = ['44.210.78.253', '54.160.124.52']
    number = 1 if int(number) == 0 else int(number)
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]

    with cd("/data/web_static/releases"):
	archives = run("ls -tr").split()
	archives = [a for a in archives if "web_static_" in a]
	[archives.pop() for i in range(number)]
	[run("rm -rf ./{}".format(a)) for a in archives]
