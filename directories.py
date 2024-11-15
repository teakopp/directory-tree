import sys

directories = {"/": {}}

def _split_dir(directory):
	paths = directory.split("/")
	print(paths[-2])
	# If there are less than 2 paths it means that the directory is in the root
	if len(paths) < 2:
		return ["/", paths[-1]]
	return paths[-2:]

def bfs(directory):
	visited = set()
	queue = [("/", directories["/"])]
	visited.add("/")
	while queue:
		curr_dir, curr_path = queue.pop()
		if curr_dir == directory:
			return curr_path
		for name, path in curr_path.items():
			if name not in visited:
				visited.add(name)
				queue.append((name, path))
	return None

def create_directory(directory):
	parent, child = _split_dir(directory)
	print(parent, child)

	curr = bfs(parent)
	if not curr:
		print("Parent directory does not exist")
		return
	
	curr[child] = {}


def delete_directory(directory):
	parent, child = _split_dir(directory)
	curr = bfs(parent)	
	del curr[child]

def list_directories():
	for name, path in directories.items():
		print(name, path)

directories["/"] = {"home": {"user": {}, "admin": {}}, "etc": {}, "var": {}}
curr = bfs("user")
curr["thing"] = {}
create_directory("home/user/yep")
