
from string import ascii_lowercase

def main() -> None:
    panagrams = (
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

    for panagram in panagrams:
        print(check_string(panagram))

def check_string(my_string):
    lwrCharacters = set([*ascii_lowercase])
    chkString = set([*my_string.lower()])
    diff = lwrCharacters.difference(chkString)
    if len(diff) == 0:
        value = f'The string "{my_string}" contains all the letters of the alphabet.'
    else:
        diff = sorted(diff)
        diff = ''.join(diff)
        value = f'The string "{my_string}" is missing the following letters: {diff}'
    return value

if __name__ == "__main__":
    main()