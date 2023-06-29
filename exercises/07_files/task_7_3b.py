# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Пример работы скрипта:

Enter VLAN number: 10
10       0a1b.1c80.7000      Gi0/4
10       01ab.c5d0.70d0      Gi0/8

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
vlan = input('Enter VLAN number: ')

template = "{:<9}{:<19}{}"
macs = []
with open('CAM_table.txt') as g:
    for line in g:
        line_mac = line.split()
        if (len(line_mac) > 2) and '.' in line_mac[1]:
            macs.append([int(line_mac[0]), line_mac[1], line_mac[3]])

for i in sorted(macs):
    if i[0] == int(vlan):
        print(template.format(i[0], i[1], i[2]))