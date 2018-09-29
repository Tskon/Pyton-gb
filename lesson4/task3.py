# Опишем пару сущностей player и enemy через словарь, который будет иметь ключи и значения: name — строка, полученная от
# пользователя, health — 100, damage — 50. Поэкспериментируйте с значениями урона и жизней по желанию. Теперь надо создать
# функцию attack(person1, person2), аргументы можете указать свои, функция в качестве аргумента будет принимать атакующего
# и атакуемого, должна получить параметр damage атакующего и отнять это количество health от атакуемого. Функция должна
# сама работать с словарями и изменять их значения.

userName = input('Введите свое имя: ')

player = {
  'name': userName,
  'health': 100,
  'damage': 50
}

enemy = {
  'name': 'Enemy',
  'health': 100,
  'damage': 33
}

def attack(person1, person2):
  person2['health'] = person2['health'] - person1['damage']

print('До атак', player, enemy)
attack(player, enemy)
print('Атака 1', player, enemy)
attack(enemy, player)
print('Атака 2', player, enemy)