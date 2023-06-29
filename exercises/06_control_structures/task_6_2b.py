# -*- coding: utf-8 -*-
"""
Задание 6.2b

Сделать копию скрипта задания 6.2a.

Дополнить скрипт: Если адрес был введен неправильно, запросить адрес снова.

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'
Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
while True:
   ip = input("Введите  IP-адрес в формате 10.0.1.1: ")
   dot_count = 0
   octet_count = 0

   for c in ip:
      if c == '.':
         dot_count += 1


   if dot_count == 3:
      ip_octet = ip.split('.')
      for oct in ip_octet:
         if oct.isdigit():
            if (0 <= int(oct) <= 255):
               octet_count += 1

   if octet_count == 4 and dot_count == 3:
      ip_oct1 = int(ip.split('.')[0])
      if ip_oct1 == 0:
         print('unassigned')
         break
      elif ip_oct1 > 0 and ip_oct1 < 224:
         print('unicast')
         break
      elif ip_oct1 > 223 and ip_oct1 < 240:
         print('multicast')
         break
      elif ip_oct1 == 255:
         print('local broadcast')
         break
      else:
         print('unused')
         break
   else:
      print('Неправильный IP-адрес')