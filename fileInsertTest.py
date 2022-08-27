#! /usr/bin/env python3
'''
#
# Program:
#    Name: Andrew                  File: fileInsertTest.py
#    Date: Wed Aug 24 2022
#   Notes:
#
#........1.........2.........3.........4.........5.........6.........7.........8.........9.........0.........1.........2.........3..
'''

import argparse
from tkinter import Tk
from pathlib import Path

# Setup the arg parser to import and parse arguments.
_parser = argparse.ArgumentParser()

# Parameter for file to insert flag value into
_parser.add_argument(
  "--file", "-f",
  default=None,
  required=True,
  help="Log file to put the flag into"
)

# Make sure ONLY flag type or search string are specified by grouping them together.
searchGroup = _parser.add_mutually_exclusive_group(required=True)

# Specify the type of flag root/user
searchGroup.add_argument(
  "--flagtype", "-t",
  default=None,
  type=str.lower,
  choices=['root', 'user']
)

# Specify custom search string to insert after
searchGroup.add_argument(
  "--search", "-s",
  default=None,
  help="Custom search string to insert flag after. Will use '## {User/Root} Flag' syntax \
         in the file (case insensitive) if not provided."
)

# Specify the flag value to be inserted
_parser.add_argument(
  "--flag", "-g",
  default=None,
  help="Flag to insert into file. Will use clipboard contents if not provided"
)

# Enable formatting the flag for viewing in markdown (indent the flag under the heading)
_parser.add_argument(
  "--markdown", "-m",
  default=None,
  action='store_true',
  help="Use if the flag should be indented to allow highlight when viewing in Markdown"
)

# Parse arguments and store them to use later.
_args = _parser.parse_args()

# Default search criteria based on flag type with allowance for a custom one.
_flag_type = {
  "root": '## Root flag',
  "user": '## User flag',
  "custom": str
}

# In-line lambda function for keeping a value between a min and max.
clamp = lambda n, minn, maxn: max(min(n, maxn), minn)


def main():
  '''
  Parse the input file and insert the flag values under the correct headings.
  '''
  global _flag_type

  # Populate our constants with the arguments from the command line.
  FILE = _args.file
  FLAGTYPE = _args.flagtype
  if _args.flag:
    FLAG = _args.flag
  else:
    FLAG = Tk().clipboard_get()

    # Check to see if we got something on the clipboard.
    # For testing: flag{flag_inserted_from_clipboard}
    #   To clear the clipboard: Tk().clipboard_clear()
    if not FLAG:
      print('\nERROR: No flag provided. Specify --flag on call or have it on the system clipboard\n')
      return

  if _args.search:
    FLAGTYPE = 'custom'
    _flag_type[FLAGTYPE] = _args.search

  if _args.markdown:
    MARKDOWN = True
  else:
    MARKDOWN = False

  # Try to open and load the contents of the file specified.
  try:
    with open(Path(FILE), 'r') as fp:
      contents = fp.readlines()

  except:
    print('\nERROR: File to insert into not found...\n')

  # Update the contents of the file.
  contents = writeFlag(_flag_type[FLAGTYPE], FLAG, contents, MARKDOWN)

  # Output the file with the changes made.
  with open(Path(FILE), 'w') as fp:
    fp.seek(0)
    fp.writelines(contents)

def writeFlag(srchVal: str, flag: str, contents: list[str], markdown: bool) -> list[str]:
  '''
  Search the file for the headings and insert the flags underneath them.
  '''
  # Change the flag string for display in markdown (4 spaces required)
  if markdown:
    flag = ' ' * 4 + flag

  # Handle if the search value is at the end of the file with/without blank lines after.
  if srchVal.lower() in contents[-1].lower():
    # If thebottom line has a new line character at the end of it we only need to insert the flag.
    if contents[-1].endswith('\n'):
      contents.append(flag)

    # Otherwise we need to go to a new line and then insert the flag.
    else:
      contents.append('\n' + flag)

  # Handle if the flag heading is in the middle of the file and the flag is not already there.
  for index, line in enumerate(contents):
    # Check if we have a match and the next line is not already the flag we're inserting.
    if srchVal.lower() in line.lower() and flag not in contents[index + 1]:
      scan_ahead_lines = 3

      # Figure out how many new lines we need for spacing by looking at empty lines ahead.
      for i in range(index, clamp(index + 3, index, len(contents))):
        if contents[i][0:] == '\n':
          scan_ahead_lines -= 1

      # Insert the flag and however many new lines we need for spacing.
      contents.insert(index + 1, flag + '\n')
      for i in range(1, scan_ahead_lines):
        contents.insert(index + 2, '\n')

  return contents     # Return the modified file.


def interact():
  ''' Using python -i fileInsertTest.py it will execute globals and drop into REPL '''
  import code
  code.InteractiveConsole(locals=globals()).interact()


# If the fileInsertTest.py is run (instead of imported as a module), call the main() function:
if __name__ == '__main__':
  main()
