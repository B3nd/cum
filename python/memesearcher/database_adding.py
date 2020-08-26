#!usr/bin/dev/python
# -*- coding:utf-8 -*-
import os
import logging
import mongo_setup
import data_service as svc
from image_text import ImageText

def main():
    mongo_setup.global_init()
    for im_name in os.listdir('/home/stas/coding/python/memesearcher/images'):
        image_text = svc.recognise_text('/home/stas/coding/python/memesearcher/images/' + im_name)
        if image_text != None:
            print(image_text)

if __name__ == '__main__':
    main()
    