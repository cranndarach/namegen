# Name Generator

>Generate pseudo-random names based on a corpus of real names.

Note: The names database used here comes from [Kaggle](https://www.kaggle.com/kaggle/us-baby-names).
You can use whatever you want.

## Requirements

* Python 3 (developed in 3.5)
* `lexlib` (`pip3 install lexlib` or `conda install -c cranndarach lexlib`)
* `random` (standard library)
* IPython (not required, but highly recommended)

## Obtain

### git clone

```sh
git clone https://github.com/cranndarach/namegen.git
cd namegen
```

### zip

[Download](https://github.com/cranndarach/namegen/archive/master.zip)

```sh
cd path/to/downloaded/namegen.zip
zip -d namegen.zip
rm namegen.zip
cd namegen
```

### tarball

[Download](https://github.com/cranndarach/namegen/tarball/master)

```sh
cd path/to/downloaded/namegen.tar.gz
tar -xzvf namegen.tar.gz
rm namegen.tar.gz
cd namegen
```

## Run

First, make an appropriate name list (you'll only have to do this once) by running:

```sh
python prep_names.py
```

You'll want to run the name generator interactively. This example shows how to
do it in IPython (start an IPython session by entering `ipython` in your terminal).

```ipython
%run namegen.py

# To generate one name at a time.
# You can also set the min_len, stop_len,
# and vowel_mod parameters. vowel_mod is
# the inverse probability of skipping the
# consonants for that syllable, resulting
# in multiple vowels in a row.
generate(clusters, vowels)

# To generate a list of names (in this example, 10).
# The same additional parameters can be set here.
generate_many(clusters, vowels, how_many=10)
```

## License and use

This *software* is licensed under the terms of the MIT license, copyright (c) 2016
R. Steiner, meaning roughly that you can use, modify, and distribute it as you 
like as long as you give credit (see [LICENSE.md](./LICENSE.md) for details).
You are welcome to use the *names* you generate freely without attribution, though
a link would be nice when it's reasonable. :)
