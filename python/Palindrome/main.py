#!usr/bin/env python
# -*- coding:utf-8 -*-
main_string = input("Введите строку: ")
palindrome = True
main_string = main_string.replace(" ", "")
main_string = main_string.upper()
for i in range(0, len(main_string)):
    if main_string[i] == main_string[len(main_string)-i-1]:
       pass 
    else:
        palindrome = False
        break
if palindrome:
    print("Строка является палинромом")
else:
    print('Строка не является палиндроимом')

