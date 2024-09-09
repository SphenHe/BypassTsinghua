#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import os
import json
from os.path import isfile, join
import filecmp
import time
import subprocess

PROGRAM = 'aplusb.py'
FULL_SCORE = 80
TIME_LIMIT = 1.0
DATA_PATH = 'data'

if len(sys.argv) > 1:
    PROGRAM = sys.argv[1]

if sys.version_info[0] != 3:
    print("Plz use python3")
    sys.exit()


def file_lines(file):
    lines = []
    with open(file, 'r', encoding='utf-8') as fd:
        for line in fd:
            line = line.strip()
            if len(line) > 0:
                lines.append(line)
    return lines


if __name__ == '__main__':

    grade = 0
    data = dict()
    files = [f for f in os.listdir(DATA_PATH) if isfile(
        join(DATA_PATH, f)) and f.startswith('in')]

    success_count = 0

    for file in sorted(files):
        file_in = join(DATA_PATH, file)
        num = int(file[2:-4])
        file_ans = join(DATA_PATH, f'ans{num}.txt')
        file_out = join(DATA_PATH, f'out{num}.txt')
        try:
            os.remove(file_out)
        except FileNotFoundError:
            pass

        message = []
        success = True

        p = subprocess.Popen([sys.executable, PROGRAM], stdin=open(
            file_in, 'r'), stdout=open(file_out, 'w'), stderr=subprocess.PIPE)
        start_time = time.time()

        while p.poll() is None:
            if time.time() - start_time > TIME_LIMIT:
                p.kill()
                message.append('Time limit exceeded')
                success = False
        else:
            if not os.path.isfile(file_out):
                message.append('No output file found')
                success = False

        if success:
            ans, out = file_lines(file_ans), file_lines(file_out)
            if len(ans) != len(out):
                    message.append(f'Line count mismatch: should be {len(ans)}, got {len(out)}')
                    success = False
            else:
                for i in range(len(ans)):
                    if out[i] != ans[i]:
                        message.append(f'Line {i} mismatch: should be \'{ans[i]}\', get \'{out[i]}\'')
                        success = False
                        break

        if success:
            success_count += 1
            if os.isatty(1):
                print(f'Testcase {num}: PASS')
        else:
            if os.isatty(1):
                stdout, stderr = p.communicate(timeout=1)
                if len(stderr) > 0:
                    message.append(f'Your program exited with: {stderr.decode("utf-8")}')
                print(f'Testcase {num}: {", ".join(message)}')


    # output grade
    grade = int(FULL_SCORE / len(files) * success_count)
    data['grade'] = grade
    if os.isatty(1):
        print(f'Grade: {grade}/{int(FULL_SCORE)}')
    else:
        print(json.dumps(data))

    if grade < FULL_SCORE:
        sys.exit(1)
