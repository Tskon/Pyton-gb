import math

while (True):
  answer = int(input('Введите число от 1 до 100: '))
  if (1 > answer or answer > 100):
    print('Неверный ввод')
  else:
    break

minNum = 1
maxNum = 100

while(True):
  cpuAnswer = math.ceil(maxNum/2)

  userResult = int(input('Вы загадали число {}. Компььютер предполагает что ответ {}.\nПравильный ли ответ?\n'.format(answer, cpuAnswer) +
                       '1.Ответ правильный!\n2.Загаданное число меньше\n3.Загаданное число больше\nВведите вариант ответа: '))
