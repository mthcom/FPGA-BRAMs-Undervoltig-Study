import numpy as np
from sys import argv
import os

def convert(file_path):
    no_of_brams = 2060
    ram_size = 4096
    file = open(file_path)
    data = file.readline()
    file.close()
    ndarray = list()
    for i in range(no_of_brams):
        ndarray.append(data[i * ram_size:(i + 1) * ram_size])
    np.save(file_path[:-4], np.array(ndarray))

def traverse_folders(root_path):
    for root, dirs, files in os.walk(root_path):
        for file in files:
            current_path = os.path.join(root, file)
            if file[-4:] == '.bin':
                print('converting: ', current_path)
                convert(current_path)

if __name__ == '__main__':
    if len(argv) == 2:
        traverse_folders(argv[1])
    else:
        traverse_folders('.')