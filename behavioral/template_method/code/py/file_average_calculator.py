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
Template Method pattern example

"""
from calculator import AverageCalculator


class FileAverageCalculator(AverageCalculator):

    def __init__(self, file):
        self.file = file
        self.last_line = self.file.readline()

    def has_next(self):
        return self.last_line != ''

    def next_item(self):
        result = float(self.last_line)
        self.last_line = self.file.readline()
        return result

    def dispose(self):
        self.file.close()






