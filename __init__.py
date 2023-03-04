import os

BASE_DIR = os.getcwd()

# take all files names from blacklist_files directory
files = os.listdir(os.path.join(BASE_DIR,'blacklist_files'))

