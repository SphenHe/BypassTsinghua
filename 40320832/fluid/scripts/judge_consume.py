#!/usr/bin/env python3

import sys, time, os, subprocess, time, shutil, json

paths = sys.argv[1:]

tot = 0
for path in paths:
    with open(path) as verdict:
        score = float(verdict.readline())
        tot += score
        if os.isatty(1):
            print("[Similarity({})]: {}/1.0".format(path, score))

grade = tot / len(paths) * 100

if os.isatty(1):
    print('[Black box] {}/100 pts'.format(grade))
else:
    print(json.dumps({'grade': grade}))

