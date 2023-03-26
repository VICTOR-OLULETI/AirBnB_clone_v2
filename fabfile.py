#from fabric import Connection, task
import shlex
import os
from fabric import *
from fabric.operations import *

@task
def deploy(c, archive_path='versions/web_static_2023320103148.tgz'):
    """Deploys the web_static content"""
    c.user = 'ubuntu'
    c.hosts = ['54.197.82.68', '54.237.1.122']
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

        c.put(archive_path, "/tmp/")
        c.run("mkdir -p {}".format(releases_path))
        c.run("tar -xzf {} -C {}".format(tmp_path, releases_path))
        c.run("rm {}".format(tmp_path))
        c.run("mv {}web_static/* {}".format(releases_path, releases_path))
        c.run("rm -rf {}web_static".format(releases_path))
        c.run("rm -rf /data/web_static/current")
        c.run("ln -s {} /data/web_static/current".format(releases_path))
        print("New version deployed!")
        return True
    except ValueError:
        return False

