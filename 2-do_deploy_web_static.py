#!/usr/bin/python3
"""
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
    except Exception:
        return None


def do_deploy(archive_path):
    """
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
        return False
