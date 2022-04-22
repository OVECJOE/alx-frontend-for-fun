#!/usr/bin/python3
'''
A script that codes markdown to HTML
'''
import sys
import os

if __name__ == '__main__':
    if len(sys.argv[1:]) != 2:
        print('Usage: ./markdown2html.py README.md README.html',
              file=sys.stderr)
        sys.exit(1)

    md_file = sys.argv[1]
    html_file = sys.argv[2]

    if not (os.path.exists(md_file) and os.path.isfile(md_file)):
        print(f'Missing {md_file}', file=sys.stderr)
        sys.exit(1)
