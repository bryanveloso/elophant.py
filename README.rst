elophant.py |travis|
====================

A minimalistic wrapper around the `Elophant <http://elophant.com/developers>`_
League of Legends statistics API.

Usage
-----

To start, you'll need to sign up for an `API key
<http://elophant.com/developers/new>`_. Once you have that, here's how you
use it. ::

    >>> from elophant import Elophant
    >>> e = Elophant(key='IyDxAwvLhQbzEZPiVYJo', region='na')
    >>> e.get_summoner('Elsydeon')
    {u'data': {u'internalName': u'elsydeon', u'name': u'Elsydeon' ...
    >>> e.find_team('clg')
    {u'data': {u'status': u'RANKED', u'modifyDate': u'/Date(1358737198000)/', u'name': u'Counter Logic Gaming' ...

Installation
------------

It's easy and foolproof! Like tower diving! ::

    pip install elophant

.. |travis| image:: https://travis-ci.org/bryanveloso/elophant.py.png?branch=master
