#!/bin/bash

# while [ $? -eq 0 ]
# do
python3 gen.py --size 100 > rand.in
time python3 a.py rand.in a.out
time python3 b.py rand.in b.out
diff -Zb a.out b.out
# done
