""" QUESTION 4
Write a script that will recursively browse through a directory and list all the
files which has the word ‘HCL’ in it. Use regular expression and make this case insensitive
"""

import re
import glob

def list_files(spath):
    pattern = re.compile(r'hcl')
    files = glob.glob(spath + '/**/*', recursive=True)

    for file in files:
        match = pattern.search(file, re.I)
        if match:
            print(file)
        # print(file)

spath = r"/Users/tess/Desktop/"
list_files(spath)
