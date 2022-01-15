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
Module description goes here

"""
import unittest
from generator_adapter import GeneratorAdapter
from file_average_calculator import FileAverageCalculator


class AdapterTest(unittest.TestCase):

    def test_file_average(self):
        numbers = [4, 8, 15, 16, 23, 42]
        file = (numb for numb in numbers)
        calculator = FileAverageCalculator(GeneratorAdapter(file))
        expected_result = 18.0
        self.assertEqual(calculator.average(), expected_result)


if __name__ == '__main__':
    unittest.main()
