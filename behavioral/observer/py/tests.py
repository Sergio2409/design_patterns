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
from employee import Employee
from payroll import Payroll, TaxMan


class ObserverTest(unittest.TestCase):

    def test_proper_behaviour(self):
        emp1 = Employee('Amy Fowler', 50000)
        pay1 = Payroll()
        tax1 = TaxMan()

        emp1.add_observer(pay1)
        emp1.add_observer(tax1)

        print('Update 1')
        emp1.salary = 60000

        emp1.delete_observer(tax1)

        print('Update 2')
        emp1.salary = 65000
        # The important here isn't the test but check the out messages instead to check the proper notifications after
        # the salary changes.
        self.assertEqual(emp1.salary, 65000)


if __name__ == '__main__':
    unittest.main()
