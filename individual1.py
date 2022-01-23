#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if __name__ == '__main__':
    m = int(input("Введите номер месяца: "))

    if m == 1 or m == 2 or m == 12:
        print("Декабрь, Январь, Февраль")
    elif m == 3 or m == 4 or m == 5:
        print("Март, Апрель, Май")
    elif m == 6 or m == 7 or m == 8:
        print("Июнь, Июль, Август")
    elif m == 9 or m == 10 or m == 11:
        print("Сентябрь, Октябрь, Ноябрь")
    else:
        print("Ошибка!", file=sys.stderr)
        exit(1)