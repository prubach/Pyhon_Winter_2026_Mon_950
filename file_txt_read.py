import os

#my_file = 'data/myfile.txt'
#my_file = 'c:\\Users\\prubac\\PycharmProjects\\Python_Winter_2026_Mon_950\\data\\myfile.txt'
#my_file = 'c:/Users/prubac/PycharmProjects/Python_Winter_2026_Mon_950/data/myfile.txt'
my_file = os.path.join('data', 'myfile.txt')
cwd = os.getcwd()
print(cwd)
my_folder = os.path.dirname(my_file)
print(f'file data folder: {my_folder}')

my_project_folder = os.path.dirname(os.path.dirname(my_file))
print(f'file project folder: {my_project_folder}')

my_folder_abs = os.path.abspath(my_folder)
print(f'file absolute path: {my_folder_abs}')

path_var = os.getenv("PATH")
print(f'PATH={path_var}')

f = open(my_file, mode='r')
lines = f.readlines()
i = 0
while i < len(lines):
    print(lines[i], end='')
    i += 1
f.close()

print('\n-------------')

with open(my_file, mode='r') as f:
    lines = f.readlines()
    for line in lines:
        print(line, end='')


