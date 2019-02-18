#!/usr/bin/python3

# Plot the reminder of an integer division x / y
# Copyright (C) 2019 Davide Madrisan <davide.madrisan@gmail.com>
# SPDX-License-Identifier: Apache-2.0

from utils import argparser, plot

def parse_args():
    """This function parses and return arguments passed in"""
    descr = ("Plot m mod n for 0 <= m,n <= SIZE.\n"
             "Optionally save the plot to a PNG file")

    parser = argparser(descr)
    parser.add_argument(
        "-s", "--size",
        action="store", dest="size", type=int, default=500,
        help="range of the mod values to be plotted (default: %(default)s)")
    parser.add_argument(
        "-f", "--outfile",
        action="store", dest="outfile",
        help="name of the output PNG file")

    return parser.parse_args()

def main():
    args = parse_args()
    r = range(1, args.size)
    rem = lambda m, n: m % n
    data = [[rem(m, n) for m in r] for n in r]
    plot(data, 1, args.size, args.outfile)

if __name__ == "__main__":
    main()
