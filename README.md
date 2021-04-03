# EPUBTOCBZ.PY


This is a python3.9 script aiming at converting comics in epub format to CBZ format.

## Why this script

I have recently had a bad customer experience with comics in CBZ format, into which the JPEG files where too compressed for reading (blurry text, artefacts, ...), whereas the EPUB files also provided where readable but not practical. Knowing that EPUB files themselves also contain JPEG files of the comics pages, I made this script in order to be able to read my purchased comics comfortably. If anything, I hope i will not have to use it again by have correct CBZ files directly at purchase.
## requirements

1. [Python 3.9+](https://www.python.org/)
2. [Click](https://click.palletsprojects.com/en/5.x/)

## usage

`python3 epubtocbz.py ORIGIN DESTINATION`

where: 

+ origin is a directory containing the .epub files to convert
+ destination is a path for the generated files to be put in. If destination does not exist, it will be created.