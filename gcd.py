#!/usr/bin/python3

# Plot gcd(m,n) for -SIZE <= m,n <= SIZE.
# A different color is associated to each value with the color range
# pretty evident along the main diagonal.
#
#   -- See "Abstract Algebra with Applications" - Audrey Terras
#
# Copyright (C) 2019 Davide Madrisan <davide.madrisan.gmail.com>
# SPDX-License-Identifier: Apache-2.0

from math import gcd
import argparse
import matplotlib.pyplot as plt
import numpy as np
import textwrap

__author__ = "Davide Madrisan"
__copyright__ = "Copyright (C) 2019 Davide Madrisan"
__license__ = "Apache License 2.0 (Apache-2.0)"
__version__ = "1"
__email__ = "davide.madrisan@gmail.com"
__status__ = "stable"

def argparser(descr, examples):
    """Return a new ArgumentParser object """
    return argparse.ArgumentParser(
               formatter_class = argparse.RawDescriptionHelpFormatter,
               description = copyleft(descr),
               epilog = "Examples:\n" + textwrap.dedent(examples))

def copyleft(descr):
    """Print the Copyright message and License """

    return ("{0} v.{1} ({2})\n{3} <{4}>\nLicense: {5}"
        .format(
            descr, __version__, __status__,
            __copyright__, __email__,
            __license__))

def parse_args():
    """This function parses and return arguments passed in"""
    descr = ("Plot gcd(m,n) for -SIZE <= m,n <= SIZE. "
             "Optionally save the plot to a PNG file.")
    examples = """
        %(prog)s
        %(prog)s --size 40
        %(prog)s --size 50 --outfile images/gcd.png
    """

    parser = argparser(descr, examples)
    parser.add_argument(
        "-s", "--size",
        action="store", dest="size", type=int, default=50,
        help="range of the gcd values to be plotted (default: %(default)s)")
    parser.add_argument(
        "-f", "--outfile",
        action="store", dest="outfile",
        help="name of the output PNG file")

    return parser.parse_args()

def plot(matrix, size, outfile):
    """This function plot the data, and save them to a png file
       if a filename is specified ('outfile')."""
    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)
    ax.set_aspect("equal")
    for side in ["left", "top", "right", "bottom"]:
        ax.spines[side].set_visible(False)

    plt.imshow(matrix,
               interpolation="nearest",
               cmap=plt.cm.Spectral,
               extent=(-size, size,
                       -size, size))
    plt.xticks([])
    plt.yticks([])

    if (outfile):
        plt.savefig(outfile, bbox_inches="tight", transparent=True)
    else:
        plt.show()

def main():
    args = parse_args()
    r = range(-args.size, args.size + 1)
    data = [[gcd(m, n) for m in r] for n in r]
    plot(data, args.size, args.outfile)

if __name__ == "__main__":
    main()
