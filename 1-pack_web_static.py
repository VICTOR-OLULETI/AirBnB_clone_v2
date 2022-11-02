#!/usr/bin/python3
"""
this would generate a .tgz file
"""
from datetime import datetime
from fabric.api import run, get, local


def do_pack():
    """
    This function would store all files in web_static in an archive
    """
    dt = datetime.utcnow()
    archive_path = '/versions/web_static_{}{}{}{}{}{}.tgz'.format(
            dt.year,
            dt.month,
            dt.day,
            dt.day,
            dt.hour,
            dt.minute,
            dt.second)
    local("mkdir -p /versions/")
    pack = local("tar -cvzf {} web_static".format(archive_path)
    if (pack.failed):
        return None
    return archive_path
