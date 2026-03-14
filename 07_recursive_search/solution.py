# Напиши решение здесь
import os

# Find all .txt files in project folder (including subfolders)
txt_files = []
for root, dirs, files in os.walk('project'):
    for file in files:
        if file.endswith('.txt'):
            txt_files.append(file)

# Write file names to found.txt
with open('found.txt', 'w') as f:
    f.write('\n'.join(txt_files))
