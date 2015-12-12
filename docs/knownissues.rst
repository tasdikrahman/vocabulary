============
Known Issues
============

When using the method ``pronunciation``

::

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
