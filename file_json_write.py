import os
import json
my_file = os.path.join('data', 'myfile_out.json')

a = [13, 3.263, 5.363, 7, 9]

with open(my_file, 'w') as f:
    json.dump(a, f)