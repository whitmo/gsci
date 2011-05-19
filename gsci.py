from contextlib import contextmanager
from fabric.api import local
from path import path
import argparse
import os
import sys


def main(argv=None):
    if argv is None:
        args = sys.argv
    
    parser = argparse.ArgumentParser(description='Git svn clone something and pip install it')
    parser.add_argument('url', metavar='C',
                        help='truncated url of package to checkout and install')
    parser.add_argument('-i', dest='index', type=str, default="http://yorick:9003/index",
                        help='index to use for dependencies')
    parser.add_argument('-s', dest='svn', type=str, default="svn://svn/s",
                        help='url to svn repo root')
    args = parser.parse_args(argv)
    venv = os.environ.get('VIRTUAL_ENV', None)
    if venv is None:
        raise argparse.ArgumentTypeError("You are not in a virtualenv. Please activate.")
    local('git svn clone -s %s/%s' %(args.svn, args.url))
    with pushd(path(args.url).name):
        local('%(venv)s/bin/pip install -E %(venv)s -i %(index)s -e ./' %dict(venv=venv, index=args.index))


@contextmanager
def pushd(dir):
    '''A context manager (Python 2.5+ only) for stepping into a 
    directory and automatically coming back to the previous one. 
    The original directory is returned. Usage is like this::
    
        from __future__ import with_statement
        # the above line is only needed for Python 2.5
        
        from paver.easy import *
        
        @task
        def my_task():
            with pushd('new/directory') as old_dir:
                ...do stuff...
    '''
    old_dir = os.getcwd()
    os.chdir(dir)
    try:
        yield old_dir
    finally:
        os.chdir(old_dir)
