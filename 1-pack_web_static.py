#!/usr/bin/python3
"""
<<<<<<< HEAD
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
=======
Generates a .tgz archive from the contents of
the web_static folder of your AirBnB Clone repo,
using the function do_pack
"""
import os
from datetime import datetime
from fabric.api import local


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
    except FileNotFoundError:
        print("Error: Unable to find specified directory.")
        return None
>>>>>>> 1c5d4cd4888a8e562d234bafc79dbbd03667ba78
