WizCoin
======

A Pythom module to represent the galleon, sickle and knut coins of wizard currency.

Installation
------------

To install with pip, run:

    pip install wizcoin

Quickstart Guide
----------------

Here is some example code demonstrating how this module is used:

    >>> import wizcoin
    >>> coin = wizcoin.WizCoin(2, 5, 10)
    >>> str(coin)
    >>> "2g, 5s, 10k"
    >>> coin.value()
    1141

Contribute
----------

If you'd like to contribute to WizCoin, check out https://github.com/ekogl/wizcoin
