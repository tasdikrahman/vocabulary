.. figure:: http://i.imgur.com/ddxYie4.jpg
   :alt: 

Vocabulary
==========

|PyPI version| |License| |Build Status|

A dictionary magician in the form of a module!

Table of Contents
-----------------

-  `What is it? <#what-is-it>`__
-  `Features <#features>`__
-  `Installation <#installation>`__

   -  `pip <#option-1-installing-through-pip-suggested-way>`__
   -  `from source <#option-2-installing-from-source>`__

-  `Demo <#demo>`__
-  `Usage <#usage>`__
-  `How does it Work <#how-does-it-work>`__
-  `To Do <#to-do>`__
-  `Tests <#tests>`__
-  `Contributing <#contributing>`__
-  `Bugs <#bugs>`__
-  `License <#license>`__

What is it
----------

Using ``Vocabulary``, you can get

-  **Meaning**

   -  **Synonyms**
   -  **Antonyms**

-  **Part of speech** : whether the word is a ``noun``, ``interjection``
   or an ``adverb`` et el
-  **Usage example** : a quick example on how to use the word in a
   sentence
-  **Pronuciation**
-  **Hyphenation** : Breaks down the word and shows the particular
   stress points(if any) during pronunciation

for a given word!

Features
--------

-  Written in uncomplicated ``Python``
-  Returns ``JSON`` objects
-  Minimum dependencies ( just uses ``requests``
   (https://github.com/kennethreitz/requests))
-  Easy to
   `install <https://github.com/prodicus/vocabulary#installation>`__
-  Stupidly `easy to
   use <https://github.com/prodicus/vocabulary#usage>`__
-  Fast!
-  Supports both, ``python2.*`` and ``python3.*``
-  Works on Mac, Linux and Windows

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

Uninstalling
~~~~~~~~~~~~

``$ pip uninstall vocabulary``

Demo
----

.. figure:: 
   :alt: Imgur link

   Imgur link

Usage
-----

A Simple demonstration of the module

.. code:: bash

    ## Importing the module
    >>> from vocabulary import Vocabulary as vb

    ## Extracting "Meaning"
    >>> vb.meaning("hillbilly")
    [{'text': 'Someone who is from the hills; especially from a rural area, with a connotation of a lack of refinement or sophistication.', 'seq': 0}, {'text': 'someone who is from the hills', 'seq': 1}, {'text': 'A white person from the rural southern part of the United States.', 'seq': 2}]
    >>>

    ## "Synonym"
    >>> vb.synonym("hurricane")
    '[{"text": "storm", "seq": 0}, {"text": "tropical cyclone", "seq": 1}, {"text": "typhoon", "seq": 2}, {"text": "gale", "seq": 3}]'
    >>> 

    ## "Antonym"
    >>> vb.antonym("respect")
    '{"text": ["disesteem", "disrespect"]}'
    >>> vb.antonym("insane")
    '{"text": ["sane"]}'

    ## "Part of Speech"
    >>> vb.part_of_speech("hello")
    [{'text': 'interjection', 'example:': 'Used to greet someone, answer the telephone, or express surprise.', 'seq': 0}]
    >>> 

    ## "Usage Examples"
    >>> vb.usage_example("chicanery")
    '[{"text": "The Bush Administration is now the commander-in-theif (lower-case intentional) thanks to their chicanery.", "seq": 0}]'
    >>>

    ## "Pronunciation"
    >>> vb.pronunciation("hippopotamus")
    [{'raw': '(hĭpˌə-pŏtˈə-məs)', 'rawType': 'ahd-legacy', 'seq': 0}, {'raw': 'HH IH2 P AH0 P AA1 T AH0 M AH0 S', 'rawType': 'arpabet', 'seq': 0}]
    >>>

    ## "Hyphenation"
    >>> vb.hyphenation("hippopotamus")
    [{'text': 'hip', 'type': 'secondary stress', 'seq': 0}, {'text': 'po', 'seq': 1}, {'text': 'pot', 'type': 'stress', 'seq': 2}, {'text': 'a', 'seq': 3}, {'text': 'mus', 'seq': 4}]
    >>> >>> vb.hyphenation("amazing")
    [{'text': 'a', 'seq': 0}, {'text': 'maz', 'type': 'stress', 'seq': 1}, {'text': 'ing', 'seq': 2}]
    >>> 

How does it work
----------------

Under the hood, it makes use of 4 awesome API's to give you consistent
results. The API's being - Urbandict - Glosbe - BighugeLabs - Wordnik

To do
-----

-  Add translate module

Tests
-----

``Vocabulary`` uses ``unittesting`` for testing.

Run the test cases by doing a

.. code:: bash

    $ ./tests.py -v
    test_antonym_1 (__main__.TestModule) ... ok
    test_antonym_2 (__main__.TestModule) ... ok
    test_hyphenation (__main__.TestModule) ... ok
    test_meaning (__main__.TestModule) ... ok
    test_partOfSpeech_1 (__main__.TestModule) ... ok
    test_partOfSpeech_2 (__main__.TestModule) ... ok
    test_pronunciation (__main__.TestModule) ... ok
    test_synonym (__main__.TestModule) ... ok
    test_usageExamples (__main__.TestModule) ... ok

    ----------------------------------------------------------------------
    Ran 9 tests in 7.742s

    OK
    (testvocab)

Contributing
------------

Feel free to contribute

1. Fork it.
2. Create your feature branch
   (``git checkout -b my-new-awesome-feature``)
3. Commit your changes (``git commit -am 'Added <xyz> feature'``)
4. Push to the branch (``git push origin my-new-awesome-feature``)
5. Create new Pull Request

Bugs
----

Please report the bugs at the `issue
tracker <https://github.com/prodicus/vocabulary/issues>`__

License :
---------

`MIT License <http://prodicus.mit-license.org/>`__ © Tasdik Rahman You
can find a copy of the License at http://prodicus.mit-license.org/

.. |PyPI version| image:: https://badge.fury.io/py/vocabulary.svg
   :target: https://badge.fury.io/py/vocabulary
.. |License| image:: https://img.shields.io/pypi/l/vocabulary.svg
   :target: https://img.shields.io/pypi/l/vocabulary.svg
.. |Build Status| image:: https://travis-ci.org/prodicus/vocabulary.svg?branch=master
