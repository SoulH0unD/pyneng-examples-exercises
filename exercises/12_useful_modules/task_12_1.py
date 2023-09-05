# -*- coding: utf-8 -*-
"""
Задание 12.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.

Функция ожидает как аргумент список IP-адресов.

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для проверки доступности IP-адреса, используйте команду ping (запуск ping через subprocess).
IP-адрес считается доступным, если выполнение команды ping отработало с кодом 0 (returncode).
Нюансы: на Windows returncode может быть равен 0 не только, когда ping был успешен,
но для задания нужно проверять именно код. Это сделано для упрощения тестов.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
import subprocess



def ping_ip_addresses(list_ip_address):
    ip_available = []
    ip_not_available = []
    for ip_address in list_ip_address:
        result = subprocess.run(['ping', '-c', '3', '-n', ip_address], stdout=subprocess.DEVNULL)
        if result.returncode == 0:
            ip_available.append(ip_address)
        else:
            ip_not_available.append(ip_address)

    return ip_available, ip_not_available


if __name__ == '__main__':
    l_ip = ['8.8.8.8', '7.7.7.7']


    print(ping_ip_addresses(l_ip))