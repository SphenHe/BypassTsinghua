#!/usr/bin/env python3

import sys
import h5py

output = h5py.File(sys.argv[1])
std = h5py.File(sys.argv[2])

THRESHOLD = 0.01
def scoring(r, r_std):
  ratio = abs(r - r_std) / max(abs(r_std), 1e-5)

  if ratio < THRESHOLD:
    return 1
  return 0.1 ** ((ratio - THRESHOLD) / (1 - THRESHOLD))

def compare_dataset(ans, std):
    if ans.shape != std.shape:
        print("Wrong dataset shape, expecting:")
        print(std.shape)
        print("...but got:")
        print(ans.shape)
        return 0

    tot = 0;
    cnt = 0;

    for i in range(1, ans.shape[0]-1):
        for j in range(1, ans.shape[1]-1):
            for k in range(0, ans.shape[2]):
                score = scoring(ans[i,j,k], std[i,j,k])
                tot += score
                if score < 1:
                    print("Diff at (%d,%d)[%d], %f <-> %f" % (i, j, k, ans[i,j,k], std[i,j,k]))
                cnt += 1

    return tot / cnt

vs = compare_dataset(output.get('velocity'), std.get('velocity'))
print("Velocity average score: ", vs, " / 1.0")
ds = compare_dataset(output.get('dyes'), std.get('dyes'))
print("Dyes average score: ", ds, " / 1.0")

ts = (vs + ds) / 2
print("Final score: ", ts, " / 1.0")

with open(sys.argv[3], 'w') as verdict:
    verdict.write(str(ts))
