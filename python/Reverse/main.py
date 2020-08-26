#!usr/bin/env python
# -*- coding: utf-8 -*-
s = input("Введите строку: ")
r_s = ""
for i in range(0, len(s)):
    r_s = r_s + s[len(s) - i - 1]
print(r_s)
