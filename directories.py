class Directory:
	def __init__(self, name):
		self.name = name
		self.children = {}

class DirectoryManager:
	def __init__(self):
		self.root = Directory("/")

	def __find_parent_dir(self, directory):
		# If directory is "/" it's root
		if directory == "/":
			return self.root
		# Split the directory path by "/" and remove the last
		# because we're only interested in parent directory
		paths = directory.split("/")[:-1]
		# Start at the root
		curr = self.root
		# Traverse the path to find the parent directory
		# Like a Trie
		for p in paths:
			if p not in curr.children:
				print(f"{p} directory does not exist")
				return None
			curr = curr.children[p]
		return curr
	
	def __find_dir(self, directory):
		# Use find_parent so we don't have to repeat code
		curr = self.__find_parent_dir(directory)
		if curr is None:
			return None
		# Get the last part of the directory path
		# This is the child directory we're looking for
		child = directory.split("/")[-1]
		# If the child directory is not in the parent directory
		if child not in curr.children:
			# Print error message and return None
			print(f"{directory} directory does not exist")
			return None
		# Return the child directory
		# so other functions can use it
		return curr.children[child]

	def create_directory(self, directory):
		parent_dir = self.__find_parent_dir(directory)
		if parent_dir is None:
			return False
		# Last par of directory is the child directory we're creating
		child = directory.split("/")[-1]
		if child not in parent_dir.children:
			# Create the child directory in the parent directory
			parent_dir.children[child] = Directory(child)
			print(f"{directory} created")
			return True
		print(f"{directory} already exists")
		return False

	def move_directory(self, target, location):
		# check if both target and location exist
		# because if either doesn't exist, we should return False early
		target_dir_parent = self.__find_parent_dir(target)
		location_dir = self.__find_dir(location)

		target_child = target.split("/")[-1]

		if target_child not in target_dir_parent.children:
			print(f"{target} does not exist")
			return False
		
		if target_child in location_dir.children:
			print(f"{location} already exists")
			return False
		
		# Move the target directory to the location directory
		target_directory = target_dir_parent.children.pop(target_child)
		location_dir.children[target_child] = target_directory

		print(f"{target} moved to {location}")

		return True

	def delete_directory(self, directory):
		# Make sure the directory exists before we delete it
		parent_dir = self.__find_parent_dir(directory)
		if parent_dir is None:
			print(f"Can't delete directory, Parent directory does not exist")
			return False
		# split off child directory so we can check if it's in parent
		# before we delete it
		child = directory.split("/")[-1]
		if child not in parent_dir.children:
			print(f"Can't delete directory. {directory} does not exist")
			return False
		del parent_dir.children[child]
		return True

	def list_directories(self, directory=None, depth=0):
		# If directory is None, we're starting at the root
		if directory is None:
			directory = self.root
		print(" " * depth + directory.name) 
		# Recursively list all child directories
		# but add +1 depth each time so we can print the correct number of spaces
		# and make it look nice
		for child_name in sorted(directory.children): 
			self.list_directories(directory.children[child_name], depth + 1)
		

def validate_command(command, expected_length):
	# Check if the command has the expected number of arguments
	if len(command) != expected_length:
		print(f"{' '.join(command)} is an invalid command")
		return False
	return True

if __name__ == "__main__":
	directory_manager = DirectoryManager()
	while True:
		# Get user input and split it into a list
		command = input("\nEnter command (CREATE, DELETE, MOVE, LIST, EXIT): ").split()
		# Get the first part of the command to determine what action
		# convert to upper case for case insensitivity because it's easier to use (in my opinion)
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
			# If the command is not recognized, print an error message
			print(f"{" ".join(command)} is an invalid command")
			continue