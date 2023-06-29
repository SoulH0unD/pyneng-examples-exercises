# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса.
Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение: 'Неправильный IP-адрес'

Сообщение "Неправильный IP-адрес" должно выводиться только один раз,
даже если несколько пунктов выше не выполнены.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
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
   elif ip_oct1 > 0 and ip_oct1 < 224:
      print('unicast')
   elif ip_oct1 > 223 and ip_oct1 < 240:
      print('multicast')
   elif ip_oct1 == 255:
      print('local broadcast')
   else:
      print('unused')
else:
   print('Неправильный IP-адрес')