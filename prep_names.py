#!/usr/bin/env python3

import lexlib as lx


namefile = "NationalNames.csv"
names = lx.get_words(namefile, "Name", ",")
with open("names.csv", "w") as f:
    f.write("\n".join(names))
