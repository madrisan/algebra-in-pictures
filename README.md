# Algebra in pictures

![Release Status](https://img.shields.io/badge/status-in--progress-green.svg)
[![Maintainability](https://api.codeclimate.com/v1/badges/ef9834aff8e762b4ae01/maintainability)](https://codeclimate.com/github/madrisan/algebra-in-pictures/maintainability)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a09af71ad7a547f98d2d178daa410262)](https://www.codacy.com/app/madrisan/algebra-in-pictures?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=madrisan/algebra-in-pictures&amp;utm_campaign=Badge_Grade)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](https://spdx.org/licenses/Apache-2.0.html)

Some interesting pictures of algebric objects.

## gcd

Plot *gcd*(*m*,*n*) for -50 <= *m*, *n* <= 50.
A different color is associated to each value with the color range pretty evident along the main diagonal,
where *gcd*(*m*,*m*) = |m|.

See: "*Abstract Algebra with Applications*" by Audrey Terras (external link: [Cambridge U. Press][aawa])

![alt tag][gcd-plot]

Python code: [gcd.py][gcd-code]

Usage:

    ./gcd.py --help
    ./gcd.py --size 50
    ./gcd.py --size 50 --outfile gcd.png

[aawa]: https://www.cambridge.org/core/books/abstract-algebra-with-applications/725D4A0DDED4E62472C870D0C53F134C
[gcd-code]: https://github.com/madrisan/algebra-in-pictures/blob/master/gcd.py "python source gcd"
[gcd-plot]: https://github.com/madrisan/algebra-in-pictures/blob/master/images/gcd.png "gcd plot"
