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
Singleton class example

"""


class Tigger(object):

    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super(Tigger, cls).__new__(cls)
        return cls.instance

    def __str__(self):
        return f"I'm the only one: {id(self)}!"

    def roar(self):
        return 'Grrr!'
