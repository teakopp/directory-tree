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

def create_directory(name, path):
	directories[name] = {}
	directories[name][path] = {}

def remove_directory(name):
	del directories[name]

def list_directories():
	for name, path in directories.items():
		print(name, path)

directories["/"] = {"home": {"user": {}, "admin": {}}, "etc": {}, "var": {}}
curr = bfs("user")
print(curr)
curr["thing"] = {}
print(directories)