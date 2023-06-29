# -*- coding: utf-8 -*-
"""
Задание 7.2b

Переделать скрипт из задания 7.2a: вместо вывода на стандартный поток вывода,
скрипт должен записать полученные строки в файл

Имена файлов нужно передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

При этом, должны быть отфильтрованы строки, которые содержатся в списке ignore
и строки, которые начинаются на '!'.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "configuration"]

from sys import argv


result = []
file_name = argv[1]
out_file = argv[2]
with open(file_name) as g:
    for line in g:
        if not line.startswith('!'):
            if not set(ignore) & set(line.split()):
                result.append(line)

with open(out_file, 'a') as o:
    for line in result:
        o.write(line)
