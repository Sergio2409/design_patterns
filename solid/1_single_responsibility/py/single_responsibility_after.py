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


class PaymentMethod(ABC):

    def __init__(self, security_code):
        self.security_code = security_code

    @abstractmethod
    def pay(self) -> bool:
        pass


class DebitPayment(PaymentMethod):
    def pay(self):
        print("Processing debit payment type")
        print(f"Verifying security code: {self.security_code}")
        return True


class CreditPayment(PaymentMethod):
    def pay(self):
        print("Processing credit payment type")
        print(f"Verifying security code: {self.security_code}")
        return True


class Order:

    def __init__(self, payment_method: PaymentMethod):
        self.items = []
        self.quantities = []
        self.prices = []
        self.status = "open"
        self.payment_method = payment_method

    def add_item(self, name, quantity, price):
        self.items.append(name)
        self.quantities.append(quantity)
        self.prices.append(price)

    def total_price(self):
        total = 0
        for i in range(len(self.prices)):
            total += self.quantities[i] * self.prices[i]
        return total

    def checkout(self):
        if self.payment_method.pay():
            self.status = "paid"
        else:
            raise Exception(f"An error occurred paying the order")


if __name__ == '__main__':
    order = Order(DebitPayment("0372846"))
    order.add_item("Keyboard", 1, 50)
    order.add_item("SSD", 1, 150)
    order.add_item("USB cable", 2, 5)

    print(order.total_price())
    order.checkout()



