import os
import pickle
my_file = os.path.join('data', 'myfile_out.pkl')

with open(my_file, 'rb') as file:
    my_arr = pickle.load(file)

print(my_arr)
print(type(my_arr))
for key in my_arr:
    print(key)
    print(type(key))