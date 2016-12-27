#!/usr/bin/env python3

import random as rd
import wordutils

namefile = "names.csv"
with open(namefile, "r") as f:
    names = [name[:-1] for name in f.readlines()]
vowels = ['a', 'e', 'i', 'o', 'u', 'y']
clusters = wordutils.clusters(names, vowels)


def generate(clusters, vowels, max_len=12):
    if rd.randrange(10) == 9:
        name = rd.choice(vowels)
        name += rd.choice(clusters)
    else:
        name = rd.choice(clusters)
    while len(name) < 9:
        name += rd.choice(vowels)
        if len(name) >= 4 and rd.randrange(3) == 2:
            break
        else:
            name += rd.choice(clusters)
            if len(name) >= 4 and rd.randrange(3) == 2:
                break
    name = name.title()
    return name
