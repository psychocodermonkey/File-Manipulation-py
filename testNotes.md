Test Markdown file for notes with CTF Flag headers
===================================================
# Programmer Name
## Box Name

# Description
The script will read through the file and search for the root and user flag headers to insert the flags passed to the script. The majority of the document here is purely to have a file with the types of things that would be in a markdown note file used for CTF. There are ways that the script can be "tricked" or fooled into doing weird things if you try, but works for the most part.

    Layout / Text notes in use for the indention.
    Good for examples and just flat out commands
    python -m pip install --upgrade pip

## Code example
Then we can even have sections for code to be recognized. Using ``` followed by the language. These "quotes" are not the normal quote, but the "tick" mark on the same key as "~".

```python

from pathlib import Path

with open(Path('file.txt'), 'r') as fp:
    for line in fp:
        print(line)

```

## User flag

This flag heading is where it is to show where a middle of the file insert would look like if it was only single spaced fro the header.


## Testing parsing
These are some other texts and parsing tests

```bash

echo "Hello World"

```

```c++

import <stdio>

void main() {
    printf("Hello World");
}

```

## Root flag
This root flag is spaced right next to other text and should end up spaced below the flag with two spaces since the script tries to look at lines beyond the header identified.

## In line highlighting with markdown
It does appear that whatever you put after the 3 tick marks will be used to direct it how to interpert the line. Also appears that the 3 tick marks has to be at the beginning of the line to be read properly.

Putting the ticks on the line will cause the text even in a paragraph to be changed to look like it is code. `Like this. This is now being shown in the same font as code!`

## In the end
In the end all looks good and appears fairly easy to have some basic text and headers and layout for the items that are presented in the document.

    May the MarkDown be with you!

## End of file flag headings
The challenge flag headeg is done by passing a custom search string to the script. As well as handling inserting any of the flags as the last line in the file. Tested by manually moving the lines below hee to the end of the file.

## Challenge flag
## User flag
## Root flag