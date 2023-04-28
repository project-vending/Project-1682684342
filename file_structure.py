 
import os

# Define the directory structure
folders = ['data', 'logs', 'src']
files = {'data': ['raw_data', 'processed_data'], 'logs': ['log.txt'], 'src': ['main.py', 'config.py']}

# Create the folders and files
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    for file in files.get(folder, []):
        with open(os.path.join(folder, file), 'w') as f:
            pass

# Print the directory structure
for folder in folders:
    print(folder)
    for file in files.get(folder, []):
        print('    └──', file)
