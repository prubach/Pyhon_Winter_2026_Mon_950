import os

my_file = os.path.join('data', 'rates.csv')
print(os.path.getsize(my_file))

# Contributed by Dariusz Jadowski

#my_folder = 'c:\\windows\\system32\\drivers'
my_folder = 'data'
print(os.path.getsize(my_folder))

folder_files = os.listdir(my_folder)
print(folder_files)

def get_size(start_path = my_folder):
    total_size = 0
    for dirpath, dirnames, filenames in os.walk(start_path):
        for f in filenames:
            fp = os.path.join(dirpath, f)
            if not os.path.islink(fp):
                total_size += os.path.getsize(fp)


    return total_size

print ('The total size of the folder is:', get_size(), 'bytes')