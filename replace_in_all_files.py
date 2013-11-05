# coding: utf-8
import os
from sys import argv

def replace_in_all_files(parent_folder_path, oldChar, newChar):
	"""Replace the oldChar for newChar in all text
	files found in parent_folder_path and its children
	directories.
	"""
	filenames = os.listdir(parent_folder_path)
	
	for filename in filenames:
		filename = os.path.join(parent_folder_path, filename)
		
		if os.path.isdir(filename):
			replace_in_all_files(filename, oldChar, newChar)
		else:
			arq = open(os.path.join(parent_folder_path, filename), 'r')
			oldContent = arq.readlines()
			arq.close()
			
			arq = open(os.path.join(parent_folder_path, filename), 'w')
			newContent = ""
			for line in oldContent:
				newContent += line.replace(oldChar, newChar) 
			arq.write(newContent)
			arq.close()
			print "OK: " + filename

if __name__ == "__main__":
	if len(argv) < 3:
		print "You need to inform all params: rootPath, oldChar, newChar"
	else:
		rootPath = str(argv[1])
		oldChar = str(argv[2])
		newChar = str(argv[3])
		replace_in_all_files(rootPath, oldChar, newChar)
