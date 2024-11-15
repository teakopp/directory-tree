# Directory tree

## Description
A project to manage directories (without actually altering any real directories) using a series of commands.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)

## Installation 
To install this project, clone the repository and that's it! There are no external dependencies just make sure you have python 3 installed.

[Steps to install Python 3](https://docs.python.org/3/using/index.html)

```bash
git clone https://github.com/yourusername/project-name.git
cd directory-tree
```


## Usage
Once installed, make sure you’re in the correct directory (`directory-tree`) and then run the script using one of the following commands, depending on your system:

```
python directories.py    # For Windows or Linux
python3 directories.py   # For macOS
```


The following commands are available for managing the directory tree:
### `CREATE`
- **Usage**: `CREATE <directory>`
- **Description**: Creates a directory at the specified path. The directory must not already exist.

### `MOVE`
- **Usage**: `MOVE <source> <destination>`
- **Description**: Moves a directory from one location to another. Both the source and destination directories must exist.

### `DELETE`
- **Usage**: `DELETE <directory>`
- **Description**: Deletes the specified directory. The directory must exist and cannot be the root directory.

### `LIST`
- **Usage**: `LIST`
- **Description**: Lists all directories and their children, showing the structure in a tree-like format. Indentation indicates the depth of each directory relative to the root.


Examples:
### Example 1: Create Directories
```
CREATE howdy
CREATE howdy/partner
CREATE hello
```

### Example 2: Move a Directory
```
CREATE howdy
CREATE howdy/partner
CREATE hello
```

### Example 3: Delete a Directory
```
DELETE howdy
```

### Example 4: List Directories
```
LIST

```

Output:

```
hello
howdy
  partner

```
