====
Help
====


If you need to see the usage for any of the methods, do a

.. code-block:: python

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
