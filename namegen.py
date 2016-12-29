#!/usr/bin/env python3

import random as rd
import wordutils


def generate(clusters, vowels, stop_len=9, min_len=1, vowel_mod=6):
    name = ""
    while len(name) < stop_len:
        name += rd.choice(clusters) if not check(vowel_mod) else ""
        name += rd.choice(vowels)
        breakchance = stop_len - len(name)
        if breakchance <= int(stop_len/2):
            breakchance = int(stop_len/2)
        if len(name) >= min_len and check(breakchance):
            break
    name += rd.choice(clusters) if not check(vowel_mod) else ""
    name = name.title()
    return name


def generate_many(clusters, vowels, how_many, max_len=9, min_len=1,
                  vowel_mod=3):
    counter = 0
    names = []
    while counter < how_many:
        name = generate(clusters, vowels, max_len, min_len, vowel_mod)
        print(name)
        names.append(name)
        counter += 1
    return names


def check(num):
    return True if rd.randrange(num) == 0 else False


if __name__ == "__main__":
    # namefile = "ext_names.txt"
    namefile = "names.csv"
    with open(namefile, "r") as f:
        namestring = f.read()
    names = namestring.split("\n")
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    clusters = wordutils.clusters(names, vowels)
