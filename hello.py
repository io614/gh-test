import os

# List all files in a directory using os.listdir
basepath = 'my_directory/'
hello = 'world'

def add(num):
  return num+1

add(3)

for entry in os.listdir(basepath):
  if os.path.isfile(os.path.join(basepath, entry)):
    print(entry)
