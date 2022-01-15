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
import random
from abc import ABC, abstractmethod


class ProcessingStrategy(ABC):

    @abstractmethod
    def create_ordering(self, tickets: list):
        pass


class Fifo(ProcessingStrategy):

    def create_ordering(self, tickets: list):
        return tickets


class Filo(ProcessingStrategy):

    def create_ordering(self, tickets: list):
        return reversed(tickets)


class Random(ProcessingStrategy):

    def create_ordering(self, tickets: list):
        random.shuffle(tickets)
        return tickets
