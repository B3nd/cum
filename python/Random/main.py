#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

min = int(input("Введите минимальное число: "))
max = int(input("Введите максимальное число: "))

print("Ваше число: "+ str(int(random.uniform(min + 1, max))))
