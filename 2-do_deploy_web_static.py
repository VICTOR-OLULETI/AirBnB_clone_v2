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
    if os.path.exists(archive_path) is False:
        return (False)
    try:
        filename = archive_path.split('/')[-1]
        put(archive_path, "/tmp/")
        file = filename.split('.')[0]
        release_path = '/data/web_static/releases/{}/'.format(file)
        run('mkdir -p /data/web_static/releases/' + file)
        run('tar -xzf /tmp/{} -C {}'.format(filename, release_path))
        run('rm /tmp/{}'.format(filename))
        run('mv {}web_static/* {}'.format(release_path))
        run('rm -rf {}web_static'.format(release_path))
        run('rm -rf /data/web_static/current')
        run('ln -s {} /data/web_static/current'.format(release_path))
        print("New version deployed!")
    except:
        return (False)
    return (True)
