#!/usr/bin/python3
"""Fabric script that distributes an archive to your web
servers using do_deploy"""

from fabric.api import env, put, run
from os.path import exists
from datetime import datetime

env.hosts = ['<IP web-01>', 'IP web-02']
env.user = '<your_username>'
env.key_filename = '<path_to_your_private_key>'


def do_deploy(archive_path):
    """Distributes an archive to the web servers"""

    # Check if the archive exists
    if not exists(archive_path):
        return False

    # Get the archive filename without extension
    archive_filename = archive_path.split("/")[-1][:-4]

    # Upload the archive to the /tmp/ directory of the web server
    put(archive_path, "/tmp/")

    # Create the release directory
    run("mkdir -p /data/web_static/releases/{}".format(archive_filename))

    # Uncompress the archive to the release directory
    run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format(
        archive_filename, archive_filename))

    # Delete the archive from the web server
    run("rm /tmp/{}.tgz".format(archive_filename))

    # Move the contents of the release directory to the web_static directory
    run("mv /data/web_static/releases/{}/web_static/* "
        "/data/web_static/releases/{}/".format(
            archive_filename, archive_filename))

    # Delete the old symbolic link
    run("rm -rf /data/web_static/current")

    # Create a new symbolic link
    run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(
        archive_filename))

    print("New version deployed!")

    return True


if __name__ == "__main__":
    # Example usage:
    do_deploy("versions/web_static_20170315003959.tgz")
