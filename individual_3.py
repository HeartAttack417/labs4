#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# . Путем вставок и удаления символов исправить ошибки:
# в слове прроцесор;
# во фразе теекстовыйфайл;
# во фразе програма и аллгоритм;
# во фразе процесор и паммять.

if __name__ == '__main__':
    word1 = 'прроцесор'
    word2 = 'теекстовыйфайл'
    phraz1 = 'програма и аллгоритм'
    phraz2 = 'процесор и паммять'

    word1 = word1.replace(word1[1], '', 1)
    word1 = word1[:6] + 'c' + word1[6:]
    print(word1)

    word2 = word2.replace(word2[1], '', 1)
    word2 = word2[:9] + ' ' + word2[9:]
    print(word2)

    phraz1 = phraz1[:6] + 'м' + phraz1[6:]
    phraz1 = phraz1.replace('л', '', 1)
    print(phraz1)

    phraz2 = phraz2[:5] + 'с' + phraz2[5:]
    phraz2 = phraz2.replace('м', '', 1)
    print(phraz2)