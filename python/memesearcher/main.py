#!usr/bin/dev/python
# -*- coding:utf-8 -*-
from database_adding import main as db
from search import main as search

def main():
    choose = input('Hello do you want to [s]earch or [u]pdate database? ')
    if choose == 's':
        search()

    elif choose == 'u':
        db()
    
    else:
        return


if __name__ == '__main__':
    main()