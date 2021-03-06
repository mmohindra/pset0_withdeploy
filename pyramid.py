#!/usr/bin/env python3
"""Print a pyramid to the terminal

A pyramid of height 3 would look like:

--=--
-===-
=====

"""

from argparse import ArgumentParser, RawDescriptionHelpFormatter


def print_pyramid(rows):
    """Print a pyramid of a given height

    :param int rows: total height
    """

    maxsigncnt = rows*2-1
    for i in range(1,rows+1):
        ddashcnt = i*2-1
        dashcnt = int((maxsigncnt -ddashcnt)/2)
        print(('-'*dashcnt),('='*ddashcnt),('-'*dashcnt), sep='')
    #raise NotImplementedError("Called with rows={}".format(rows))


if __name__ == "__main__":
    parser = ArgumentParser(
        description=__doc__, formatter_class=RawDescriptionHelpFormatter
    )
    parser.add_argument("-r", "--rows", default=10, help="Number of rows")

    args = parser.parse_args()
    print_pyramid(args.rows)
