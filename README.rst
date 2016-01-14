.. figure:: http://i.imgur.com/ddxYie4.jpg
   :alt: 

Vocabulary
==========

|PyPI version| |License| |Python Versions| |Build Status| |Requirements Status| |Gitter chat| 

A dictionary magician in the form of a module!

:Author: Tasdik Rahman

.. contents::
    :backlinks: none

.. sectnum::

What is it
----------

For a given word, using ``Vocabulary``, you can get it's

-  **Meaning**
-  **Synonyms**
-  **Antonyms**
-  **Part of speech** : whether the word is a ``noun``, ``interjection``
   or an ``adverb`` et el
-  **Translate** : Translate a phrase from a source language to the desired language.
-  **Usage example** : a quick example on how to use the word in a
   sentence
-  **Pronunciation**
-  **Hyphenation** : shows the particular stress points(if any)

Features
--------

-  Written in uncomplicated ``Python``
-  Returns ``JSON`` objects
-  Minimum dependencies ( just uses `requests <https://github.com/kennethreitz/requests>`__ module )
-  Easy to
   `install <https://github.com/prodicus/vocabulary#installation>`__
-  A decent substitute to ``Wordnet``\ (well almost!) Wanna see? Here is
   a `small comparison <#wordnet-comparison>`__
-  Stupidly `easy to
   use <https://github.com/prodicus/vocabulary#usage>`__
-  Fast!
-  Supports

   -  both, ``python2.*`` and ``python3.*``
   -  Works on Mac, Linux and Windows

Why should I use Vocabulary
---------------------------

``Wordnet`` is a great resource. No doubt about it! So why should you
use ``Vocabulary`` when we already have ``Wordnet`` out there?

Wordnet Comparison
~~~~~~~~~~~~~~~~~~

Let's say you want to find out the synonyms for the word ``car``.

-  Using ``Wordnet``

.. code:: python

    >>> from nltk.corpus import wordnet
    >>> syns = wordnet.synsets('car')
    >>> syns[0].lemmas[0].name
    'car'
    >>> [s.lemmas[0].name for s in syns]
    ['car', 'car', 'car', 'car', 'cable_car']

    >>> [l.name for s in syns for l in s.lemmas]
    ['car', 'auto', 'automobile', 'machine', 'motorcar', 'car', 'railcar', 'railway_car', 'railroad_car', 'car', 'gondola', 'car', 'elevator_car', 'cable_car', 'car']

-  Doing the same using ``Vocabulary``

.. code:: python

    >>> from vocabulary import Vocabulary as vb
    >>> vb.synonym("car")
    '[{
      "seq": 0,
      "text": "automobile"
    }, {
      "seq": 1,
      "text": "cart"
    }, {
      "seq": 2,
      "text": "automotive"
    }, {
      "seq": 3,
      "text": "wagon"
    }, {
      "seq": 4,
      "text": "motor"
    }]'
    >>> ## load the json data
    >>> car_synonyms = json.loads(vb.synonym("car"))
    >>> type(car_synonyms)
    <class 'list'>
    >>> 

So there you go. You get the data in an easy ``JSON`` format.

You can go on comparing for the other methods too.

Installation
------------

Option 1: installing through `pip <https://pypi.python.org/pypi/vocabulary>`__ (Suggested way)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`pypi package link <https://pypi.python.org/pypi/vocabulary>`__

``$ pip install vocabulary``

If you are behind a proxy

``$ pip --proxy [username:password@]domain_name:port install vocabulary``

**Note:** If you get ``command not found`` then
``$ sudo apt-get install python-pip`` should fix that

Option 2: Installing from source
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    $ git clone https://github.com/prodicus/vocabulary.git
    $ cd vocabulary/
    $ pip install -r requirements.txt
    $ python setup.py install


Demo
~~~~

.. figure:: https://raw.githubusercontent.com/prodicus/vocabulary/master/assets/usage.gif
   :alt: Demo link


Documentation
-------------

For a detailed usage example, refer the `documentation at Read the Docs <http://vocabulary.readthedocs.org/en/latest/>`__

Contributing
------------

Please refer `Contributing page for details <https://github.com/prodicus/vocabulary/blob/master/CONTRIBUTING.rst>`__


Discuss
~~~~~~~

Join us on our `Gitter channel <https://gitter.im/prodicus/vocabulary>`__
if you want to chat or if you have any questions in your mind.

Contributers
~~~~~~~~~~~~

-  Thanks to `Anton Relin <https://github.com/relisher>`__ for adding the `translate <https://github.com/prodicus/vocabulary/blob/master/vocabulary/vocabulary.py#L218>`__ module.
- And a big shout out to all the `contributers <https://github.com/prodicus/vocabulary/graphs/contributors>`__ for their contributions

Changelog
---------
Please refer `Changelog page for details <https://github.com/prodicus/vocabulary/blob/master/CHANGELOG.rst>`__

Bugs
----

Please report the bugs at the `issue
tracker <https://github.com/prodicus/vocabulary/issues>`__


Known Issues
~~~~~~~~~~~~

-  In **python2**, when using the method **Vocabulary.pronunciation()** 

.. code:: python

    >>> vb.pronunciation("hippopotamus")
    [{
      "seq": 0,
      "text": "automotive"
    }, {
      "seq": 1,
      "text": "motor"
    }, {
      "seq": 2,
      "text": "wagon"
    }, {
      "seq": 3,
      "text": "cart"
    }, {
      "seq": 4,
      "text": "automobile"
    }]
    >>> type(vb.pronunciation("hippopotamus"))
    <class 'list'>
    >>> json.dumps(vb.pronunciation("hippopotamus"))
    '[{"raw": "(h\\u012dp\\u02cc\\u0259-p\\u014ft\\u02c8\\u0259-m\\u0259s)", "rawType": "ahd-legacy", "seq": 0}, {"raw": "HH IH2 P AH0 P AA1 T AH0 M AH0 S", "rawType": "arpabet", "seq": 0}]'
    >>>

You are being returned a ``list`` object instead of a ``JSON`` object.
When returning the latter, there are some ``unicode`` issues. A fix for
this will be released soon.

I may suggest `python-ftfy <https://github.com/LuminosoInsight/python-ftfy>`__ which can help you in this matter.


License :
---------

`MIT License <http://prodicus.mit-license.org/>`__ © `Tasdik Rahman <http://tasdikrahman.me/>`__

You can find a copy of the License at http://prodicus.mit-license.org/

|Bitdeli Badge|

.. |PyPI version| image:: https://img.shields.io/pypi/v/Vocabulary.svg
   :target: https://img.shields.io/pypi/v/Vocabulary.svg
.. |License| image:: https://img.shields.io/pypi/l/vocabulary.svg
   :target: https://img.shields.io/pypi/l/vocabulary.svg
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/Vocabulary.svg
.. |Build Status| image:: https://travis-ci.org/prodicus/vocabulary.svg?branch=master
.. |Gitter chat| image:: https://img.shields.io/gitter/room/gitterHQ/gitter.svg
   :alt: Join the chat at https://gitter.im/prodicus/vocabulary
   :target: https://gitter.im/prodicus/vocabulary?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
.. |Bitdeli Badge| image:: https://d2weczhvl823v0.cloudfront.net/prodicus/vocabulary/trend.png
   :target: https://bitdeli.com/free%20Bitdeli%20Badge
.. |Requirements Status| image:: https://requires.io/github/prodicus/vocabulary/requirements.svg?branch=master
   :target: https://requires.io/github/prodicus/vocabulary/requirements/?branch=master
