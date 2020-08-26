#!usr/bin/dev/python
# -*- coding:utf-8 -*-
import mongo_setup
import threading
import os
import data_service as svc
from image_text import ImageText

def mongo_start():
    os.system('mongo')

def main():
    # x = threading.Thread(target=mongo_start, daemon=True)
    # x.start()
    mongo_setup.global_init()
    query = input('Input text you want to search: \n').lower()
    print('\n')
    found = False
    refs = []
    for u in svc.list_all():
        if query in u.text_without_anything or \
        query in u.text_with_low_enhancer or \
        query in u.text_with_high_enhancer or \
        query in u.gray_text or \
        query in u.text_with_CLAHE or \
        query in u.only_black_and_white_text:
            found = True
            refs.append(u.image_ref)
    if found:
        print('Here are what we could found: \n')
        command = 'feh '
        for r in refs:
            command += r + ' '
            print(r)
        os.system(command)
    else:
        print('We couldn\'t find any images with this text')
if __name__ == '__main__':
    main()