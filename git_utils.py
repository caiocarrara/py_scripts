# coding: utf-8
import os
import subprocess
from sys import argv

def git_all_subdir(base_dir=".", arguments=[]):
    base_dir_path = os.path.abspath(base_dir)
    for dir in os.listdir(base_dir_path):
        dir_path = os.path.join(base_dir_path, dir)
        if os.path.isdir(dir_path) and not dir.startswith("."):
            if ".git" in os.listdir(dir_path):
                command = ['git', '-C', dir_path]
                command.extend(arguments)
                subprocess.call(command)

if __name__ == "__main__":
    """
    Call git_utils.py passing arguments as passing to a git command.
    For exemple, to call 'git pull' in all subdirectories, execute
    'python git_utils.py pull origin master'. Or, specify a directory to
    execute command. Exemple: 

    python git_utils.py base_dir=../path pull origin master
    """
    base_dir = "."
    base_dir_index = None

    for arg in argv:
        if arg.startswith('base_dir='):
            base_dir_index = argv.index(arg)
            base_dir = arg.split('=')[1]

    if base_dir_index:
        argv.pop(base_dir_index)

    git_all_subdir(base_dir=base_dir, arguments=argv[1:])