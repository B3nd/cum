#!usr/bin/env python
# -*- coding: utf-8 -*-

import pyttsx3
from time import sleep

tts = pyttsx3.init()

voices = tts.getProperty('voices')

# Задать голос по умолчанию

tts.setProperty('voice', 'ru') 

# Попробовать установить предпочтительный голос

# for voice in voices:

#     if voice.name == 'Aleksandr':

#         tts.setProperty('voice', voice.id)

#tts.say('Командный голос вырабатываю, товарищ генерал-полковник!')
tts.say("Я......Хочу......Хуитцы")
tts.runAndWait()
# while 1:
#     tts.say("cum")
#     tts.runAndWait()
#     # sleep(0.5)