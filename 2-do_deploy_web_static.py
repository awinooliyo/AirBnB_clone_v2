#!/usr/bin/python3
"""A Fabric Script that distributes archives on web servers"""

from fabric.api import *
from datetime import datetime
from os import path

env.hosts = ['18.215.160.180', '3.95.32.201']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/school'


def do_deploy(archive_path):
    """
    Deploying the  web files to the server
    """
    if not path.exists(archive_path):
        return False
    try:
        if not path.exists(archive_path):
            return False

        # Upload archive
        put(archive_path, '/tmp/')

        # Create target directory
        timestamp = archive_path[-18:-4]
        release_path = ('/data/web_static/releases/web_static_{}/'
                        .format(timestamp))
        run('mkdir -p {}'.format(release_path))

        # Uncompress archive and delete .tgz
        run('tar -xzf /tmp/web_static_{0}.tgz -C {1}'
            .format(timestamp, release_path))
        # Remove archive
        run('rm /tmp/web_static_{0}.tgz'.format(timestamp))

        # Move contents into host web_static
        run('mv {0}/web_static/* {0}/'.format(release_path))

        # Remove extraneous web_static directory
        run('rm -rf {0}/web_static'.format(release_path))

        # Delete pre-existing symbolic link
        run('rm -rf /data/web_static/current')

        # Re-establish symbolic link
        current_path = '/data/web_static/current'
        run('ln -s {0} {1}'.format(release_path, current_path))

        print("New version deployed!")
        return True
    except Exception as e:
        return False
