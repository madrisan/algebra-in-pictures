#!/usr/bin/python3

# Plot the reminder of an integer division x / y
# Copyright (C) 2019 Davide Madrisan <davide.madrisan@gmail.com>
# SPDX-License-Identifier: Apache-2.0

import numpy as np
import os
from utils import argparser, copyleft, plot

def parse_args():
    """This function parses and return arguments passed in"""
    descr = ("Plot some basic relations from -SIZE <= x,y <= SIZE.\n"
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
    r = range(1, args.size)
    rem = lambda x, y: x % y
    data = [[rem(x, y) for x in r] for y in r]
    plot(data, 1, args.size, args.outfile)

if __name__ == "__main__":
    main()
