#!/usr/bin/env python3

import wordutils


namefile = "NationalNames.csv"
names = wordutils.get_words(namefile, "Name", ",")
with open("names.csv", "w") as f:
    f.write("\n".join(names))
