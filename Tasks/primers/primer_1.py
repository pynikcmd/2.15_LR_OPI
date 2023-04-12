# !/usr/bin/env python3
# -*- cosing: utf-8 -*-


# open the primer.txt in append mode. Create a new file if no such file exists.
fileptr = open("primer.txt", "w")

# appending the content to the file
fileptr.write(
    "Python is the modern day language. It makes things so simple.\n"
    "It is the fastest-growing programing language"
)

# closing the opened the file
fileptr.close()
