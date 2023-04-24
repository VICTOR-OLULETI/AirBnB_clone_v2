#!/usr/bin/python3
# Deleting archives
import os
from fabric.api import *

env.hosts = ['35.153.232.12', '18.234.253.65']


def do_clean(number=0):
    """ Deletes out dated archives.
    Args:
    number: number of archives to keep
    """
    env.hosts = ['35.153.232.12', '18.234.253.65']
    # number = 1 if int(number) == 0 else int(number)
    if int(number) == 0:
        number = 1
    else:
        number = int(number)
    archives = sorted(os.listdir("versions"))
    [archives.pop() for i in range(number)]
    with lcd("versions"):
        [local("rm ./{}".format(a)) for a in archives]
    # with lcd("versions"):
    #    archives = run("ls -tr").split()
    #    archives = [a for a in archives if "web_static_" in a]
    #    [archives.pop() for i in range(number)]
    #    for i in archives:
    #        sudo("rm -rf ./{}".format(i))

    with cd("/data/web_static/releases"):
        archives = run("ls -tr").split()
        archives = [a for a in archives if "web_static_" in a]
        [archives.pop() for i in range(number)]
        [sudo("rm -rf ./{}".format(a)) for a in archives]
