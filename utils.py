#!/usr/bin/python3

# Common functions for Algebre in Pictures
# Copyright (C) 2018 Davide Madrisan <davide.madrisan@gmail.com>
# SPDX-License-Identifier: Apache-2.0

__author__ = "Davide Madrisan"
__copyright__ = "Copyright (C) 2019 Davide Madrisan"
__license__ = "Apache License 2.0 (Apache-2.0)"
__version__ = "1"
__email__ = "davide.madrisan@gmail.com"
__status__ = "stable"

import argparse
import matplotlib.pyplot as plt

def argparser(descr):
    """Return a new ArgumentParser object """
    return argparse.ArgumentParser(
               formatter_class = argparse.RawDescriptionHelpFormatter,
               description = copyleft(descr))

def copyleft(descr):
    """Print the Copyright message and License """

    return ("{0} -- v{1}\n{2} <{3}>\nLicense: {4}"
        .format(descr, __version__, __copyright__, __email__, __license__))

def plot(matrix, low, high, outfile, cmap=plt.cm.Spectral):
    """This function plot the reminders, and save them to '
       a png file if a filename is specified ('outfile')."""
    fig = plt.figure()

    ax = fig.add_subplot(1, 1, 1)
    ax.set_aspect("equal")
    for side in ["left", "top", "right", "bottom"]:
        ax.spines[side].set_visible(False)

    plt.imshow(matrix,
               interpolation="nearest",
               cmap=cmap,
               extent=(low, high,
                       low, high))
    plt.xticks([])
    plt.yticks([])

    if (outfile):
        plt.savefig(outfile, bbox_inches="tight", transparent=True)
    else:
        plt.show()
