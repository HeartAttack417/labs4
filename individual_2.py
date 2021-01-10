#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Заменить в нем все вхождения буквосочетания ах на ух

if __name__ == '__main__':
    sentence = str(input("Введите предложение "))
    i = 0
    n = len(sentence) - 1
    for i in range(n):
        print(sentence[i])
        print(sentence[i+1])
        print("цикл")
        if 'а' == sentence[i] and 'х' == sentence[i+1]:
            sentence = sentence.replace(sentence[i], 'у')
    print(sentence)