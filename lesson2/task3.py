# Дан список заполненный произвольными целыми числами. Получите новый список, элементами которого будут только уникальные элементы исходного.

numList = [1, 15, 3, 1, 2, 12, 3]

# 1 вариант - убираем лишние дубли
uniqNumList1 = list(set(numList))
print('без дублей', uniqNumList1)


# 2 вариант - только неповторяющиеся числа
doubles = numList[:]
for num in set(numList):
  doubles.remove(num)

uniqNumList2 = list(set(uniqNumList1) - set(doubles))

print('только неповторяющиеся', uniqNumList2)