#!/usr/bin/python3
"""A Fabric script that creates a archive file and ship it to a
   remote web-servers"""
do_pack = __import__('1-pack_web_static').do_pack
do_deploy = __import__('2-do_deploy_web_static').do_deploy


def deploy():
    """A Fabric task that create and deploy archive file
    to a web servers.
    """
    archive_path = do_pack()
    if archive_path:
        return(do_deploy(archive_path))
    else:
        return False
