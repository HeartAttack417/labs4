#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. В нем слова разделены одним или несколькими пробелами (символ «-»
# в предложении отсутствует). Определить количество слов в предложении. Рассмотреть два
# случая:
# начальные и конечные пробелы в предложении отсутствуют;
# начальные и конечные пробелы в предложении имеются.

if __name__ == '__main__':

    # Если пробела в начале строки нет
    sentence = str(input("Введите предложение "))
    sentence = sentence.split(' ')
    count = 0
    for item in sentence:
        count += 1
    print(count)

    # Если пробел в начале строки есть
    sentence = str(input("Введите предложение "))
    len = len(sentence)
    sentence = sentence[1:len-1]
    sentence = sentence.split(' ')
    count = 0
    for item in sentence:
        count += 1
    print(count)