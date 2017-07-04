"""
Script enables to search for specific strings within directory's files
"""

import os
import argparse

# python search_for.py  -n arg1 -e arg2
# default test strings
search_string = 'import'
ending = '.py'
results_num = 0

parser = argparse.ArgumentParser()
parser.add_argument('-n', action='store', dest='search_string')
parser.add_argument('-e', action='store', dest='ending')
arguments = parser.parse_args()

if arguments.search_string:
    search_string = str(arguments.search_string)
if arguments.ending:
    ending = str(arguments.ending)

dir_list = os.listdir()
for elem in dir_list:
    file_name = str(elem)
    if ending in file_name:
        curr_file = open(file_name, 'r', encoding="utf-8")
        file_data = curr_file.read()
        if search_string in file_data:
            print('{} found in:   '.format(search_string), file_name, '\n')
            results_num += 1
        curr_file.close()
if results_num is 1:
    print(results_num, 'result was found')
else:
    print(results_num, 'results were found')
