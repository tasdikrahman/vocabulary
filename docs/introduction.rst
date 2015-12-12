

============
Introduction
============

For a given word, using ``Vocabulary``, you can get it's

-  Meaning
-  Synonyms
-  Antonyms
-  Part of speech : whether the word is a ``noun``, ``interjection`` or an ``adverb`` et el
-  Translate : Translate a phrase from a source language to the desired language.
-  Usage example : a quick example on how to use the word in a sentence
-  Pronunciation
-  Hyphenation : shows the particular stress points(if any)


Features
========

-  Written in uncomplicated ``Python``
-  Returns ``JSON`` objects
-  Minimum dependencies ( just uses `requests <https://github.com/kennethreitz/requests>`__ )
-  Easy to `install <https://github.com/prodicus/vocabulary#installation>`__
-  A decent substitute to ``Wordnet``\ (well almost!) Wanna see? Here is a `small comparison <#wordnet-comparison>`__
-  Stupidly `easy to use <https://github.com/prodicus/vocabulary#usage>`__
-  Fast!
-  Supports

   -  both, ``python2.*`` and ``python3.*``
   -  Works on Mac, Linux and Windows

How does it work
================

Under the hood, it makes use of 4 awesome API's to give you consistent
results. The API's being

-  Wordnik
-  Glosbe
-  BighugeLabs
-  Urbandict
