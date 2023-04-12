#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os

if __name__ == '__main__':
    # Вывод списка имен всех файлов текущего рабочего каталога
    print("Все папки и файлы:", os.listdir())

    # Распечатать все файлы и папки рекурсивно
    for dirpath, dirnames, filenames in os.walk("."):
        # Перебор каталогов
        for dirname in dirnames:
            print("Каталог:", os.path.join(dirpath, dirname))
        # Перебор файлов
        for filename in filenames:
            print("Файл:", os.path.join(dirpath, filename))
