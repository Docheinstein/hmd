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

    **-l**
        Show more details"""


if __name__ == "__main__":
    HMDAnsii().process(HMD_EXAMPLE)