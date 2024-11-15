from collections import deque
import sys

directories = {"/": {}}

def _split_dir(directory):
	paths = directory.split("/")
	# If there are less than 2 paths it means that the directory is in the root
	if len(paths) < 2:
		return ["/", paths[-1]]
	return paths[-2:]

def bfs(directory):
	paths =  _split_dir(directory)
	for p in paths:
		print(p)
	
	return None
def create_directory(directory):
	parent, child = _split_dir(directory)

	print(parent, child)
	curr = bfs(parent)
	if not curr:
		print("Parent directory does not exist")
		return False
	
	curr[child] = {}
	return True

def move_directory(target, location):
	target_parent, target_child = _split_dir(target)
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
curr = bfs("user")
curr["thing"] = {}
create_directory("home/user/yep")
list_directories()
delete_directory("home/user/yep")
list_directories()
move_directory("home/user", "home/admin")
list_directories()
