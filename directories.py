from collections import deque
import sys

class Directory:
	def __init__(self, name):
		self.name = name
		self.children = {}

class DirectoryManager:

	def __init__(self):
		self.root = Directory("/")

	def find_dir(self, directory):
		paths = directory.split("/")[:-1]
		curr = self.root
		for p in paths:
			if p not in curr.children:
				print(f"{p} directory does not exist")
				return 
			curr = curr.children[p]
		return curr

	def create_directory(self, directory):
		curr = self.find_dir(directory)
		child = directory.split("/")[-1]
		curr.children[child] = Directory(child)

	def move_directory(self, target, location):
		self.create_directory(location)
		self.delete_directory(target)

	def delete_directory(self, directory):
		curr = self.find_dir(directory)
		child = directory.split("/")[-1]
		del curr[child]

	def list_directories(self):
		queue = deque()
		queue.append(self.root)
		while queue:
			curr = queue.popleft()
			print(curr.name)
			for child in curr.children:
				queue.append(curr.children[child])

DirectoryManager = DirectoryManager()
DirectoryManager.create_directory("home")
DirectoryManager.create_directory("home/user")
DirectoryManager.create_directory("home/user/documents")
DirectoryManager.list_directories()