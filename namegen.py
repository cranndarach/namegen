#!/usr/bin/env python3

import random as rd
import wordutils


def generate(clusters, vowels, stop_len=9, min_len=1, vowel_mod=6):
    name = ""
    # name += rd.choice(vowels) if check(10) else none
    # if rd.randrange(10) == 9:
    #     name = rd.choice(vowels)
    #     name += rd.choice(clusters)
    # else:
    #     name = rd.choice(clusters)
    while len(name) < stop_len:
        # if breakchance < min_len:
        #     breakchance = min_len
        # breakchance = stop_len - len(name) if len(name) < stop_len/2 else\
        #     stop_len/2
        name += rd.choice(clusters) if not check(vowel_mod) else ""
        name += rd.choice(vowels)
        breakchance = stop_len - len(name)
        if breakchance <= int(stop_len/2):
            breakchance = int(stop_len/2)
        if len(name) >= min_len and check(breakchance):
            break
        # if len(name) >= 4 and rd.randrange(3) == 2:
        #     break
        # else:
        #     name += rd.choice(clusters)
        #    if len(name) >= 4 and rd.randrange(3) == 2:
        #        break
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
    return True if rd.randrange(num) == num-1 else False


# def breakcheck(num):
#     if check(num):
#         break
#     else:
#         None

if __name__ == "__main__":
    namefile = "ext_names.txt"
    with open(namefile, "r") as f:
        # names = [name[:-1] for name in f.readlines()]
        # The above is pretty; below saves about 0.2 seconds
        namestring = f.read()
    names = namestring.split("\n")
    vowels = ['a', 'e', 'i', 'o', 'u', 'y']
    clusters = wordutils.clusters(names, vowels)
