"""
Script enables to search for specific strings within directory's files
"""

import os
import sys
import argparse

# python search_for.py  -n arg1 -e arg2
# default test strings
search_lib = 'import'
ending = '.py'

parser = argparse.ArgumentParser()
parser.add_argument('-n', action='store', dest='search_lib')
parser.add_argument('-e', action='store', dest='ending')
arguments = parser.parse_args()

if arguments.search_lib:
    search_lib = str(arguments.search_lib)
if arguments.ending:
    ending = str(arguments.ending)

dir_list = os.listdir()
for elem in dir_list:
    file_name = str(elem)
    if ending in file_name:
        curr_file = open(file_name, 'r', encoding="utf-8")
        file_data = curr_file.read()
        if search_lib in file_data:
            print('{} found in:   '.format(search_lib), file_name, '\n')
        curr_file.close()
