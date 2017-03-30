#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
The MIT License (MIT)
Copyright © 2017 Chizzy Alaedu

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


__version__ = '0.0.1'
__author__ = "Chizzy Alaedu"


class Response(object):
    """
    |  Private methods       | Public methods   |
    |:----------------------:|------------------|
    | __respond_with_dict()  | respond()        |
    | __respond_with_list()  |                  |
    |                        |                  |
    """



    def __respond_with_dict(self, data):
        pass

    def __respond_with_list(self, data):
        pass

    def respond(self, data, format='json'):
        dispatchers = {
            "dict" : self.__respond_with_dict,
            "list" : self.__respond_with_list
        }

        if not dispatchers.get(format, False):
            return data

        return dispatchers[format](data)
