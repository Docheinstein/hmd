from hmd import HMDAnsii

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

    **-g**, **--group**
        Group by file type

    **-l**
        Show more details

    **-r**, **--reverse**
        Reverse sort order

    **-S**
        Show files size

    **-s**, **--sort-size**
        Sort by size"""


if __name__ == "__main__":
    HMDAnsii().process(HMD_EXAMPLE)