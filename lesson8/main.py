import sys
from core import *

try:
  command = sys.argv[1]
  save_info('start')

  if command == 'list':
    get_list()
  elif command == 'create_file':
    create_file(sys.argv[2], sys.argv[3])
  elif command == 'create_folder':
    create_folder(sys.argv[2])
  elif command == 'delete':
    delete_file(sys.argv[2])
  elif command == 'copy':
    copy_file(sys.argv[2], sys.argv[3])
  elif command == 'help':
    print("create_file name - создать файл\ncreate_folder name - создать папку\ndelete name - удалить файл/папку\nlist True\False - список файлов/папок\ncopy name newName - копировать файл/папку")
except Exception as e:
  print("Что-то пошло не так: {}".format(e))

save_info('end')