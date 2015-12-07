.. figure:: http://i.imgur.com/ddxYie4.jpg
   :alt: 

Vocabulary
==========

|PyPI version| |License| |Python Versions| |Build Status| |Gitter chat| |Bitdeli Badge|

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
-  Minimum dependencies ( just uses ``requests``
   (https://github.com/kennethreitz/requests))
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

My 2 cents

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
    '[{"seq": 0, "text": "automotive"}, {"seq": 1, "text": "motor"}, {"seq": 2, "text": "wagon"}, {"seq": 3, "text": "cart"}, {"seq": 4, "text": "automobile"}]'
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

Upgrade
~~~~~~~

You can update to the latest version by doing a 

``$ pip install --upgrade vocabulary``

Uninstalling
------------

``$ pip uninstall vocabulary``

Usage
-----

A Simple demonstration of the module

.. code:: python

    ## Importing the module
    >>> from vocabulary import Vocabulary as vb

    ## Extracting "Meaning"
    >>> vb.meaning("hillbilly")
    '[{"text": "Someone who is from the hills; especially from a rural area, with a connotation of a lack of refinement or sophistication.", "seq": 0}, {"text": "someone who is from the hills", "seq": 1}, {"text": "A white person from the rural southern part of the United States.", "seq": 2}]'
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
    '[{"text": "interjection", "example:": "Used to greet someone, answer the telephone, or express surprise.", "seq": 0}]'
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
    '[{"text": "hip", "type": "secondary stress", "seq": 0}, {"text": "po", "seq": 1}, {"text": "pot", "type": "stress", "seq": 2}, {"text": "a", "seq": 3}, {"text": "mus", "seq": 4}]'
    >>> vb.hyphenation("amazing")
    '[{"text": "a", "seq": 0}, {"text": "maz", "type": "stress", "seq": 1}, {"text": "ing", "seq": 2}]'
    >>>

    ## "Translate"
    >>> vb.translate("bread", "en","fra")
    '[{"seq": 0, "text": "pain"}, {"seq": 1, "text": "paner"}, {"seq": 2, "text": "pognon"}, {"seq": 3, "text": "fric"}, {"seq": 4, "text": "bl\\u00e9"}]'
    >>> vb.translate("goodbye", "en","es")
    '[{"seq": 0, "text": "hasta luego"}, {"seq": 1, "text": "vaya con Dios"}, {"seq": 2, "text": "despedida"}, {"seq": 3, "text": "adi\\u00f3s"}, {"seq": 4, "text": "vaya con dios"}, {"seq": 5, "text": "hasta la vista"}, {"seq": 6, "text": "nos vemos"}, {"seq": 7, "text": "adios"}, {"seq": 8, "text": "hasta pronto"}]'
    >>>

Demo
~~~~

.. figure:: https://raw.githubusercontent.com/prodicus/prodicus.github.io/master/images/vocabulary.gif
   :alt: Demo link

Help
~~~~

If you need to see the usage for any of the methods, do a

.. code:: python

    >>> from vocabulary import Vocabulary as vb
    >>> help(vb.translate)
    Help on function translate in module vocabulary.vocabulary:

    translate(phrase, source_lang, dest_lang)
        Gets the translations for a given word, and returns possibilites as a list
        Calls the glosbe API for getting the translation
        
        <source_lang> and <dest_lang> languages should be specifed in 3-letter ISO 639-3 format,
        although many 2-letter codes (en, de, fr) will work.
        
        See http://en.wikipedia.org/wiki/List_of_ISO_639-3_codes for full list.
        
        :param phrase:  word for which translation is being found
        :param source_lang: Translation from language
        :param dest_lang: Translation to language
        :returns: returns a json object
    (END)


and so on for other functions

How does it work
----------------

Under the hood, it makes use of 4 awesome API's to give you consistent
results. The API's being

-  Wordnik
-  Glosbe
-  BighugeLabs
-  Urbandict

Contributing
------------

1. Fork it.

2. Clone it 

create a `virtualenv <http://pypi.python.org/pypi/virtualenv>`__ 

.. code:: bash

    $ virtualenv develop              # Create virtual environment
    $ source develop/bin/activate     # Change default python to virtual one
    (develop)$ git clone https://github.com/prodicus/vocabulary.git
    (develop)$ cd vocabulary
    (develop)$ pip install -r requirements.txt  # Install requirements for 'Vocabulary' in virtual environment

Or, if ``virtualenv`` is not installed on your system:

.. code:: bash

    $ wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
    $ python virtualenv.py develop    # Create virtual environment
    $ source develop/bin/activate     # Change default python to virtual one
    (develop)$ git clone https://github.com/prodicus/vocabulary.git
    (develop)$ cd vocabulary
    (develop)$ pip install -r requirements.txt  # Install requirements for 'Vocabulary' in virtual environment

3. Create your feature branch (``$ git checkout -b my-new-awesome-feature``)

4. Commit your changes (``$ git commit -am 'Added <xyz> feature'``)

5. Run tests

.. code:: bash

    (develop) $ ./tests.py -v

Conform to `PEP8 <https://www.python.org/dev/peps/pep-0008/>`__ and if everything is running fine, integrate your feature 

6. Push to the branch (``$ git push origin my-new-awesome-feature``)

7. Create new Pull Request

Hack away! 

To do
~~~~~

-  [X] Add translate module
-  []  Add an option like `JSON=False` or `JSON=True` where the former returns a list object

Tests
~~~~~

``Vocabulary`` uses ``unittesting`` for testing purposes.

Running the test cases

.. code:: bash

    $ ./tests.py -v
    test_antonym_1 (__main__.TestModule) ... ok
    test_antonym_2 (__main__.TestModule) ... ok
    test_hyphenation (__main__.TestModule) ... ok
    test_meaning (__main__.TestModule) ... ok
    test_partOfSpeech_1 (__main__.TestModule) ... ok
    test_partOfSpeech_2 (__main__.TestModule) ... ok
    test_pronunciation1 (__main__.TestModule) ... ok
    test_pronunciation2 (__main__.TestModule) ... ok
    test_synonym (__main__.TestModule) ... ok
    test_translate (__main__.TestModule) ... ok
    test_translate2 (__main__.TestModule) ... ok
    test_usageExamples1 (__main__.TestModule) ... ok
    test_usageExamples2 (__main__.TestModule) ... ok

    ----------------------------------------------------------------------
    Ran 13 tests in 12.898s

    OK



Known Issues
~~~~~~~~~~~~

-  When using the method

.. code:: python

    >>> vb.pronunciation("hippopotamus")
    [{'raw': '(hĭpˌə-pŏtˈə-məs)', 'rawType': 'ahd-legacy', 'seq': 0}, {'raw': 'HH IH2 P AH0 P AA1 T AH0 M AH0 S', 'rawType': 'arpabet', 'seq': 0}]
    >>> type(vb.pronunciation("hippopotamus"))
    <class 'list'>
    >>> json.dumps(vb.pronunciation("hippopotamus"))
    '[{"raw": "(h\\u012dp\\u02cc\\u0259-p\\u014ft\\u02c8\\u0259-m\\u0259s)", "rawType": "ahd-legacy", "seq": 0}, {"raw": "HH IH2 P AH0 P AA1 T AH0 M AH0 S", "rawType": "arpabet", "seq": 0}]'
    >>>

You are being returned a ``list`` object instead of a ``JSON`` object.
When returning the latter, there are some ``unicode`` issues. A fix for
this will be released soon.

Discuss
~~~~~~~

Join us on our `Gitter channel <https://gitter.im/prodicus/vocabulary>`__
if you want to chat or if you have any questions.

Contributers
~~~~~~~~~~~~

-  Thanks to `Anton Relin <https://github.com/relisher>`__ for adding the `translate()` module 
-  A big shout out to all the `contributers <https://github.com/prodicus/vocabulary/graphs/contributors>`__

Changelog
---------

0.0.4
~~~~~

-  ``JSON`` inconsistency fixed for the methods

   -  ``Vocabulary.hyphenation()``
   -  ``Vocabulary.part_of_speech()``
   -  ``Vocabulary.meaning()``

0.0.5
~~~~~

- Added `translate` module
- Improved Documentation
- Minor bug fixes

Bugs
----

Please report the bugs at the `issue
tracker <https://github.com/prodicus/vocabulary/issues>`__

License :
---------

`MIT License <http://prodicus.mit-license.org/>`__ © `Tasdik Rahman <http://prodicus.github.com/>`__

You can find a copy of the License at http://prodicus.mit-license.org/

.. |PyPI version| image:: https://img.shields.io/pypi/v/Vocabulary.svg
   :target: https://img.shields.io/pypi/v/Vocabulary.svg
.. |License| image:: https://img.shields.io/pypi/l/vocabulary.svg
   :target: https://img.shields.io/pypi/l/vocabulary.svg
.. |Python Versions| image:: https://img.shields.io/pypi/pyversions/Vocabulary.svg
.. |Build Status| image:: https://travis-ci.org/prodicus/vocabulary.svg?branch=master
.. |Gitter chat| image:: https://badges.gitter.im/Join%20Chat.svg
   :alt: Join the chat at https://gitter.im/prodicus/vocabulary
   :target: https://gitter.im/prodicus/vocabulary?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge
.. |Bitdeli Badge| image:: https://d2weczhvl823v0.cloudfront.net/prodicus/vocabulary/trend.png
   :target: https://bitdeli.com/free%20Bitdeli%20Badge
