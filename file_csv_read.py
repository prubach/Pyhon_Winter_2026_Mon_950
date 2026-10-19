import os

my_file = os.path.join('data', 'rates.csv')

with open(my_file, 'r') as f:
    lines = f.readlines()
    print(lines)