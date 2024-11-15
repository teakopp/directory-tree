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
		queue.append(self.root, 0)
		while queue:
			curr, depth = queue.popleft()
			print(" " * depth + curr.name)
			for child in curr.children:
				queue.append(curr.children[child], depth + 1)


if __name__ == "__main__":
	directory_manager = DirectoryManager()
	while True:
		command = input("\nEnter command (CREATE, DELETE, MOVE, LIST, EXIT): ").split()
		if command[0] == "CREATE":
			directory_manager.create_directory(command[1])
		elif command[0] == "DELETE":
			directory_manager.delete_directory(command[1])
		elif command[0] == "MOVE":
			directory_manager.move_directory(command[1], command[2])
		elif command[0] == "LIST":
			directory_manager.list_directories()
		elif command[0] == "EXIT":
			print("Exiting program")
			exit()