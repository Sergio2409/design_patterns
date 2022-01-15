#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# Copyright (c) ░s░e░r░g░i░o░v░a░l░d░e░s░2░4░0░9░
# Mail: sergiovaldes2409@gmail.com
#
# All rights reserved.
#
#
"""
Adapter pattern example

"""


class GeneratorAdapter:

    def __init__(self, generator):
        self.generator = generator

    def readline(self):
        try:
            return next(self.generator)
        except StopIteration:
            return ''

    def close(self):
        pass

