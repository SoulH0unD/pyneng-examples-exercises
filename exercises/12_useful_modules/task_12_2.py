# -*- coding: utf-8 -*-
"""
Задание 12.2


Функция ping_ip_addresses из задания 12.1 принимает только список адресов,
но было бы удобно иметь возможность указывать адреса с помощью диапазона,
например, 192.168.100.1-10.

В этом задании необходимо создать функцию convert_ranges_to_ip_list,
которая конвертирует список IP-адресов в разных форматах в список,
где каждый IP-адрес указан отдельно.

Функция ожидает как аргумент список, в котором содержатся IP-адреса
и/или диапазоны IP-адресов.

Элементы списка могут быть в формате:
* 10.1.1.1
* 10.1.1.1-10.1.1.10
* 10.1.1.1-10

Если адрес указан в виде диапазона, надо развернуть диапазон в отдельные
адреса, включая последний адрес диапазона.
Для упрощения задачи, можно считать, что в диапазоне всегда меняется только
последний октет адреса.

Функция возвращает список IP-адресов.

Например, если передать функции convert_ranges_to_ip_list такой список:
['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']

Функция должна вернуть такой список:
['8.8.4.4', '1.1.1.1', '1.1.1.2', '1.1.1.3', '172.21.41.128',
 '172.21.41.129', '172.21.41.130', '172.21.41.131', '172.21.41.132']

"""
import ipaddress
 
 
def check_ip(ip):
    try:
        ipaddress.ip_address(ip)
    except ValueError:
        return False
    else:
        return True

def convert_ranges_to_ip_list(l_ip_adress):
    list_ip_adress = []
    for ip_adress in l_ip_adress:
        if check_ip(ip_adress):
            list_ip_adress.append(ip_adress)
        else:
            tmp = ip_adress.split('-')
            octets = tmp[0].split('.')
            start_count = int(octets[-1])
 
            if '.' in tmp[1]:
                end_count = int(tmp[1].split('.')[-1])
            else:
                end_count = int(tmp[1])
            
            for i in range(start_count, end_count + 1):
                list_ip_adress.append(f'{octets[0]}.{octets[1]}.{octets[2]}.{i}')


    return list_ip_adress

if __name__ == '__main__':
    l_ip = ['8.8.4.4', '1.1.1.1-3', '172.21.41.128-172.21.41.132']
    print(convert_ranges_to_ip_list(l_ip))