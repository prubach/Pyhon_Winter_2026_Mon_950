import os
import pickle
my_file = os.path.join('data', 'myfile_out.pkl')

a = [13, 3.263, 5.363, 7, 9]

# wb - write binary!
with open(my_file, 'wb') as f:
    pickle.dump(a, f)