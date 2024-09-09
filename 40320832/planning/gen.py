#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import random


def gen(size):
    total = size + size // 2
    labels = list(range(total))
    random.shuffle(labels)
    items = dict({'物品{}'.format(labels[i]): ([], 1) for i in range(size // 2)})
    counter = size // 2
    while counter < total:
        name = '物品{}'.format(labels[counter])
        materials = random.sample(list(items.keys()), k=random.randint(2, 5))
        children = [(random.randint(1, 5), material) for material in materials]
        items[name] = (children, random.randint(1, 5))
        counter += 1
    xs = list(items.items())
    random.shuffle(xs)
    for name, (children, k) in xs:
        if len(children) > 0:
            if random.randint(0, 2) == 0:
                print('# 一些注释')
            print(' + '.join(['{} {}'.format(x, y)
                  for x, y in children]) + ' -> ' + '{} {}'.format(k, name))
    print('Q:')
    for i in range(random.randint(total, total + total // 2)):
        print('物品{} {}'.format(random.randint(
            0, total - 1), random.randint(1, 1000)))


def main():
    parser = argparse.ArgumentParser(
        'Generate test data for planning homework.')
    parser.add_argument('--size', type=int, required=True,
                        help='Size of the generated rules.')
    args = parser.parse_args()
    assert args.size >= 10
    gen(args.size)


if __name__ == '__main__':
    main()
