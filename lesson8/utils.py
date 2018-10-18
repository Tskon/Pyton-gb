import os


def create_file(name, text=None):
  with open(name, 'w', encoding='utf-8') as f:
    if text:
      f.write(text)


def create_folder(name):
  try:
    os.mkdir(name)
  except FileExistsError:
    print('Такая папка уже есть')


def get_list(folders_only=False):
  result = os.listdir()
  if folders_only:
    result = [f for f in result if os.path.isdir(f)]
  print(result)


if __name__ == '__main__':
  create_file('text.dat', 'text')
  create_folder('fff')
  get_list()
  get_list(True)
