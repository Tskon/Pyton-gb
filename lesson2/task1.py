# Даны два произвольных списка. Удалите из первого списка элементы, присутствующие во втором.

peopleList = ['Mike', 'Nick', 'Potato', 'Sam', 'Orange']
foodList = ['Apple', 'Orange', 'Potato']

peopleList = list(set(peopleList) - set(foodList))

print(peopleList)


