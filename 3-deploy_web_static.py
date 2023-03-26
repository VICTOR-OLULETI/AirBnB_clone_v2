#!/usr/bin/python3
"""
This script deploys archive in web server
"""
import os.path
from fabric.api import *
import shlex
import os
from datetime import datetime

env.user = 'ubuntu'
env.hosts = ['54.197.82.68', '54.237.1.122']


def do_pack():
    """
    This function would store all files in web_static in an archive
    """
    dt = datetime.utcnow()
    archive_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
            dt.year,
            dt.month,
            dt.day,
            dt.hour,
            dt.minute,
            dt.second)

    if os.path.isdir("versions") is False:
        if local("mkdir -p versions").failed is True:
            return None
    if local("tar -cvzf {} web_static".format(archive_file)).failed is True:
        return None
    return archive_file


def do_deploy(archive_path):
    """ Deploys """
<<<<<<< HEAD
    #env.user = 'ubuntu'
    #env.hosts = ['54.197.82.68', '54.237.1.122']
=======
    env.user = 'ubuntu'
    env.hosts = ['44.210.78.253', '54.160.124.52']
>>>>>>> e2888f1c0fa8e51ad795a41caf05a9f181e3adbd
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
<<<<<<< HEAD
        sudo("mkdir -p {}".format(releases_path))
        sudo("tar -xzf {} -C {}".format(tmp_path, releases_path))
        sudo("rm {}".format(tmp_path))
        sudo("mv {}web_static/* {}".format(releases_path, releases_path))
        sudo("rm -rf {}web_static".format(releases_path))
        sudo("rm -rf /data/web_static/current")
        sudo("ln -s {} /data/web_static/current".format(releases_path))
=======
        run("mkdir -p {}".format(releases_path))
        run("tar -xzf {} -C {}".format(tmp_path, releases_path))
        run("rm {}".format(tmp_path))
        run("mv {}web_static/* {}".format(releases_path, releases_path))
        run("rm -rf {}web_static".format(releases_path))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(releases_path))
>>>>>>> e2888f1c0fa8e51ad795a41caf05a9f181e3adbd
        print("New version deployed!")
        return True
    except ValueError:
        return False


def deploy():
<<<<<<< HEAD
=======
    """add all files in static to archive and deploys it on remote servers"""
>>>>>>> e2888f1c0fa8e51ad795a41caf05a9f181e3adbd
    archive_path = do_pack()
    if not archive_path:
        return False
    return (do_deploy(archive_path))