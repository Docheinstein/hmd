# HMD

Simple WYSIWYG markdown language for write and render man pages, from command line or from Python.

## WHY

The goal of the *HMD* language is to provide a simple language that permit to render
an .hmd man page directly from a Python application.

This allow you to write your own man page and render it in a cross platform manner 
(since does not depends on the external `man` command).

## INSTALLATION
```
pip install hmd
```

or 

```
git clone https://github.com/Docheinstein/hmd
```

## USAGE

Run with
```
hmd
```

or 

```
python -m hmd
```

```
usage: __main__.py [-h] [-t] [-n] [-c COLUMNS] [input]

Render documents written in hmd (Help MarkDown) with the default pager. Reads from 'input' or from stdin if it is not given.

positional arguments:
  input                 Help MarkDown file to process and render

optional arguments:
  -h, --help            show this help message and exit
  -t, --text            Output text, without ANSI style
  -n, --no-pager        Just print, without using the pager
  -c COLUMNS, --columns COLUMNS
                        Override columns number (by default it depends on the terminal size)
```

## EXAMPLES

### Usage from command line

Renders `ls.hmd` with the default pager
```
hmd ls.hmd
```

Prints `ls.hmd`, without the pager
```
hmd -n ls.hmd
```

Prints `ls.hmd`, without the pager and without style using 60 columns
```
hmd -n -t -c 60 ls.hmd
```

### Usage from Python
See `_main__.py` or `demos`.

For example

`demo1.py`
```python
from hmd import HMD

HMD_EXAMPLE = \
"""\
. This is a comment, keep calm
**NAME**
    ls - list local directory content
    
**SYNOPSIS**
    **ls** [*OPTION*]... [*DIR*]

**DESCRIPTION**
    List content of the local *DIR* or the current local directory if \
    no *DIR* is specified.

**OPTIONS**
    **-a**, **--all**
        Show hidden files too

    **-l**
        Show more details"""


if __name__ == "__main__":
    # Renders with less the processed .hmd
    HMD().render(HMD_EXAMPLE)
```

## HMD LANGUAGE

The HMD language is really simple and is thought for contain the minimal stuff for 
render a well formatted man page (ANSI formatting, automatic break respecting indent, align overriding, ...).

In the spirit of a WYSIWYG language, you will get almost what your write, and
differently from canonical markdown, a new line in the source will be translated
to a new line in the output (*no ugly double space at end of line!*)


See the `examples` folder for examples of `.hmd` files.

Here an example of a `.hmd` file from the `examples` folder

```
**COMMAND**
    ls - list local directory content

**SYNOPSIS**
    **ls** [*OPTION*]... [*DIR*]

**DESCRIPTION**
    List content of the local *DIR* or the current local directory if \
    no *DIR* is specified.

**OPTIONS**
    **-a**, **--all**
        Show hidden files too

    **-g**, **--group**
        Group by file type

    **-l**
        Show more details

    **-r**, **--reverse**
        Reverse sort order

    **-S**
        Show files size

    **-s**, **--sort-size**
        Sort by size
```

### Indent
The indentation of each paragraph is equal to the number of left spaces in the source file.  
If a line is longer the the number of available columns, the line will be broken and the
remaining part will be indented automatically by the same amount.

### Format

##### Bold
Same as markdown: \*\*NAME\*\* => **NAME**

##### Italic (underline)
Same as markdown: \*DIR\* => *DIR*

### Escaping
Backslash (`\`) can be use for escape the next character.  
You can use it for render characters that would be interpreted otherwise.  
For example:  
* \\* => *
* \\\\ => \\

### Directives
Each line starting with a `.` is a directive.

##### Comment
An unknown directive is an inline comment, so you can use:  `. My long comment...`

##### Alignment
The are cases in which you want the text to break to an alignment different from
the indentation of the paragraph (e.g. lists). The alignment directive graphically
helps you to do so.

To override the alignment for a part of the document, wrap it between `.A` and `./A`.  

For example: 
```
.A     .
    1. I want this text to wrap below the 'I', not below the 1, if the length
    of the line is greater than the number of lines
./A
```

As you see, the trailing `.` in the `.A` directive specify graphically where to wrap.

### Misc
##### Long lines
If you have long lines in your source file, you could add a trailing `\` at 
the end of the line for join it with the consecutive line (in the output).
Use the same indent of the first line even for consecutive lines.

For example:

```
**DESCRIPTION**
    This is my really really long hmd line that would exceed my strict rule of \
    maximum 80 columns, but fortunalety hmd supports the trailing backslash, \
    this make me really happy.
```