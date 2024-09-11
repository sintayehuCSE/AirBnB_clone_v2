#!/usr/bin/python3
"""Fabric script that generates a .tgz archive from the contents of the
web_static folder contained AirBnB Clone repo, using the function do_pack"""
from time import strftime
from fabric.api import local


def do_pack():
    """A Fabric task that generate archive file for the web_static folder of
    AirBnB clone project"""
    try:
        local("mkdir -p versions")
        timenow = strftime("%Y%m%d%I%M%S")
        archive_name = "web_static_{}.tgz".format(timenow)
        local("tar -czvf versions/{} web_static".format(archive_name))
        return "versions/{}".format(archive_name)
    except:
        return None
