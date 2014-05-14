# coding: utf-8
import os
import subprocess
from sys import argv

def git_all_subdir(base_dir=".", arguments=[]):
	for dir in os.listdir(base_dir):
		if os.path.isdir(dir) and not dir.startswith("."):
			if ".git" in os.listdir(dir):
				command = ['git', '-C', dir]
				command.extend(arguments)
				subprocess.call(command)

if __name__ == "__main__":
	git_all_subdir(arguments=argv[1:])