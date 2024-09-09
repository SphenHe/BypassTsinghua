#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import json
from os.path import isfile, join, dirname
import filecmp
import time
import subprocess
import shutil

PROGRAM = 'main.py'
FULL_SCORE = 80
TIME_LIMIT = 1.0
DATA_PATH = 'data'

if len(sys.argv) > 1:
    print("Custom program unsupported (because the entry is main.py)")
    sys.exit()

if sys.version_info[0] != 3:
    print("Plz use python3")
    sys.exit()


if __name__ == '__main__':

    grade = 0
    data = dict()
    files = [f for f in os.listdir(DATA_PATH) if isfile(
        join(DATA_PATH, f)) and f.endswith('py')]

    success_count = 0

    for file in sorted(files):
        datagen = join(DATA_PATH, file)
        num = int(file[:-3])
        shutil.copy(datagen, join(dirname(__file__), 'data.py'))

        message = []
        success = True

        p = subprocess.Popen([sys.executable, PROGRAM],
                             stdin=None, stdout=None, stderr=subprocess.PIPE)
        start_time = time.time()

        while p.poll() is None:
            if time.time() - start_time > TIME_LIMIT:
                p.kill()
                message.append('Time limit exceeded')
                success = False
        else:
            stdout, stderr = p.communicate(timeout=1)
            code = p.returncode
            if code == 0:
                success_count += 1
                if os.isatty(1):
                    print(f'Testcase {num}: PASS')
            else:
                if os.isatty(1):
                    print(f'Testcase {num}:\n{stderr.decode("utf-8")}')

    # output grade
    grade = int(FULL_SCORE / len(files) * success_count)
    data['grade'] = grade
    if os.isatty(1):
        print(f'Grade: {grade}/{int(FULL_SCORE)}')
    else:
        print(json.dumps(data))

    shutil.copy(join(dirname(__file__), 'data', '1.py'),
                join(dirname(__file__), 'data.py'))

    if grade < FULL_SCORE:
        sys.exit(1)
