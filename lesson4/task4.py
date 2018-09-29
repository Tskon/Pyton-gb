# Усложним предыдущее задание, измените сущности, добавив новый параметр — armor = 1.2. Теперь надо добавить функцию,
# которая будет вычислять и возвращать полученный урон по формуле damage/armor. Следовательно, у вас должно быть 2 функции,
# одна наносит урон, вторая вычисляет урон по отношению к броне.
import math

userName = input('Введите свое имя: ')

player = {
  'name': userName,
  'health': 100,
  'damage': 50,
  'armor': 1.5
}

enemy = {
  'name': 'Enemy',
  'health': 100,
  'damage': 33,
  'armor': 1.2
}

def getDmgValue(dmg, armor):
  return round(dmg / armor)

def attack(person1, person2):
  person2['health'] = person2['health'] - getDmgValue(person1['damage'], person2['armor'])

print('До атак', player, enemy)
attack(player, enemy)
print('Атака 1', player, enemy)
attack(enemy, player)
print('Атака 2', player, enemy)