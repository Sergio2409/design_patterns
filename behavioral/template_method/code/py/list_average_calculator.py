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


class ListAverageCalculator(AverageCalculator):

    def __init__(self, number_list):
        self.number_list = number_list
        self.index = 0

    def has_next(self):
        return self.index < len(self.number_list)

    def next_item(self):
        value = self.number_list[self.index]
        self.index += 1
        return value
