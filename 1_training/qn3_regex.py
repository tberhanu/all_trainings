#!/usr/bin/env python3.7

import re


def main():
    pattern = re.compile(r'(Time_sample([[]123[]])|time_sample( -:))')
    with open('myfile.txt', 'r') as f:
        contents = f.read()
        matches = pattern.finditer(contents)
        for match in matches:
            print(match.group())

if __name__ == "__main__":

    main()