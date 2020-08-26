#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

def r():
    return random.uniform(0.0, 1.0)

number = int(input("Введите колличество: "))
number_total = 0
number_in_circle = 0


for i in range(number):
    x = r()
    y = r()
    radius  = x**2 + y**2
    if radius <= 1:
        number_in_circle += 1
    number_total += 1

answer = 4 * number_in_circle / number_total
print(answer)
