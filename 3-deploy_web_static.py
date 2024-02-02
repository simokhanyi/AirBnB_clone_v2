#!/usr/bin/python3
"""
Fabric script that creates and distributes an archive to your web servers
"""
from fabric.api import local, run, put, env
from os.path import exists
from datetime import datetime

env.hosts = ['<IP web-01>', '<IP web-02>']


def do_pack():
    """
    Create a compressed archive of web_static contents
    """
    try:
        current_time = datetime.utcnow().strftime("%Y%m%d%H%M%S")
        local("mkdir -p versions")
        filename = "versions/web_static_{}.tgz".format(current_time)
        local("tar -cvzf {} web_static".format(filename))
        return filename
    except Exception as e:
        return None


def do_deploy(archive_path):
    """
    Distribute an archive to your web servers
    """
    if not exists(archive_path):
        return False

    try:
        archive_filename = archive_path.split("/")[-1][:-4]
        put(archive_path, "/tmp/")
        run("mkdir -p /data/web_static/releases/{}/".format(archive_filename))
        run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/".format(
            archive_filename, archive_filename))
        run("rm /tmp/{}.tgz".format(archive_filename))
        run("mv /data/web_static/releases/{}/web_static/* "
            "/data/web_static/releases/{}/".format(
                archive_filename, archive_filename))
        run("rm -rf /data/web_static/releases/{}/web_static".format(
            archive_filename))
        run("rm -rf /data/web_static/current")
        run("ln -s /data/web_static/releases/{}/ "
            "/data/web_static/current".format(archive_filename))
        return True
    except Exception as e:
        return False


def deploy():
    """
    Deploy the web_static content to your web servers
    """
    archive_path = do_pack()
    if archive_path is None:
        return False
    return do_deploy(archive_path)
