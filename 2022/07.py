# Read input data
with open("07.txt", "r") as input:
  data = input.read().splitlines()

# Class definitions:
class folder:
  def __init__(self, name, parent):
    self.name = name
    self.parent = parent
    self.size = 0
    self.subfolders = []
    self.files = []
  def add_subfolder(self, folder_name):
    new_sub = folder(folder_name, self)
    self.subfolders.append(new_sub)
  def add_file(self, file_name, file_size):
    new_file = file(file_name, file_size)
    self.files.append(new_file)
  def get_size(self):
    self.size = 0                       # reset size
    for file in self.files:
      self.size += file.size            # add file sizes to folder size
    for subfolder in self.subfolders:
      self.size += subfolder.get_size() # add folder sizes to folder size
    return self.size

class file:
  def __init__(self, name, size):
    self.name = name
    self.size = size

# Create folder & file structure:
root_folder = folder("/", None)
current_folder = root_folder
for line in data:
  line = line.split()
  if line[0] == "$":
    if line[1] == "cd":
      if line[2] == "/":
        current_folder = root_folder
        continue
      elif line[2] == "..":
        current_folder = current_folder.parent
        continue
      else:
        for dir in current_folder.subfolders:
          if dir.name == line[2]:
            current_folder = dir
            continue
    if line[1] == "ls":
      continue
  elif line[0] == "dir":
    current_folder.add_subfolder(line[1])
  elif line[0].isnumeric():
     current_folder.add_file(line[1], int(line[0]))
root_folder.get_size()    

# Solution:
solution = [0, 99999999]
free_space = 70000000 - root_folder.size
min_delete = 30000000 - free_space
def solve(dir):
  global solution
  for sub_dir in dir.subfolders:
    if sub_dir.size <= 100000:
      solution[0] += sub_dir.size
    solve(sub_dir)
    if (sub_dir.size >= min_delete) and (sub_dir.size < solution[1]):
      solution[1] = sub_dir.size 
solve(root_folder)
print(solution[0])
print(solution[1])