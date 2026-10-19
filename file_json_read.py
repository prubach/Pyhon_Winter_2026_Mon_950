import os
import json
my_file = os.path.join('data', 'myfile_out.json')

with open(my_file, 'r') as file:
    my_arr = json.load(file)

print(my_arr)
print(type(my_arr))
for key in my_arr:
    print(key)
    print(type(key))