# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком
виде на стандартный поток вывода:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

template

"""
with open('ospf.txt') as g:
    for line in g:
        data = line.split()
        print(f"Prefix                {data[1]}")
        print(f"AD/Metric             {data[2][1:7]}")
        print(f"Next-Hop              {data[4].replace(',','')}")
        print(f"Last update           {data[5].replace(',','')}")
        print(f"Outbound Interface    {data[6]} \n")