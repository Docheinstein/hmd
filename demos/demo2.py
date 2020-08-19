from hmd import HMD, text_filter

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
    # Print the processed .hmd (without style)
    print(HMD(hmd_filter=text_filter).convert(HMD_EXAMPLE))