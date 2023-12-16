Python file manipulation
========================

## Purpose of this repo
This repo will have python examples for file manipulation. It will most likely be a mess of random scripts and examples I wish to keep track of.

## File: fileInsertTest.py
This file is an example of modifying a file based on searched strings on line it finds. It is a "modify in place".

### Topics in this file
#### argparse
    Arguments passed with grouping.
    Arguments with default values.
    Arguments with validated choices for arguments.

#### file reading / updating
    example for reading a file into a list object for processing.
    text line searches for identification.
    inserting / appending lines

#### system clipboard
    using Tkinter to pull information from the system clipboard

#### clamping function (lambda function)
    Utilizing a lambda function for a inline clamping function. This is to control min and max
    for ranges to keep the values in range for the end of the file.

### Files related to this file
These are the files directly related to or required by fileInsertTest.py

    testNotes.md

## File: pangramCheck.py
Script containing some fun pangrams as well as code to check if strings are pangrams.

### Topics in this file
#### List comprehension
    List comprehension used to split out the characters into the sets.

#### set
    Set is being used to eliminate nested loops to look through the string to check
    that all characters in the string exist in the alphabet.
