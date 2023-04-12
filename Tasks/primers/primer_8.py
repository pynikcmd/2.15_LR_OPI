#!/usr/bin/env python3
# -*- coding: utf-8 -*-


# open the file primer.txt in read mode
with open("primer.txt", "r") as fileptr:
    # initially the filepointer is at 0
    print("The filepointer is at byte :", fileptr.tell())

    # changing the file pointer location to 10.
    fileptr.seek(10);

    # tell() returns the location of the fileptr.
    print("After reading, the filepointer is at:", fileptr.tell())
