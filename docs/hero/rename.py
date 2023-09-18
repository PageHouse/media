# alright so basically im lazy and whoever did this before MANUALLY renamed all the photos ???

import os

cwd = os.getcwd()

files = os.listdir(cwd)

num_files = len(files) - 1

for i in range(num_files):
    file_name = files[i]
    new_file_name = str(i).zfill(4) + '.jpg'
    os.rename(file_name, new_file_name)

