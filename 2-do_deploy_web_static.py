#!/usr/bin/python3
""" A Fabric script that deploy web static archive file
  to a remote web-servers"""
from fabric.api import *
env.user = "ubuntu"
env.hosts = ['100.25.33.79', '34.227.101.79']


def do_deploy(archive_path):
    """A Fabric task that depolya static archive file
    to a remote servers
    """
    try:
        if not archive_path:
            return False
        else:
            archive_name = archive_path[archive_path.find('/') + 1:]
            filename = archive_name[:archive_name.find('.')]
            put(archive_path, '/tmp/')
            sudo('mkdir -p /data/web_static/releases/{}'.format(filename))
            sudo('tar -xzf /tmp/{} -C /data/web_static/releases/{}'
                 .format(archive_name, filename))
            sudo('rm -rf /tmp/{}'.format(archive_name))
            dst = '/data/web_static/releases/{}/'.format(filename)
            sudo('mv /data/web_static/releases/{}/web_static/* {}'.
                 format(filename, dst))
            sudo('rm -rf /data/web_static/releases/{}/web_static'.
                 format(filename))
            sudo('rm -rf /data/web_static/current')
            target = '/data/web_static/releases/{}'.format(filename)
            sudo('ln -s {} /data/web_static/current'.format(target))
            return True
    except:
        return False
