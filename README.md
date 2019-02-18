# Algebra in pictures

![Release Status](https://img.shields.io/badge/status-in--progress-green.svg)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/a09af71ad7a547f98d2d178daa410262)](https://www.codacy.com/app/madrisan/algebra-in-pictures?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=madrisan/algebra-in-pictures&amp;utm_campaign=Badge_Grade)
[![License](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](https://spdx.org/licenses/Apache-2.0.html)

Some interesting pictures of algebric objects.

## gcd

Plot *gcd*(*m*,*n*) for -SIZE <= *m*, *n* <= SIZE. (SIZE=50 by default).
A different color is associated to each value with the color range pretty evident along the main diagonal,
where *gcd*(*m*,*m*) = |m|.

See: "*Abstract Algebra with Applications*" by Audrey Terras (external link: [Cambridge U. Press][aawa])

![alt tag][gcd-plot]

Python code: [gcd.py][gcd-code]

Usage:

    ./gcd.py --help
    ./gcd.py
    ./gcd.py --size 50 --outfile gcd.png

## Reminder

Let's say we have integers *m* and *n*.
The *remainder* of *m* divided by *n* is the number *r* such that *m* = *qn* + *r*
for some integer *q* and *0* ≤ *r* < *n*.

Plot the *reminder* of *m* divided by *n* for 0 <= *m*, *n* <= SIZE. (SIZE=500 by default).

![alt tag][rem-plot]

Python code: [reminder.py][rem-code]

Usage:

    ./reminder.py --help
    ./reminder.py --size 1000
    ./reminder.py --size 1000 --outfile reminder.png

[aawa]: https://www.cambridge.org/core/books/abstract-algebra-with-applications/725D4A0DDED4E62472C870D0C53F134C
[gcd-code]: https://github.com/madrisan/algebra-in-pictures/blob/master/gcd.py "python source gcd"
[gcd-plot]: https://github.com/madrisan/algebra-in-pictures/blob/master/images/gcd.png "gcd plot"
[rem-code]: https://github.com/madrisan/algebra-in-pictures/blob/master/reminder.py "python source reminder"
[rem-plot]: https://github.com/madrisan/algebra-in-pictures/blob/master/images/reminder.png "reminder plot"
