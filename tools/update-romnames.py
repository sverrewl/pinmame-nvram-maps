#!/usr/bin/env python3

# User needs to pipe output from `pinmame -listfull` to this program.

import json
import os
import sys


if os.isatty(0):
    print("Usage: pinmame -listfull | update-romnames.py")
    exit(0)

romnames = {
    '_note': 'Automatically generated by tools/update-romnames.py',
}

linecount = 0
for line in sys.stdin:
    if linecount:
        # skip the first line, which is just a header
        line = line.strip('\n\r"')
        (rom, description) = line.split('"', 1)
        rom = rom.strip()
        romnames[rom] = description
    linecount += 1

rootdir = os.path.join(os.path.dirname(__file__), '..')
with open(os.path.join(rootdir, 'romnames.json'), 'w') as f:
    f.write(json.dumps(romnames, indent=2, sort_keys=True))
    f.write('\n')   # include trailing newline

print('Updated romnames.json with %u names.' % (linecount - 1))
