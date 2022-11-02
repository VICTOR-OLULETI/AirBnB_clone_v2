#!/usr/bin/python3
# this would generate a .tgz file
from datetime import datetime
from fabric.operations import run, get
name = 'web_static' + datetime.now().hour() + datetime.now().minute + datetime.now().second() + '.tgz'
def do_pack():
    archive_path = "/versions/" + name
    run("mkdir -p /versions/")
    get(remote_path="/web/static/*", local_path="/versions/"+ name)
    return archive_path
