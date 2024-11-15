from collections import deque
import sys

directories = {"/": {}}

def find_dir(directory):
	paths = directory.split("/")[:-1]
	curr = directories["/"]
	for p in paths:
		if p not in curr:
			print(f"{p} directory does not exist")
			return 
		curr = curr[p]
	return curr

def create_directory(directory):
	curr = find_dir(directory)
	child = directory.split("/")[-1]
	curr[child] = {}

def move_directory(target, location):
	create_directory(location)
	delete_directory(target)

def delete_directory(directory):
	curr = find_dir(directory)
	child = directory.split("/")[-1]
	del curr[child]

def list_directories():
	for name, path in directories.items():
		print(name, path)

directories["/"] = {"home": {"user": {}, "admin": {}}, "etc": {}, "var": {}}
list_directories()
create_directory("home/user/yep")
list_directories()
move_directory("home/user/yep","home/admin/yep")
list_directories()
create_directory("home/admin/yep/admin")
list_directories()
create_directory("home/admin/yep/admin/yep")
list_directories()