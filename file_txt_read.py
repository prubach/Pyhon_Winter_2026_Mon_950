import os

my_file = 'data/myfile.txt'
cwd = os.getcwd()
print(cwd)

f = open(my_file, mode='r')
lines = f.readlines()
i = 0
while i < len(lines):
    print(lines[i], end='')
    i += 1

