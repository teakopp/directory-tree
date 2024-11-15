from collections import deque
import sys

directories = {"/": {}}

def bfs(paths):
	curr = directories["/"]
	print(paths)
	for p in paths:
		if p not in curr:
			print(f"{p} directory does not exist")
			return False
		curr = curr[p]
	return curr

def create_directory(directory):
	paths = directory.split("/")
	curr = bfs(paths[:-1])
	child = paths[-1]
	curr[child] = {}

def move_directory(target, location):
	created = create_directory(f"{location}/{target_child}")
	deleted = delete_directory(target)
	print(f"Created: {created}, Deleted: {deleted}")
	if not created or not deleted:
		print("Directory could not be moved")
		return False
	return True


def delete_directory(directory):
	parent, child = _split_dir(directory)
	curr = bfs(parent)
	if child not in curr:
		print(f"{child} directory does not exist. It cannot be deleted")
		return	False
	del curr[child]
	return True

def list_directories():
	for name, path in directories.items():
		print(name, path)

directories["/"] = {"home": {"user": {}, "admin": {}}, "etc": {}, "var": {}}
list_directories()
create_directory("home/user/yep")
list_directories()