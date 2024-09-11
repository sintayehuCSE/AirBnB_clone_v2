#!/usr/bin/python3
"""A Fabric script that deletes out-of-date archives"""
from fabric.api import *
deploy = __import__('3-deploy_web_static').deploy

def do_clean(number=0):
    """A Fabric task that remove outdated version of
    deployed web-static file in favor of new one
    """
    deploy()
    number = int(number)
    if number == 0:
        number = 1
    else:
        with lcd('./versions'):
            local("ls -lt | tail -n +{} | rev | cut -f1 -d" " | rev | \
            xargs -d '\n' rm".format(1 + number))
        with cd('/data/web_static/releases/'):
            sudo("ls -lt | tail -n +{} | rev | cut -f1 -d" " | rev | \
            xargs -d '\n' rm".format(1 + number))
