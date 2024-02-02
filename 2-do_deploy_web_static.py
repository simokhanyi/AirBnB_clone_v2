#!/usr/bin/python3
"""
<<<<<<< HEAD
Fabric script (based on the file 1-pack_web_static.py)
"""

from fabric.api import *
from os.path import exists
from datetime import datetime

env.hosts = ['<IP web-01>', 'IP web-02']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/my_ssh_private_key'  # replace with your private key path


def do_pack():
    """
    Generate a .tgz archive from the contents of the web_static folder.
    Archive will be stored in the "versions" folder.
    Return the archive path if successful, None otherwise.
    """
    try:
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        local('mkdir -p versions')
        file_path = 'versions/web_static_{}.tgz'.format(timestamp)
        local('tar -cvzf {} web_static'.format(file_path))
        return file_path
=======
Creates and distributes an archive to your web
servers, using the function deploy
"""
import os
from datetime import datetime
from fabric.api import *

env.user = "ubuntu"
env.hosts = ["52.86.50.144", "52.3.250.50"]


def do_pack():
    """Compress files from web_static directory"""
    try:
        if not os.path.isdir("versions"):
            os.makedirs("versions")
        date = datetime.now()
        file = "versions/web_static_{0}{1}{2}{3}{4}{5}".format(
            date.year,
            date.month,
            date.day,
            date.hour,
            date.minute,
            date.second
        )
        file += ".tgz"
        local("tar -cvzf {} web_static".format(file))
        return file
>>>>>>> 1c5d4cd4888a8e562d234bafc79dbbd03667ba78
    except Exception:
        return None


def do_deploy(archive_path):
    """
<<<<<<< HEAD
    Distributes an archive to your web servers.
    """
    if not exists(archive_path):
        return False

    try:
        # Upload the archive to the /tmp/ directory of the web server
        put(archive_path, '/tmp/')

        # Extract the archive to the folder /data/web_static/releases/
        archive_filename = archive_path.split('/')[-1]
        folder_name = '/data/web_static/releases/{}'.format(
            archive_filename.split('.')[0])
        run('mkdir -p {}'.format(folder_name))
        run('tar -xzf /tmp/{} -C {}'.format(archive_filename, folder_name))

        # Delete the archive from the web server
        run('rm /tmp/{}'.format(archive_filename))

        # Move contents to the correct folder
        run('mv {}/web_static/* {}'.format(folder_name, folder_name))

        # Remove the unnecessary web_static directory
        run('rm -rf {}/web_static'.format(folder_name))

        # Delete the symbolic link /data/web_static/current from the web server
        run('rm -rf /data/web_static/current')

        # Create a new symbolic link /data/web_static/current
        run('ln -s {} /data/web_static/current'.format(folder_name))

        print('New version deployed!')
        return True

    except Exception as e:
        print(e)
=======
    Deploy archive

    Args:
        - archive_path(str, optional): Path of the archive
    """
    try:
        if not os.path.isfile(archive_path):
            return False
        path = archive_path.split("/")[1]
        name = path.split(".")[0]
        put(archive_path, "/tmp/{0}".format(path))
        run("sudo mkdir -p /data/web_static/releases/{}/".format(name))
        source = "sudo tar -xzf /tmp/{0} -C".format(path)
        dest = "/data/web_static/releases/{0}/".format(name)
        run(source + " " + dest)
        run("sudo rm /tmp/{0}".format(path))
        source = (
            "sudo mv /data/web_static/releases/{0}/web_static/*".format(name)
        )
        dest = "/data/web_static/releases/{0}/".format(name)
        run(source + " " + dest)
        run(
            "sudo rm -rf /data/web_static/releases/{0}/web_static".format(name)
        )
        run("sudo rm -rf /data/web_static/current")
        source = "sudo ln -s /data/web_static/releases/{0}/".format(name)
        dest = "/data/web_static/current"
        run(source + " " + dest)
        return True
    except Exception:
>>>>>>> 1c5d4cd4888a8e562d234bafc79dbbd03667ba78
        return False
