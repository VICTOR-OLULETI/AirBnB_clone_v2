#!/usr/bin/python3
"""
this would generate a .tgz file
"""
from datetime import datetime
from fabric.operations import run, get
name = 'web_static' + datetime.now().hour()
+ datetime.now().minute +
datetime.now().second() + '.tgz'


def do_pack():
    """
    This function would store all files in web_static in an archive
    """
    archive_path = "/versions/" + name
    run("mkdir -p /versions/")
    get(remote_path="/web/static/*", local_path="/versions/" + name)
    return archive_path
