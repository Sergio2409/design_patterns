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

First, the MySQLConnection is the low-level module while the PasswordReminder is high level, but according to the
definition of D in SOLID, which states to Depend on abstraction, not on concretions. This snippet above violates this
principle as the PasswordReminder class is being forced to depend on the MySQLConnection class.

Later, if you were to change the database engine, you would also have to edit the PasswordReminder class, and this would
violate the open-close principle.

The PasswordReminder class should not care what database your application uses. To address these issues, you can code to
an interface sin
"""
from abc import ABC, abstractmethod


class DBConnectionInterface(ABC):

    @abstractmethod
    def connect(self):
        pass


class MySQLConnection(DBConnectionInterface):

    def connect(self):
        print('Connecting to MySQL database')


class SQLiteConnection(DBConnectionInterface):

    def connect(self):
        print('Connecting to SQLite database')


class PasswordReminder:

    def __init__(self, db_connection: DBConnectionInterface):
        self.db_connection = db_connection

    def open_database(self):
        self.db_connection.connect()


if __name__ == '__main__':
    mysql_connection = MySQLConnection()
    sqlite_connection = SQLiteConnection()
    pwd_mysql_reminder = PasswordReminder(mysql_connection)
    pwd_mysql_reminder.open_database()
    pwd_sqlite_reminder = PasswordReminder(sqlite_connection)
    pwd_sqlite_reminder.open_database()
