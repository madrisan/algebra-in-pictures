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
from utils import argparser, plot

def parse_args():
    """This function parses and return arguments passed in"""
    descr = ("Plot gcd(m,n) for -SIZE <= m,n <= SIZE.\n"
             "Optionally save the plot to a PNG file")

    parser = argparser(descr)
    parser.add_argument(
        "-s", "--size",
        action="store", dest="size", type=int, default=50,
        help="range of the gcd values to be plotted (default: %(default)s)")
    parser.add_argument(
        "-f", "--outfile",
        action="store", dest="outfile",
        help="name of the output PNG file")

    return parser.parse_args()

def main():
    args = parse_args()
    r = range(-args.size, args.size + 1)
    data = [[gcd(m, n) for m in r] for n in r]
    plot(data, -args.size, args.size, args.outfile)

if __name__ == "__main__":
    main()
