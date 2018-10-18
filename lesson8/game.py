import math

def startGame():
  while (True):
    answer = int(input('Введите число от 1 до 100: '))
    if (1 > answer or answer > 100):
      print('Неверный ввод')
    else:
      break

  minNum = 1
  maxNum = 100
  lieCount = 0
  isCpuRight = False
  tryCount = 0

  while(True):
    tryCount += 1

    cpuAnswer = math.ceil((minNum - 1) + (maxNum - (minNum - 1))/2)
    lie = ''

    if (lieCount > 0):
      lie = 'В процессе игры вы соврали {} раз. '.format(lieCount)

    userResult = int(input(lie + 'Вы загадали число {}. Компььютер предполагает что ответ {}.\nПравильный ли ответ?\n'.format(answer, cpuAnswer) +
                         '1.Ответ правильный!\n2.Загаданное число меньше\n3.Загаданное число больше\n\nВведите вариант ответа: '))

    if answer == cpuAnswer:
      isCpuRight = True # Специально не прерываем игру, ведь мы можем соврать!

    if answer > cpuAnswer and userResult != 3:
      lieCount += 1
    if answer < cpuAnswer and userResult != 2:
      lieCount += 1
    if userResult == 1:
      break

    if(maxNum == cpuAnswer or minNum == cpuAnswer):
      print('\nКомпьютер смотрит на вас подозрительно и заканчивает игру. Процессор недобро шумит... Вам явно стоит быть осмотрительнее.')
      break

    if userResult == 2:
      maxNum = cpuAnswer
    else:
      minNum = cpuAnswer

    print('\n=== Конец раунда ===\n')

  print('Игра окончена за {} раунда(-ов)! Вы соврали {} раз(-а)'.format(tryCount, lieCount))

  if(isCpuRight):
    print('Компьютеру удалось угадать число!')
  else:
    print('Компьютер не угадал верное число.')