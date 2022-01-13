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
Dependency Inversion applied to the code inside `before_applying` file

"""

from abc import ABC, abstractmethod


class Switchable(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class LightBulb(Switchable):

    def turn_on(self):
        print("LightBulb: turned on...")

    def turn_off(self):
        print("LightBulb: turned off...")


class Fan(Switchable):

    def turn_on(self):
        print("Fan: turned on...")

    def turn_off(self):
        print("Fan: turned off...")


class ElectricPowerSwitch:

    def __init__(self, switchable: Switchable):
        self.switchable = switchable
        self.on = False

    def press(self):
        if self.on:
            self.switchable.turn_off()
            self.on = False
        else:
            self.switchable.turn_on()
            self.on = True


if __name__ == '__main__':
    light_bulb = LightBulb()
    fan = Fan()
    switch_light_bulb = ElectricPowerSwitch(light_bulb)
    switch_light_bulb.press()
    switch_light_bulb.press()
    switch_fan = ElectricPowerSwitch(fan)
    switch_fan.press()
    switch_fan.press()




