from collections import deque
import sys

class Directory:
	def __init__(self, name):
		self.name = name
		self.children = {}

class DirectoryManager:

	def __init__(self):
		self.root = Directory("/")

	def find_dir(directory):
		paths = directory.split("/")[:-1]
		curr = DirectoryManager.root
		for p in paths:
			if p not in curr:
				print(f"{p} directory does not exist")
				return 
			curr = curr[p]
		return curr

	def create_directory(self, directory):
		curr = self.find_dir(directory)
		child = directory.split("/")[-1]
		curr[child] = {}

	def move_directory(self, target, location):
		self.create_directory(location)
		self.delete_directory(target)

	def delete_directory(self, directory):
		curr = self.find_dir(directory)
		child = directory.split("/")[-1]
		del curr[child]

	def list_directories(self):
		for name, path in self.root.items():
			print(name, path)

DirectoryManager = DirectoryManager()
DirectoryManager.create_directory("/home")
DirectoryManager.create_directory("/home/user")
DirectoryManager.create_directory("/home/user/documents")
DirectoryManager.list_directories()