import os

def check_create_dir(dirpath):
	if not os.path.exists(dirpath):
		os.makedirs(dirpath)

def write(filename, data):
	with open(filename, 'w+') as outfile:
		outfile.write(data)