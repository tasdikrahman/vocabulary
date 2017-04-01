Contributing
============

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
-  [X]  Add an option like `JSON=False` or `JSON=True` where the former returns a list object

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

