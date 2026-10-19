import os
my_file = os.path.join('data', 'myfile_out.txt')

f = open(my_file, 'w')
f.write('hello world\n')
f.write('Hello from Python\n')
f.flush()
f.write('3rd line\n')
f.close()
print('Finished writing')

with open(my_file, 'a') as f:
    f.write('hello world\n')
    f.write('Hello from Python\n')
