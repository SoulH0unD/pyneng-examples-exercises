# -*- coding: utf-8 -*-
"""
Задание 17.3

Создать функцию parse_sh_cdp_neighbors, которая обрабатывает
вывод команды show cdp neighbors.

Функция ожидает, как аргумент, вывод команды одной строкой (не имя файла).
Функция должна возвращать словарь, который описывает соединения между устройствами.

Например, если как аргумент был передан такой вывод:
R4>show cdp neighbors

Device ID    Local Intrfce   Holdtme     Capability       Platform    Port ID
R5           Fa 0/1          122           R S I           2811       Fa 0/1
R6           Fa 0/2          143           R S I           2811       Fa 0/0

Функция должна вернуть такой словарь:
{'R4': {'Fa 0/1': {'R5': 'Fa 0/1'},
        'Fa 0/2': {'R6': 'Fa 0/0'}}}

Интерфейсы должны быть записаны с пробелом. То есть, так Fa 0/0, а не так Fa0/0.


Проверить работу функции на содержимом файла sh_cdp_n_sw1.txt
"""
import re

def parse_sh_cdp_neighbors(neig):
    r_str = r"(?P<dev_id>\w+) +(?P<intd>\w+ \d+/\d+).+ +(?P<port>\w+ \d+/\d+)"
    int_dec = {}
    for line in neig.split('\n'):
        if 'show cdp neighbors' in line:
            device = line.split('>')[0]
        elif 'Eth ' in line:
            match = re.search(r_str, line)
            int_dec[match.group('intd')] = {match.group('dev_id'): match.group('port')}
    return {device: int_dec}
            

        


if __name__ == "__main__":
    with open('sh_cdp_n_sw1.txt') as f:
        n = f.read()

    print(parse_sh_cdp_neighbors(n))