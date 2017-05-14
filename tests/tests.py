#!/usr/bin/env python
# -*- coding: utf-8 -*-

from vocabulary.vocabulary import Vocabulary as vb
from vocabulary.responselib import Response as rp
import unittest
import sys

try:
    import simplejson as json
except ImportError:
    import json
try:
    from unittest import mock
except Exception as e:
    import mock


class TestModule(unittest.TestCase):
    """Checks for the sanity of all module methods"""

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_meaning_found(self, mock_api_call):
        res = {
            "tuc": [
                {
                    "meanings": [
                        {
                            "language": "en",
                            "text": "the act of singing with closed lips"
                        }
                    ]
                }
            ]
        }

        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 200
        mock_api_call.return_value.json.return_value = res

        expected_result = '[{"seq": 0, "text": "the act of singing with closed lips"}]'
        expected_result = json.dumps(json.loads(expected_result))
        result = vb.meaning("humming")

        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(expected_result, result)
        else:
            self.assertCountEqual(expected_result, result)

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_meaning_not_found(self, mock_api_call):
        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 404

        self.assertFalse(vb.meaning("humming"))

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_meaning_key_error(self, mock_api_call):
        res = {
            "result": "ok",
            "phrase": "humming"
        }

        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 200
        mock_api_call.return_value.json.return_value = res

        expected_result = '[{"seq": 0, "text": "the act of singing with closed lips"}]'
        expected_result = json.dumps(json.loads(expected_result))

        self.assertFalse(vb.meaning("humming"))

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_synonynm_found(self, mock_api_call):
        res = {
            "tuc": [
                {
                    "phrase": {
                        "text": "get angry",
                        "language": "en"
                    }
                },
                {
                    "phrase": {
                        "text": "mad",
                        "language": "en"
                    },
                }
            ]
        }

        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 200
        mock_api_call.return_value.json.return_value = res

        expected_result = '[{"text": "get angry", "seq": 0}, {"text": "mad", "seq": 1}]'
        expected_result = json.dumps(json.loads(expected_result))
        result = vb.synonym("angry")

        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(expected_result, result)
        else:
            self.assertCountEqual(expected_result, result)

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_synonynm_not_found(self, mock_api_call):
        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 404

        self.assertFalse(vb.synonym("angry"))

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_synonynm_tuc_key_error(self, mock_api_call):
        res = {
            "result": "ok",
            "phrase": "angry"
        }

        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 200
        mock_api_call.return_value.json.return_value = res

        self.assertFalse(vb.synonym("angry"))

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_synonynm_empty_list(self, mock_api_call):
        res = {
            "result": "ok",
            "tuc": [],
            "phrase": "angry"
        }

        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 200
        mock_api_call.return_value.json.return_value = res

        self.assertFalse(vb.synonym("angry"))

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_translate_found(self, mock_api_call):
        res = {
            "tuc": [
                {
                    "phrase": {
                        "text": "anglais",
                        "language": "fr"
                    }
                },
                {
                    "phrase": {
                        "text": "germanique",
                        "language": "fr"
                    },
                }
            ]
        }

        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 200
        mock_api_call.return_value.json.return_value = res

        expected_result = '[{"text": "anglais", "seq": 0}, {"text": "germanique", "seq": 1}]'
        expected_result = json.dumps(json.loads(expected_result))
        result = vb.translate("english", "en", "fr")

        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(expected_result, result)
        else:
            self.assertCountEqual(expected_result, result)

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_translate_not_found(self, mock_api_call):
        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 404

        self.assertFalse(vb.translate("english", "en", "fr"))

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_translate_tuc_key_error(self, mock_api_call):
        res = {
            "result": "ok",
            "phrase": "english"
        }

        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 200
        mock_api_call.return_value.json.return_value = res

        self.assertFalse(vb.translate("english", "en", "fr"))

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_translate_empty_list(self, mock_api_call):
        res = {
            "result": "ok",
            "tuc": [],
            "phrase": "english"
        }

        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 200
        mock_api_call.return_value.json.return_value = res

        self.assertFalse(vb.translate("english", "en", "fr"))

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_antonym_found(self, mock_api_call):
        res = {
            "noun": {
                "ant": ["hate", "dislike"]
            },
            "verb": {
                "ant": ["hate", "hater"]
            }
        }

        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 200
        mock_api_call.return_value.json.return_value = res

        expected_result = '[{"text": "hate", "seq": 0}, {"text": "dislike", "seq": 1}, {"text": "hater", "seq": 2}]'
        result = vb.antonym("love")

        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(expected_result, result)
        else:
            self.assertCountEqual(expected_result, result)

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_antonym_not_found(self, mock_api_call):
        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 404

        self.assertFalse(vb.antonym("love"))

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_antonym_ant_key_error(self, mock_api_call):
        res = {
            "noun": {},
            "verb": {}
        }

        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 200
        mock_api_call.return_value.json.return_value = res

        self.assertFalse(vb.antonym("love"))

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_partOfSpeech_found(self, mock_api_call):
        res = [
            {
                "word": "hello",
                "partOfSpeech": "interjection",
                "text": "greeting"
            },
            {
                "word": "hello",
                "partOfSpeech": "verb-intransitive",
                "text": "To call."
            }
        ]

        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 200
        mock_api_call.return_value.json.return_value = res

        expected_result = '[{"text": "interjection", "example": "greeting", "seq": 0}, {"text": "verb-intransitive", "example": "To call.", "seq": 1}]'
        result = vb.part_of_speech("hello")

        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(expected_result, result)
        else:
            self.assertCountEqual(expected_result, result)

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_partOfSpeech_not_found(self, mock_api_call):
        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 404

        self.assertFalse(vb.part_of_speech("hello"))

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_usageExample_found(self, mock_api_call):
        res = {
            "list": [
                {
                    "definition": "a small mound or hill",
                    "thumbs_up": 18,
                    "word": "hillock",
                    "example": "I went to the to of the hillock to look around.",
                    "thumbs_down": 3
                }
            ]
        }

        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 200
        mock_api_call.return_value.json.return_value = res

        expected_result = '[{"seq": 0, "text": "I went to the to of the hillock to look around."}]'
        result = vb.usage_example("hillock")

        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(expected_result, result)
        else:
            self.assertCountEqual(expected_result, result)

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_usageExample_not_found(self, mock_api_call):
        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 404

        self.assertFalse(vb.usage_example("hillock"))

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_usageExample_empty_list(self, mock_api_call):
        res = {
            "list": [
                {
                    "definition": "a small mound or hill",
                    "thumbs_up": 0,
                    "word": "hillock",
                    "example": "I went to the to of the hillock to look around.",
                    "thumbs_down": 3
                }
            ]
        }

        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 200
        mock_api_call.return_value.json.return_value = res

        self.assertFalse(vb.usage_example("hillock"))

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_pronunciation_found(self, mock_api_call):
        res = [
            {
                "rawType": "ahd-legacy",
                "seq": 0,
                "raw": "hip"
            },
            {
                "rawType": "arpabet",
                "seq": 0,
                "raw": "HH IH2 P AH0 P AA1 T AH0 M AH0 S"
            }
        ]

        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 200
        mock_api_call.return_value.json.return_value = res

        expected_result = '[{"rawType": "ahd-legacy", "raw": "hip", "seq": 0}, {"rawType": "arpabet", "raw": "HH IH2 P AH0 P AA1 T AH0 M AH0 S", "seq": 1}]'
        result = vb.pronunciation("hippopotamus")

        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(expected_result, result)
        else:
            self.assertCountEqual(expected_result, result)

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_pronunciation_not_found(self, mock_api_call):
        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 404

        self.assertFalse(vb.pronunciation("hippopotamus"))

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_hyphenation_found(self, mock_api_call):
        res = [
            {
                "seq": 0,
                "type": "secondary stress",
                "text": "hip"
            },
            {
                "seq": 1,
                "text": "po"
            }
        ]

        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 200
        mock_api_call.return_value.json.return_value = res

        expected_result = '[{"seq": 0, "text": "hip", "type": "secondary stress"}, {"seq": 1, "text": "po"}]'
        result = vb.hyphenation("hippopotamus")

        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(expected_result, result)
        else:
            self.assertCountEqual(expected_result, result)

    @mock.patch('vocabulary.vocabulary.requests.get')
    def test_hyphenation_not_found(self, mock_api_call):
        mock_api_call.return_value = mock.Mock()
        mock_api_call.return_value.status_code = 404

        self.assertFalse(vb.hyphenation("hippopotamus"))

    def test_respond_as_dict_1(self):
        data = json.loads('[{"text": "hummus", "seq": 0}]')
        expected_result = {0: {"text": "hummus"}}
        result = rp().respond(data, 'dict')
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(expected_result, result)
        else:
            self.assertCountEqual(expected_result, result)

    def test_respond_as_dict_2(self):
        data = json.loads('[{"text": "hummus", "seq": 0},{"text": "hummusy", "seq": 1}]')
        expected_result = {0: {"text": "hummus"}, 1: {"text": "hummusy"}}
        result = rp().respond(data, 'dict')
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(expected_result, result)
        else:
            self.assertCountEqual(expected_result, result)

    def test_respond_as_dict_3(self):
        data = json.loads('{"text": ["hummus"]}')
        expected_result = {"text": "hummus"}
        result = rp().respond(data, 'dict')
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(expected_result, result)
        else:
            self.assertCountEqual(expected_result, result)

    def test_respond_as_list_1(self):
        data = json.loads('[{"text": "hummus", "seq": 0}]')
        expected_result = ["hummus"]
        result = rp().respond(data, 'list')
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(expected_result, result)
        else:
            self.assertCountEqual(expected_result, result)

    def test_respond_as_list_2(self):
        data = json.loads('[{"text": "hummus", "seq": 0},{"text": "hummusy", "seq": 1}]')
        expected_result = ["hummus", "hummusy"]
        result = rp().respond(data, 'list')
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(expected_result, result)
        else:
            self.assertCountEqual(expected_result, result)

    def test_respond_as_list_3(self):
        data = json.loads('{"text": ["hummus"]}')
        expected_result = ["hummus"]
        result = rp().respond(data, 'list')
        if sys.version_info[:2] <= (2, 7):
            self.assertItemsEqual(expected_result, result)
        else:
            self.assertCountEqual(expected_result, result)


if __name__ == "__main__":
    unittest.main()
