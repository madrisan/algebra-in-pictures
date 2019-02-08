#!/usr/bin/python3

# Plot gcd(m,n) for -50 <= m,n <= 50.
# A different color is associated to each value with the color range
# pretty evident along the main diagonal.
#
#   -- See "Abstract Algebra with Applications" - Audrey Terras
#
# Copyright (C) 2019 Davide Madrisan <davide.madrisan.gmail.com>

from math import gcd
import matplotlib.pyplot as plt
import numpy as np

def main():
    radius = 50
    r = range(-radius, radius)
    data = [[gcd(m, n) for m in r] for n in r]
    matrix = np.matrix(data)

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_aspect('equal')
    for side in ['left', 'top', 'right', 'bottom']:
        ax.spines[side].set_visible(False)

    plt.imshow(matrix,
               interpolation='nearest',
               cmap=plt.cm.Spectral,
               extent=(-radius, radius,
                       -radius, radius))
    plt.xticks([])
    plt.yticks([])

    plt.savefig('gcd.png', bbox_inches='tight', transparent=True)

if __name__ == '__main__':
    main()
