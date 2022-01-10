#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# Copyright (c) ░s░e░r░g░i░o░v░a░l░d░e░s░2░4░0░9░
# Mail: sergiovaldes2409@gmail.com
#
# All rights reserved.
#
#

import unittest
from file_average_calculator import FileAverageCalculator
from list_average_calculator import ListAverageCalculator


class TemplateTest(unittest.TestCase):

    def test_file_average(self):
        file = open('file')
        calculator = FileAverageCalculator(file)
        expected_result = 18.0
        self.assertEqual(calculator.average(), expected_result)

    def test_list_average(self):
        numbers = [4, 8, 15, 16, 23, 42]
        calculator = ListAverageCalculator(numbers)
        expected_result = 18.0
        self.assertEqual(calculator.average(), expected_result)


if __name__ == '__main__':
    unittest.main()
