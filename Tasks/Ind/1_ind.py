#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# 8. Написать программу, которая считывает текст из файла и выводит на экран только цитаты,
# то есть предложения, заключенные в кавычки.

if __name__ == '__main__':
    with open('1_ind.txt', 'r', encoding='utf-8') as f:
        text = f.read()
    quote = []
    for i in range(0, len(text)):
        if text[i] == '"':
            quote.append(i)
    i = 0
    while i < len(quote):
        print(text[quote[i]:quote[i+1]+1])
        i += 2
