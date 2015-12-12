==================
Wordnet Comparison
==================

``Wordnet`` is a great resource. No doubt about it! So why should you
use ``Vocabulary`` when we already have ``Wordnet`` out there?

Let's say you want to find out the synonyms for the word ``car``.

-  Using ``Wordnet``

:: 

    >>> from nltk.corpus import wordnet
    >>> syns = wordnet.synsets('car')
    >>> syns[0].lemmas[0].name
    'car'
    >>> [s.lemmas[0].name for s in syns]
    ['car', 'car', 'car', 'car', 'cable_car']

    >>> [l.name for s in syns for l in s.lemmas]
    ['car', 'auto', 'automobile', 'machine', 'motorcar', 'car', 'railcar', 'railway_car', 'railroad_car', 'car', 'gondola', 'car', 'elevator_car', 'cable_car', 'car']

-  Doing the same using ``Vocabulary``

:: 

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