Contributing
============

1. Fork it.

2. Clone it

create a `virtualenv <http://pypi.python.org/pypi/virtualenv>`__

.. code:: bash

    $ virtualenv develop              # Create virtual environment
    $ source develop/bin/activate     # Change default python to virtual one
    (develop)$ git clone https://github.com/tasdikrahman/vocabulary.git
    (develop)$ cd vocabulary
    (develop)$ pip install -r requirements.txt  # Install requirements for 'Vocabulary' in virtual environment

Or, if ``virtualenv`` is not installed on your system:

.. code:: bash

    $ wget https://raw.github.com/pypa/virtualenv/master/virtualenv.py
    $ python virtualenv.py develop    # Create virtual environment
    $ source develop/bin/activate     # Change default python to virtual one
    (develop)$ git clone https://github.com/tasdikrahman/vocabulary.git
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
-  [X] Add an option like `JSON=False` or `JSON=True` where the former returns a list object

Tests
~~~~~

``Vocabulary`` uses ``unittesting`` for testing purposes.

Running the test cases

.. code:: bash

    test_antonym_ant_key_error (tests.tests.TestModule) ... ok
    test_antonym_found (tests.tests.TestModule) ... ok
    test_antonym_not_found (tests.tests.TestModule) ... ok
    test_hyphenation_found (tests.tests.TestModule) ... ok
    test_hyphenation_not_found (tests.tests.TestModule) ... ok
    test_meaning_found (tests.tests.TestModule) ... ok
    test_meaning_key_error (tests.tests.TestModule) ... ok
    test_meaning_not_found (tests.tests.TestModule) ... ok
    test_partOfSpeech_found (tests.tests.TestModule) ... ok
    test_partOfSpeech_not_found (tests.tests.TestModule) ... ok
    test_pronunciation_found (tests.tests.TestModule) ... ok
    test_pronunciation_not_found (tests.tests.TestModule) ... ok
    test_respond_as_dict_1 (tests.tests.TestModule) ... ok
    test_respond_as_dict_2 (tests.tests.TestModule) ... ok
    test_respond_as_dict_3 (tests.tests.TestModule) ... ok
    test_respond_as_list_1 (tests.tests.TestModule) ... ok
    test_respond_as_list_2 (tests.tests.TestModule) ... ok
    test_respond_as_list_3 (tests.tests.TestModule) ... ok
    test_synonynm_empty_list (tests.tests.TestModule) ... ok
    test_synonynm_found (tests.tests.TestModule) ... ok
    test_synonynm_not_found (tests.tests.TestModule) ... ok
    test_synonynm_tuc_key_error (tests.tests.TestModule) ... ok
    test_translate_empty_list (tests.tests.TestModule) ... ok
    test_translate_found (tests.tests.TestModule) ... ok
    test_translate_not_found (tests.tests.TestModule) ... ok
    test_translate_tuc_key_error (tests.tests.TestModule) ... ok
    test_usageExample_empty_list (tests.tests.TestModule) ... ok
    test_usageExample_found (tests.tests.TestModule) ... ok
    test_usageExample_not_found (tests.tests.TestModule) ... ok

    ----------------------------------------------------------------------
    Ran 29 tests in 0.015s

    OK

