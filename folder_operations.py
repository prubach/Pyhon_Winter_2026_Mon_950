import os

my_file = os.path.join('data', 'rates.csv')
print(os.path.getsize(my_file))

my_folder = 'data'

folder_files = os.listdir(my_folder)
print(folder_files)
