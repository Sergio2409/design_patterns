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
from observer import Observer


class Payroll(Observer):

    def update(self, changed_employee, new_salary):
        print(f'Cut a new check for `{changed_employee.name}`! Her/His salary is now {new_salary}')


class TaxMan(Observer):

    def update(self, changed_employee, new_salary):
        print(f'Send `{changed_employee.name}` a new tax bill!')
