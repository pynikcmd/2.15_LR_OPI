# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


# open the primer.txt in write mode.
with open("primer.txt", "a") as fileptr:
    # overwriting the content of the file
    fileptr.write(" Python has an easy syntax and user-friendly interaction.")
