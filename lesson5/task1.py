# Создайте модуль, а в нем — функцию, создающую директории dir_1 — dir_9 в папке, из которой запущен данный скрипт.
# Напишите вторую функцию, удаляющую эти папки. Проверьте работу функций в этом же модуле.

import os

def createDirs():
  for i in range(1, 10):
    dir = os.path.dirname(__file__) + '/dir_' + str(i)
    os.mkdir(dir)

def delDirs():
  for i in range(1, 10):
    dir = os.path.dirname(__file__) + '/dir_' + str(i)
    os.rmdir(dir)

if __name__ == '__main__':
  createDirs()
  # delDirs()  # раскомментить для удаления каталогов

