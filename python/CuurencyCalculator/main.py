#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pycbrf.toolbox import ExchangeRates

rates = ExchangeRates()
curr_name = raw_input("Введите кoд валюты: ")
curr = None
value = None
answer = None
while 1:
    try:
        curr = rates[curr_name]
        auth = raw_input("Вы выбрали " + curr.name.encode('utf8') + "? [Yes/No]\n")
        if auth == "Yes":
            print("Ща тогда посчитаем...")
            break
        elif auth == "No":
            curr_name = raw_input("Тогда введите новый код валюты: ")
            break
        else:
            print("Вам же написали: Yes или No, зачем вы пишете " + auth + "?")
    except KeyError:
        print("Неправильно введён код валюты")
        curr_name = raw_input("Введите кoд валюты: ")
currency = float(curr.value)
settings = raw_input("Выберите вариант: \n1)Из рублей \n2)В рубли\n")
while 1:
    try:
        value = int(input("Введите колличество: "))
        break
    except ValueError:
            print("Дэбил, цифры введи")


if settings == '1':
    answer = value * currency
    print("ну палучаэтца " + str(answer) + " Рубликов")
elif settings == '2':
    answer = value / currency
    print("Ну палучаэтца " + str(answer) + curr.name.encode('utf8'))
else:
    setting = raw_input('Пожалуйста, напрягите ваши две извилины и выберите вариант: \n1)Из рублей \n2)В рубли\n')

