#!/usr/bin/python3
"""
Fabric script that generates a .tgz archive from the contents
of the web_static folder of the AirBnB Clone repo.
"""
from fabric.api import local
from datetime import datetime


def do_pack():
    """
    Generates a .tgz archive from the contents of the web_static folder.

    Returns:
        str: Path to the created archive, or None if archiving fails.
    """
    try:
        # Create the versions folder if it doesn't exist
        local("mkdir -p versions")

        # Create the archive name using the current timestamp
        time_format = "%Y%m%d%H%M%S"
        archive_name = f"web_static_{datetime.now().strftime(time_format)}.tgz"

        # Compress the contents of the web_static folder
        local("tar -cvzf versions/{} web_static".format(archive_name))

        return "versions/{}".format(archive_name)
    except Exception as e:
        return None

    archive_path = do_pack()
    print("Archive Path:", archive_path)
