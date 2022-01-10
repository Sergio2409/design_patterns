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
Observer patter example

"""
from abc import ABC, abstractmethod


class Observer(ABC):

    @abstractmethod
    def update(self, observable, *args):
        pass


class Observable:
    def __init__(self):
        self.__observers = []

    def add_observer(self, observer):
        self.__observers.append(observer)

    def delete_observer(self, observer):
        self.__observers.remove(observer)

    def notify_observers(self, *args):
        for observer in self.__observers:
            observer.update(self, *args)


