import sys

directories = {"/": {}}


def bfs(directory):
	visited = set()
	queue = [("/", directories["/"])]
	visited.add("/")
	while queue:
		curr_dir, curr_path = queue.pop()
		if curr_dir == directory:
			return curr_path
		for name, path in curr_path.items():
			print(name,path)
			if name not in visited:
				visited.add(name)
				queue.append((name, path))
	return None

def create_directory(directory):
	paths = directory.split("/")
	# If there are less than 2 paths it means that the directory is in the root
	if len(paths) <2:
		parent = paths[-2]
		child = paths[-1]
	else:
		parent = "/"
		child = paths

	curr = bfs(parent)
	curr[child] = {}


def remove_directory(name):
	del directories[name]

def list_directories():
	for name, path in directories.items():
		print(name, path)

directories["/"] = {"home": {"user": {}, "admin": {}}, "etc": {}, "var": {}}
curr = bfs("user")
curr["thing"] = {}
create_directory("home/user/yep")
create_directory("hi")
print(directories)