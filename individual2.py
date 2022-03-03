#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':

    x = float(input("Введите координату x: "))
    y = float(input("Введите координату y: "))

    if (x*x + y*y <=1) and (x*x + y*y >= 0.25):
        print("Принадлежит")
    else:
        print("Не принадлежит")
