import sys
from core import *
import game
import os

try:
  command = sys.argv[1]
  arg1 = None
  arg2 = None
  save_info('start')

  if command == 'change_dir':
    os.chdir(sys.argv[2])
    input = input("введите следующую команду: ").split(' ')
    command = input[0]
    arg1 = input[1]
    arg2 = input[2]

  if command == 'list':
    get_list()
  elif command == 'create_file':
    create_file(arg1 or sys.argv[2], arg2 or sys.argv[3])
  elif command == 'create_folder':
    create_folder(arg1 or sys.argv[2])
  elif command == 'delete':
    delete_file(arg1 or sys.argv[2])
  elif command == 'copy':
    copy_file(arg1 or sys.argv[2], arg2 or sys.argv[3])
  elif command == 'game':
    game.startGame()
  elif command == 'help':
    print(
      "create_file name - создать файл\ncreate_folder name - создать папку\ndelete name - удалить файл/папку\nlist True\False - список файлов/папок\ncopy name newName - копировать файл/папку\ngame - играть\nchange_dir path - сменить текущую папку выполнения скрипта")
except Exception as e:
  print("Что-то пошло не так: {}".format(e))

save_info('end')
