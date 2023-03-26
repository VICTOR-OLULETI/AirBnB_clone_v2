#!/usr/bin/python3
"""
This script deploys archive in web server
"""
import os.path
from fabric.api import *
import shlex
import os


env.user = 'ubuntu'
env.hosts = ['54.197.82.68', '54.237.1.122']

def do_deploy(archive_path):
    """ Deploys """
    #env.user = 'ubuntu'
    #env.hosts = ['54.197.82.68', '54.237.1.122']
    if not os.path.exists(archive_path):
        return False
    try:
        name = archive_path.replace('/', ' ')
        name = shlex.split(name)
        name = name[-1]

        wname = name.replace('.', ' ')
        wname = shlex.split(wname)
        wname = wname[0]

        releases_path = "/data/web_static/releases/{}/".format(wname)
        tmp_path = "/tmp/{}".format(name)

        put(archive_path, "/tmp/")
        sudo("mkdir -p {}".format(releases_path))
        sudo("tar -xzf {} -C {}".format(tmp_path, releases_path))
        sudo("rm {}".format(tmp_path))
        sudo("mv {}web_static/* {}".format(releases_path, releases_path))
        sudo("rm -rf {}web_static".format(releases_path))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except ValueError:
        return False
