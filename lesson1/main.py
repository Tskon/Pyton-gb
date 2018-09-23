print('=== 1 task ===')
num = int(input('input some number: '))
print('Your number +2 is', num + 2)

print('=== 2 task ===')
num = int(input('Please input correct number (0 < number < 10): '))
while(not 0 < num < 10):
  num = int(input('Incorrect number! Please input correct number (0 < number < 10): '))
print(num**2)

print('=== 3 task ===')
name = input('Enter your name: ')
surname = input('Enter your surname: ')
age = int(input('Enter your age: '))
weight = int(input('Enter your weight: '))

if age < 30 and 50 <= weight <= 120:
  print(name, surname, ', Вы в отличном состоянии')
elif age > 30 and not 50 <= weight <= 120:
  if age > 40:
    print(name, surname, ', обратитесь к врачу')
  else:
    print(name, surname, ', Вам нужно начать вести правильный образ жизни')
else:
  print('Для Вас пока советов нет')