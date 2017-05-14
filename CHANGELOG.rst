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

1.0.0
~~~~~

- Added support for specifying response format
- Updated ``Vocabulary.pronunciation``, ``Vocabulary.antonym```, ```Vocabulary.part_of_speech``` to return a list of objects with apprioprate index

1.0.3
~~~~~

- Fixed `setup.py` import issue
- API changes to importing the module
```from vocabulary.vocabulary import Vocabulary as vb``` instead of ```from vocabulary import Vocabulary as vb```

