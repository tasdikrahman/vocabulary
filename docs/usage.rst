==============
Usage Examples
==============

A Simple demonstration of the module

.. code-block:: python

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

    ## "Response Formatting"
    >>> vb.antonym("love", format="dict")
    {"text": "hate"}
    >>> vb.antonym("love", format="list")
    ["hate"]
    >>> vb.part_of_speech("code", format="dict")
    {0: {"text": "noun", "example": "A systematically arranged and comprehensive collection of laws."}}
    >>> vb.part_of_speech("code", format="list")
    [["noun", "A systematically arranged and comprehensive collection of laws."]]

