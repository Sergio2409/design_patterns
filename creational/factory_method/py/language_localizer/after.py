#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -----------------------------------------------
# Copyright (c) ░s░e░r░g░i░o░v░a░l░d░e░s░2░4░0░9░
# Mail: sergiovaldes2409@gmail.com
#
# All rights reserved.
#
#
from abc import ABC, abstractmethod


class LanguageLocalizer:

    def localize(self, msg):
        """change the message using translations"""
        return self.translations.get(msg, msg)


class FrenchLocalizer(LanguageLocalizer):
    """ it simply returns the french version """

    def __init__(self):
        self.translations = {"car": "voiture", "bike": "bicyclette",
                             "cycle": "cyclette"}


class SpanishLocalizer(LanguageLocalizer):
    """it simply returns the spanish version"""

    def __init__(self):
        self.translations = {"car": "coche", "bike": "bicicleta",
                             "cycle": "ciclo"}


class Translator(ABC):

    lang_localizer: LanguageLocalizer = None

    def localize(self, msg):
        return self.lang_localizer.localize(msg)

    @abstractmethod
    def create_localizer(self) -> LanguageLocalizer:
        pass


class FrenchTranslator(Translator):

    def __init__(self):
        self.lang_localizer = self.create_localizer()

    def create_localizer(self) -> LanguageLocalizer:
        print('------- French Translator -------')
        return FrenchLocalizer()


class SpanishTranslator(Translator):

    def __init__(self):
        self.lang_localizer = self.create_localizer()

    def create_localizer(self) -> LanguageLocalizer:
        print('------- Spanish Translator -------')
        return SpanishLocalizer()


if __name__ == "__main__":
    message = ["car", "bike", "cycle"]
    f = FrenchTranslator()
    for msg in message:
        print(f.localize(msg))
    s = SpanishTranslator()
    for msg in message:
        print(s.localize(msg))
