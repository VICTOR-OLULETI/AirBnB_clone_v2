#!/usr/bin/python3
"""
this would generate a .tgz file
"""
import os.path
from datetime import datetime
# from fabric import *
from fabric.api import run, get, local


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
