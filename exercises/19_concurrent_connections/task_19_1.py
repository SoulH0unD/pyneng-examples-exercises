# -*- coding: utf-8 -*-
"""
Задание 19.1

Создать функцию ping_ip_addresses, которая проверяет пингуются ли IP-адреса.
Проверка IP-адресов должна выполняться параллельно в разных потоках.

Параметры функции ping_ip_addresses:
* ip_list - список IP-адресов
* limit - максимальное количество параллельных потоков (по умолчанию 3)

Функция должна возвращать кортеж с двумя списками:
* список доступных IP-адресов
* список недоступных IP-адресов

Для выполнения задания можно создавать любые дополнительные функции.

Для проверки доступности IP-адреса, используйте ping.

Подсказка о работе с concurrent.futures:
Если необходимо пинговать несколько IP-адресов в разных потоках,
надо создать функцию, которая будет пинговать один IP-адрес,
а затем запустить эту функцию в разных потоках для разных
IP-адресов с помощью concurrent.futures (это надо сделать в функции ping_ip_addresses).
"""
import subprocess
from concurrent.futures import ThreadPoolExecutor

def ping_ip(ip):
    reply = subprocess.run(['ping', '-c', '3', '-n', ip],
                           stdout=subprocess.PIPE,
                           stderr=subprocess.PIPE,
                           encoding='utf-8')
    if reply.returncode == 0:
        return True
    else:
        return False


def ping_ip_addresses(ip_list, limit = 3):
    with ThreadPoolExecutor(max_workers=limit) as executor:
        active = []
        no_active = []
        for ip in ip_list:
            future = executor.submit(ping_ip, ip)
            if future.result():
                active.append(ip)
            else:
                no_active.append(ip)

    return active, no_active





if __name__ == "__main__":
    ip_list = ['10.1.22.130', '10.1.22.131', '10.39.5.160', '198.1.1.1', '192.1.1.1']
    print(ping_ip_addresses(ip_list))
    # for ip in ip_list:
    #     print(ip, ping_ip(ip))