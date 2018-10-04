# Создайте модуль, а в нем — функцию, которая принимает список и возвращает из него случайный элемент.
# Если список пустой, функция должна вернуть None. Проверьте работу функций в этом же модуле.

import random

def randEl(list):
  if len(list):
    return random.choice(list)
  else:
    return None

if __name__ == '__main__':
  print(randEl([1, 'ads', 3]))
  print(randEl([]))