from collections import deque
import sys

class Directory:
	def __init__(self, name):
		self.name = name
		self.children = {}

class DirectoryManager:
	def __init__(self):
		self.root = Directory("/")

	def find_parent_dir(self, directory):
		if directory == "/":
			return self.root
		paths = directory.split("/")[:-1]
		curr = self.root
		for p in paths:
			if p not in curr.children:
				print(f"{p} directory does not exist")
				return None
			curr = curr.children[p]
		return curr

	def create_directory(self, directory):
		curr = self.find_parent_dir(directory)
		child = directory.split("/")[-1]
		if child not in curr.children:
			curr.children[child] = Directory(child)
			print(f"{directory} created")
			return True
		print(f"{directory} already exists")
		return False


	def move_directory(self, target, location):
		created = self.create_directory(location)
		if created:
			self.delete_directory(target)
			print(f"{target} moved to {location}")
			return True
		print(f"{target} cannot be moved to {location}")
		return False

	def delete_directory(self, directory):
		curr = self.find_parent_dir(directory)
		child = directory.split("/")[-1]
		del curr.children[child]

	def list_directories(self, directory=None, depth=0):
		if directory is None:
			directory = self.root
		print(" " * depth + directory.name) 
		for child_name in sorted(directory.children): 
			self.list_directories(directory.children[child_name], depth + 1)

def validate_command(command, expected_length):
	if len(command) != expected_length:
		print(f"{' '.join(command)} is an invalid command")
		return False
	return True

if __name__ == "__main__":
	directory_manager = DirectoryManager()
	while True:
		command = input("\nEnter command (CREATE, DELETE, MOVE, LIST, EXIT): ").split()
		action = command[0].upper()
		if action == "CREATE":
			if not validate_command(command, 2):
				continue
			directory_manager.create_directory(command[1])
		elif action == "DELETE":
			if not validate_command(command, 2):
				continue
			directory_manager.delete_directory(command[1])
		elif action == "MOVE":
			if not validate_command(command, 3):
				continue
			directory_manager.move_directory(command[1], command[2])
		elif action == "LIST":
			if not validate_command(command, 1):
				continue
			directory_manager.list_directories()
		elif action == "EXIT":
			print("Exiting program")
			exit()
		else:
			print(f"{" ".join(command)} is an invalid command")
			continue