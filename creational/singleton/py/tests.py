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
from tigger import Tigger


class SingletonTest(unittest.TestCase):

    def test_unique_instance(self):
        a = Tigger()
        b = Tigger()

        print(f'ID(a) = {id(a)}')
        print(f'ID(b) = {id(b)}')
        print(f'Are the the same object? {a is b}')
        print(a)
        print(b)
        self.assertTrue(a is b)


if __name__ == '__main__':
    unittest.main()
