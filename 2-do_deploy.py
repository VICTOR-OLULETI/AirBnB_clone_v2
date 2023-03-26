#!/usr/bin/python3
#Fabric script that distributes an archive to your web servers
import os.path
from fabric.api import *

def do_deploy(archive_path):
    if !os.path.exists(archive_path):
        return False
    put(archive_path, '/tmp/')
    archive_tmp = archive_path.split('/')[-1]
    archive = archive_tmp.split('.')[0]
    path_archive = '/data/web_static/releases/' + archive
    remote_path = '/tmp/' + archive_tmp
    run("tar -xzvf {} {}".format(remote_path, path_archive))
