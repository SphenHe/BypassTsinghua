#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import sys
import os
import json
from os.path import isfile, join
import filecmp
import time
import subprocess

if sys.version_info[0] != 3:
    print("Plz use python3")
    sys.exit()

grade = 0.0
data = dict()
path = 'data'

files = [f for f in os.listdir(path) if isfile(join(path, f)) and f.startswith('in')]

def file_lines(file):
    lines = []
    with open(file, 'r') as fd:
        for line in fd:
            line = line.strip()
            if len(line) > 0:
                lines.append(line)
    return lines

for file in sorted(files):
    file_in = join(path, file)
    num = int(file[2:-4])
    file_ans = join(path, 'ans%d.txt' % num)
    file_out = join(path, 'out%d.txt' % num)
    try:
        os.remove(file_out)
    except FileNotFoundError:
        pass
    p = subprocess.Popen([sys.executable, 'collatz.py'], stdin=open(file_in, 'r'), stdout=open(file_out,'w'), stderr=subprocess.PIPE)
    start_time = time.time()

    while p.poll() is None:
        if time.time() - start_time > 1:
            p.kill()

    if file_lines(file_ans) == file_lines(file_out):
        grade += 100.0 / len(files)
    elif os.isatty(1):
        print('Data %d: expected %s, but got %s' % (num, repr(file_lines(file_ans)), repr(file_lines(file_out))))
        stdout, stderr = p.communicate(timeout=1)
        if len(stderr) > 0:
            print('       : your program exited with:')
            sys.stdout.buffer.write(stderr)


data['grade'] = grade
if os.isatty(1):
    print('得分：%d/100' % grade)
else:
    print(json.dumps(data))
