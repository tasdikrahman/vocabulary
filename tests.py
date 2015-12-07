#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
from vocabulary import Vocabulary as vb
# import Vocabulary as vb
try:
    import simplejson as json
except ImportError:
    import json


class TestModule(unittest.TestCase):
    """Checks for the sanity of all module methods"""

    def test_meaning(self):
        current_result = vb.meaning("humming")
        result = '[{"seq": 0, "text": "Present participle of hum."}]'
        middle_val = json.loads(result)
        expected_result = json.dumps(middle_val)
        self.assertEqual(current_result, expected_result)

    def test_synonym(self):
        current_result = vb.synonym("repudiate")
        result = '[{"seq": 0, "text": "deny"}]'
        middle_val = json.loads(result)
        expected_result = json.dumps(middle_val)
        self.assertEqual(current_result, expected_result)

    def test_antonym_1(self):
        current_result = vb.antonym("love")
        result = '{"text": ["hate"]}'
        expected_result = json.loads(result)
        self.assertEqual(current_result, expected_result)

    def test_antonym_2(self):
        current_result = vb.antonym("respect")
        result = '{"text": ["disesteem", "disrespect"]}'
        expected_result = json.loads(result)
        self.assertEqual(current_result, expected_result)

    def test_partOfSpeech_1(self):
        current_result = vb.part_of_speech("hello")
        result = '[{"text": "interjection", "example:": "Used to greet someone, answer the telephone, or express surprise.", "seq": 0}]'
        middle_val = json.loads(result)
        expected_result = json.dumps(middle_val)
        self.assertEqual(current_result, expected_result)

    def test_partOfSpeech_2(self):
        current_result = vb.part_of_speech("rapidly")
        result = '[{"text": "adverb", "example:": "With speed; in a rapid manner.", "seq": 0}]'
        middle_val = json.loads(result)
        expected_result = json.dumps(middle_val)
        self.assertEqual(current_result, expected_result)

    def test_usageExamples1(self):
        current_result = vb.usage_example("hillock") # for valid word
        result = '[{"seq": 0, "text": "I went to the to of the hillock to look around."}]'
        middle_val = json.loads(result)
        expected_result = json.dumps(middle_val)
        self.assertEqual(current_result, expected_result)

    def test_usageExamples2(self):
        current_result = vb.usage_example("lksj") # # for non valid word
        expected_result = False
        self.assertEqual(current_result, expected_result)

    def test_pronunciation1(self):
        current_result = vb.pronunciation("hippopotamus") # for valid word
        result = '[{"rawType": "ahd-legacy", "raw": "(hĭpˌə-pŏtˈə-məs)", "seq": 0}, {"rawType": "arpabet", "raw": "HH IH2 P AH0 P AA1 T AH0 M AH0 S", "seq": 0}]'
        expected_result = json.loads(result)
        self.assertEqual(current_result, expected_result)

    def test_pronunciation2(self):
        current_result = vb.pronunciation("lksj") # for non valid word
        expected_result = False
        self.assertEqual(current_result, expected_result)

    def test_hyphenation(self):
        current_result = vb.hyphenation("hippopotamus")
        result = '[{"seq": 0, "text": "hip", "type": "secondary stress"}, {"seq": 1, "text": "po"}, {"seq": 2, "text": "pot", "type": "stress"}, {"seq": 3, "text": "a"}, {"seq": 4, "text": "mus"}]'
        middle_val = json.loads(result)
        expected_result = json.dumps(middle_val)
        self.assertEqual(current_result, expected_result)

    def test_translate1(self):
        current_result = vb.translate("hummus", "en", "es")
        result = '[{"text": "hummus", "seq": 0}]'
        middle_val = json.loads(result)
        expected_result = json.dumps(middle_val)
        self.assertEqual(current_result, expected_result)

    def test_translate2(self):
        current_result = vb.translate("asldkfj", "en", "ru")
        self.assertEqual(current_result, False)

if __name__ == "__main__":
    unittest.main()
