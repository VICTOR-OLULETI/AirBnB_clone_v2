#!/usr/bin/python3
"""
This script deploys archive in web server
"""
import os.path
from fabric.api import run, put

def do_deploy(archive_path):
    """
    This deploys the archive file in the web server
    """
    env.user = 'ubuntu'
    env.hosts = ['44.210.78.253', '54.160.124.52']
    if os.path.isdir(archive_path) is False:
        return (False)
    filename = archive_path.split('/')[-1]
    put(archive_path, "/tmp/" + filename)
    file = filename.split('.')[0]
    run('mkdir -p /data/web_static/releases/' + file)
    run('tar -xzf /tmp/{} -C /data/web_static/releases/{}'.format(filename, file))
    run('rm /tmp/{}'.format(filename))
    run('rm -rf /data/web_static/current')
    run('ln -s /data/web_static/releases/{} /data/web_static/current'.format(file))
    return (True)
