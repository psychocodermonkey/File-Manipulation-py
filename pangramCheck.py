#! /usr/bin/env python3
'''
# Program: Script checking if strings are a panagram.
#    Name: Andrew Dixon            File: pangramCheck.py
#    Date: 15 Dec 2023
#   Notes:
#
#........1.........2.........3.........4.........5.........6.........7.........8.........9.........0.........1.........2.........3..
'''

from string import ascii_lowercase


def main() -> None:

  pangrams = (
    'Sphinx of black quartz, judge my vow.',
    'The five boxing wizards jump quickly.',
    'Jackdaws love my big sphinx of quartz.',
    'Mr. Jock, TV quiz PhD., bags few lynx.',
    'Pack my box with five dozen liquor jugs.',
    'Waxy and quivering jocks fumble the pizza.',
    'The quick brown fox jumps over the lazy dog.',
    'The quick brown fox jumped over the lazy dog.',
    'A wizard\'s job is to vex chumps quickly in fog.',
    """This Pangram contains four a's, one b, two c's, one d, thirty e's, six f's,
        five g's, seven h's, eleven i's, one j, one k, two l's, two m's, eighteen n's,
        fifteen o's, two p's, one q, five r's, twenty-seven s's, eighteen t's, two u's,
        seven v's, eight w's, two x's, three y's, & one z."""
  )

  for pangram in pangrams:
    print(check_string(pangram))

def check_string(chkString) -> str:
  # Convert both pieces to a set to make checking contents between strings easier.
  lwrCharacters = set([*ascii_lowercase])
  chkString = set([*chkString.lower()])

  # CHeck that all lower case characters exist in the string we're checking.
  # This ignores punctuation and numbers in the string as they don't count.
  diff = lwrCharacters.difference(chkString)

  if len(diff) == 0: # Then all the alphabet exists in the string passed.
    value = f'The string "{chkString}" contains all the letters of the alphabet.'

  else:  # There was a difference, print what characters are missing from the string.
    diff = sorted(diff)
    diff = ''.join(diff)
    value = f'The string "{chkString}" is missing the following letters: {diff}'
  return value

# If the pangramCheck.py is run (instead of imported as a module),
# call the main() function:
if __name__ == '__main__':
  main()
