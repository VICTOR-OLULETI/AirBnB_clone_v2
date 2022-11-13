#!/usr/bin/python3
# Fabfile to:
#   - update the remote system(s)
#   - download and install an application

# Import Fabric's API module
# Set the password
# env.password = "passwd"
from fabric.api import run
def host_type():
    run('uname -s')
