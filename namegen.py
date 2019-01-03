#!/usr/bin/env python3

import sys
import random as rd
# import lexlib as lx
import itertools as iter


def generate(clusters, vowels, stop_len=9, min_len=1, vowel_mod=6):
    name = rd.choice(clusters["onset"]) if not check(vowel_mod) else ""
    name += rd.choice(vowels)
    while len(name) < stop_len:
        # name += rd.choice(clusters) if not check(vowel_mod) else ""
        name += rd.choice(clusters["inner"]) if not check(vowel_mod) else ""
        name += rd.choice(vowels)
        breakchance = stop_len - len(name)
        if breakchance <= int(stop_len/2):
            breakchance = int(stop_len/2)
        if len(name) >= min_len and check(breakchance):
            break
    name += rd.choice(clusters["offset"]) if not check(vowel_mod) else ""
    name = name.title()
    return name


def generate_many(clusters, vowels, how_many, max_len=9, min_len=1,
                  vowel_mod=3, print_name=True):
    counter = 0
    names = []
    while counter < how_many:
        name = generate(clusters, vowels, max_len, min_len, vowel_mod)
        if print_name:
            print(name)
        names.append(name)
        counter += 1
    return names


def check(num):
    return True if rd.randrange(num) == 0 else False


def get_clusters(names, vowels):
    clusters = {"onset": [], "offset": [], "inner": []}
    for name in names:
        broken = _split_iter(name, vowels)
        if name[0] not in vowels:
            # Add first one to onsets.
            clusters["onset"].append(broken.pop(0))
        if name[-1] not in vowels:
            # Add last one to offsets.
            clusters["offset"].append(broken.pop())
        # Add everything else to "inner."
        clusters["inner"] += broken
    return clusters


def _split_iter(word, sep_list):
    clusters = word
    for sep in sep_list:
        clusters = list(filter(lambda x: x, iter.chain(*map(lambda clus: clus.split(sep), clusters))))
        # print(clusters)
    return list(clusters)


def main(**kwargs):
    if len(sys.argv) >= 2:
        namefile = str(sys.argv[1])
    else:
        # namefile = "ext_names.txt"
        namefile = kwargs.get("names", "names.csv")
    with open(namefile, "r") as f:
        # namestring = f.read()
        names = [line.lower().strip() for line in f]
    # names = namestring.split("\n")
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    # clusters = lx.clusters(names, vowels)
    clusters = get_clusters(names, vowels)
    return clusters, vowels

if __name__ == "__main__":
    clusters, vowels = main()
