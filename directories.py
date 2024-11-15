import sys

directories = {"/": {}}

def bfs(directory):
	visited = set()
	queue = []
	queue.append("/")
	visited.add("/")
	while queue:
		curr_dir = queue.pop()
		if curr_dir == directory:
			return curr_dir
		print(curr_dir)
		for name, path in directories[curr_dir].items():
			print(name, path)
			if path not in visited:
				visited.add(path)
				queue.append(path)
	return None

def create_directory(name, path):
	directories[name] = {path}

def remove_directory(name):
	del directories[name]

def list_directories():
	for name, path in directories.items():
		print(name, path)

directories["/"] = { "/" : {"/"}, "home": "/home", "etc": "/etc", "var": "/var"}
directories["/"]["home"] = {"user": {"/"}, "admin": {"/"}}
curr = bfs("user")
