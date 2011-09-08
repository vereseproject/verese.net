#
# Fabric script to deploy website
#
#
# examples
# ~$ fab deploy

import os
from time import strftime

from fabric.api import env, run, local, cd

env.user = "verese"
env.hosts = ["beta.verese.net:2222"]
env.backup_dir = "/home/verese/backup/verese.net"
env.remote_repo_dir = "/home/verese/repositories/verese.net.git"
env.remote_app_dir = "/home/verese/public_html/"

def update_code():
    """
    Push code to server
    Update server instance
    """

    local("git pull origin master")
    local("git push origin master")

def backup():
    """
    Backup
    """
    date = strftime("%Y%m%d%H%M")

    with cd(os.path.join(env.remote_app_dir, '..')):
        run("tar czf %s/verese-%s.tar.gz public_html" %
            (env.backup_dir, date)
            )

def deploy(do_update_code=True, do_backup=False):
    if do_update_code == True:
        update_code()

    if do_backup == True:
        backup()

    with cd(env.remote_app_dir):
        run("git pull origin master")

