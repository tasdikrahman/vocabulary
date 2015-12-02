#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The MIT License (MIT)
Copyright © 2015 Tasdik Rahman

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and 
associated documentation files (the “Software”), to deal in the Software without restriction, including 
without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell 
copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the 
following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial 
portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT 
LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN 
NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, 
WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE 
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import json
import requests


__version__ = '0.0.4'
__author__ = "Tasdik Rahman"


class Vocabulary(object):
    """
    |      Function     | Public methods   |
    |:-----------------:|------------------|
    |  __get_api_link() | meaning()        |
    | __return_json()   | synonym()        |
    | __parse_content() | antonym()        |
    | __clean_dict()    | usage_example()  |
    |                   | hyphenation()    |
    |                   | part_of_speech() |
    |                   | pronunciation()  |
    """
    @staticmethod
    def __get_api_link(api):
        """returns
         - urbandictionary
         - wordnik
         - glosbe
         - bighugelabs
        API links

        params: api (possible values : "wordnik", "glosbe", "urbandict", "bighugelabs")

        """
        api_name2links = {
            "wordnik": "http://api.wordnik.com/v4/word.json/{word}/{action}?api_key=1e940957819058fe3ec7c59d43c09504b400110db7faa0509",
            "glosbe": "https://glosbe.com/gapi/translate?from={source_lang}&dest={dest_lang}&format=json&pretty=true&phrase={word}",
            "urbandict": "http://api.urbandictionary.com/v0/{action}?term={word}",
            "bighugelabs": "http://words.bighugelabs.com/api/2/eb4e57bb2c34032da68dfeb3a0578b68/{word}/json"
        }

        if api in api_name2links.keys():
            return api_name2links[api]
        else:
            return False

    @staticmethod
    def __return_json(url):
        """Takes the passed url and returns the json object by making a request
         to the specific API

        Called by 
         - meaning()
         - synonym()
        """
        response = requests.get(url)
        if response.status_code == 200:
            json_obj = response.json()
            return json_obj
        else:
            return False

    @staticmethod
    def __parse_content(tuc_content, content_to_be_parsed):
        """parses the passed "tuc_content" for
         - meanings
         - synonym
        received by querrying the glosbe API 

        Called by 
         - meaning()
         - synonym()
        """
        initial_parsed_content = {}
        
        i = 0
        for content_dict in tuc_content:
            if content_to_be_parsed in content_dict.keys():
                contents_raw = content_dict[content_to_be_parsed]
                if content_to_be_parsed == "phrase":
                    ## for 'phrase', 'contents_raw' is a dictionary
                    initial_parsed_content[i] = contents_raw['text']
                    i += 1
                elif content_to_be_parsed == "meanings":
                    ## for 'meanings', 'contents_raw' is a list
                    for meaning_content in contents_raw:
                        initial_parsed_content[i] = meaning_content['text']
                        i +=1

        final_parsed_content = {}
        ## removing duplicates(if any) from the dictionary
        for key, value in initial_parsed_content.items():
            if value not in final_parsed_content.values():
                final_parsed_content[key] = value

        ## calling __clean_dict

        formatted_list = Vocabulary.__clean_dict(final_parsed_content)
        return formatted_list

    @staticmethod
    def __clean_dict(dictionary):
        """Takes the dictionary from
            - meaning

        and creates a well formatted list

        params:
        ======
        dictionary
        """
        key_dict = {}
        value_dict = {}
        final_list = []
        for key in dictionary.keys():
            key_dict[key] = "seq"

        for value in dictionary.values():
            value_dict[value] = "text"

        for (key1, value1), (key2, value2) in zip(key_dict.items(), value_dict.items()):
            final_list.append({value1: int(key1), value2: key2})

        return final_list

    @staticmethod
    def meaning(phrase, source_lang="en", dest_lang="en"):
        """make calls to the
         - glosbe API(default choice)
         - Wordnik API 

         Wordnik's API gives less results so not Using it here for getting the meanings

         params: 
         =======
         source_lang, dest_lang (both default to "en" if nothing is specified)

         Usage: 
         ======
         >>> from vocabulary import Vocabulary as vb
         >>> vb.meaning("levitate")
         '[{"text": "(intransitive) Be suspended in the air, as if in defiance of gravity.", "seq": 0}, {"text": "(transitive) To cause to rise in the air and float, as if in defiance of gravity.", "seq": 1}]'
         >>> 
        """
        base_url = Vocabulary.__get_api_link("glosbe")
        url = base_url.format(word=phrase, source_lang=source_lang, dest_lang=dest_lang)
        json_obj = Vocabulary.__return_json(url)

        if json_obj:
            try:
                tuc_content = json_obj["tuc"]       ## "tuc_content" is a "list" 
            except KeyError:
                return False
            '''get meanings'''
            meanings_list = Vocabulary.__parse_content(tuc_content, "meanings")     
            # return meanings_list
            return json.dumps(meanings_list)
        else:
            return False

    @staticmethod
    def synonym(phrase, source_lang="en", dest_lang="en"):
        """Gets the synonym for the given word and returns them (if any found)
        Calls the glosbe API for getting the related synonym

        params:
        =======
        phrase, source_lang, dest_lang (both default to "en" if nothing is specified)

        Usage:
        ======
        >>> from vocabulary import Vocabulary as vb
        >>> vb.synonym("mundane")
        '[{"text": "routine", "seq": 0}, {"text": "workaday", "seq": 1}, {"text": "unremarkable", "seq": 2}, {"text": "everyday", "seq": 3}, {"text": "ordinary", "seq": 4}, {"text": "earthy", "seq": 5}, {"text": "quotidian", "seq": 6}]'
        >>>
        """
        base_url = Vocabulary.__get_api_link("glosbe")
        url = base_url.format(word=phrase, source_lang=source_lang, dest_lang=dest_lang)
        json_obj = Vocabulary.__return_json(url)
        if json_obj:
            try :
                tuc_content = json_obj["tuc"]       ## "tuc_content" is a "list" 
            except KeyError:
                return False
            synonyms_list = Vocabulary.__parse_content(tuc_content, "phrase")
            if synonyms_list:
                # return synonyms_list
                return json.dumps(synonyms_list)
            else:
                return False

        else:
            return False
    
        ## TO-DO:
        ## if this gives me no results, will query "bighugelabs"
    
    @staticmethod
    def antonym(phrase):
        """queries the bighugelabs API for the antonym. The results include
            - "syn" (synonym)
            - "ant" (antonym)
            - "rel" (related terms)
            - "sim" (similar terms)
            - "usr" (user suggestions)

        But currently parsing only the antonym as I have already done 
        - synonym (using glosbe API)

        params:
        ======
        phrase

        Usage:
        ======
        >>> vb.antonym("love")
        '{"text": ["hate"]}'
        >>> vb.antonym("insane")
        '{"text": ["sane"]}'
        >>> vb.antonym("respect")
        '{"text": ["disesteem", "disrespect"]}'
        >>>
        """
        base_url = Vocabulary.__get_api_link("bighugelabs")
        url = base_url.format(word=phrase)
        json_obj = Vocabulary.__return_json(url)
        
        """The thing here is that, I have no way to know what the keys returned would be,
        so I will use the 'dict.keys()' method to get all the keys first
        """
        if json_obj:
            antonyms = []
            dictionary = {}
            final_dictionary = {}
            keys = json_obj.keys()
            ## searching for the key "ant" inside the dictionary which is the value for the particular
            ## key being iterated (one of the "keys" key)
            for key in keys:
                try: 
                    key_value = json_obj[key]
                    value = key_value["ant"]
                    dictionary["text"] = value
                except KeyError:    ## if no antonyms are found!
                    return False

            ##removing duplicates if any
            for key, value in dictionary.items():
                if value not in final_dictionary.values():
                    final_dictionary[key] = value
                    antonyms.append(final_dictionary)

            # return json.dumps(final_dictionary)
            return final_dictionary
        else:
            return False

    @staticmethod
    def part_of_speech(phrase):
        """querrying Wordnik's API for knowing whether the word is a noun, adjective and the like

        params:
        ======
        phrase

        Usage:
        =====
        >>> Vocabulary.part_of_speech("hello")
        '[{"text": "interjection", "example:": "Used to greet someone, answer the telephone, or express surprise.", "seq": 0}]'
        >>> Vocabulary.part_of_speech("rapidly")
        '[{"text": "adverb", "example:": "With speed; in a rapid manner.", "seq": 0}]'
        >>>
        """
        ## We get a list object as a return value from the Wordnik API
        base_url = Vocabulary.__get_api_link("wordnik")
        url = base_url.format(word=phrase, action="definitions")
        json_obj = Vocabulary.__return_json(url)

        final_list = []
        if json_obj:
            part_of_speech = {}
            for content in json_obj:
                key = content["partOfSpeech"] 
                value = content["text"]
                part_of_speech[key] = value
                if part_of_speech:
                    ## cleaning "part_of_speech" using "__clean_dict()"
                    i = 0 
                    for key, value in part_of_speech.items():
                        final_list.append({ "seq": i, "text": key, "example:" :value})
                        i += 1
                    return json.dumps(final_list)
                    # return final_list
                else:
                    return False
        else: 
            return False

    @staticmethod
    def usage_example(phrase):
        """Takes the source phrase and queries it to the urbandictionary API

        params:
        =======
        phrase

        Usage:
        ======
        >>> Vocabulary.usage_example("heroic")
        '[{"text": "Person 1: Dude, I heard the SEAL Team got whiped out in that last mission.Person 2: Almost, there was a single survivor though. He managed to get away.Person 1: That man must be Heroic.", "seq": 0}, {"text": "Friend: Why\'d you have to go and pull heroics? Now you look like a goon", "seq": 1}, {"text": "Person 1: Dude, I heard the SEAL Team got whiped out in that last mission.Person 2: Almost, there was a single survivor though.  He managed to get away.Person 1: That man must be Heroic.", "seq": 2}]'
        >>>
        """
        base_url = Vocabulary.__get_api_link("urbandict")
        url = base_url.format(action="define", word=phrase)
        word_examples = {}
        json_obj = Vocabulary.__return_json(url)
        if json_obj:
            examples_list = json_obj["list"]
            for i, example in enumerate(examples_list):
                if example["thumbs_up"] > example["thumbs_down"]:
                    word_examples[i] = example["example"].replace("\r", "").replace("\n", "")
            if word_examples:
                ## reforamatting "word_examples" using "__clean_dict()"
                return json.dumps(Vocabulary.__clean_dict(word_examples))
                # return Vocabulary.__clean_dict(word_examples)
            else:
                return False
        else:
            return False

    @staticmethod
    def pronunciation(phrase):
        """Gets the pronunciation from the Wordnik API

        params:
        =======
        phrase

        Usage:
        ======
        >>> Vocabulary.pronunciation("hippopotamus")
        '[{"rawType": "ahd-legacy", "raw": "(hĭpˌə-pŏtˈə-məs)", "seq": 0}, {"rawType": "arpabet", "raw": "HH IH2 P AH0 P AA1 T AH0 M AH0 S", "seq": 0}]'
        >>>
        """
        base_url = Vocabulary.__get_api_link("wordnik")
        url = base_url.format(word=phrase, action="pronunciations")
        json_obj = Vocabulary.__return_json(url)
        if json_obj:
            '''
            Refer : http://stackoverflow.com/questions/18337407/saving-utf-8-texts-in-json-dumps-as-utf8-not-as-u-escape-sequence
            '''
            # return json.dumps(json_obj, ensure_ascii=False)
            return json_obj
        else:
            return False

    @staticmethod
    def hyphenation(phrase):
        """Returns back the stress points in the "phrase" passed

        params:
        ======
        phrase

        Usage:
        ======
        >>> Vocabulary.hyphenation("hippopotamus")
        '[{"seq": 0, "text": "hip", "type": "secondary stress"}, {"seq": 1, "text": "po"}, {"seq": 2, "text": "pot", "type": "stress"}, {"seq": 3, "text": "a"}, {"seq": 4, "text": "mus"}]'
        >>> 
        """
        base_url = Vocabulary.__get_api_link("wordnik")
        url = base_url.format(word=phrase, action="hyphenation")
        hyphenation = {}
        json_obj = Vocabulary.__return_json(url)
        if json_obj:
            return json.dumps(json_obj)
            # return json_obj
        else:
            return False