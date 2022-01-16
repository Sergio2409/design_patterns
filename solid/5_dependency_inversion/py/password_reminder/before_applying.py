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
Here is an example of a PasswordReminder that connects to a MySQL database:

"""


class MySQLConnection:

    def connect(self):
        print('Connecting to MySQL connection')


class PasswordReminder:

    def __init__(self, db_connection: MySQLConnection):
        self.db_connection = db_connection

    def open_database(self):
        self.db_connection.connect()
