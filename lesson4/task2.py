# Создайте функцию, принимающую на вход 3 числа и возвращающую наибольшее из них.

# Реализовал для любого количества чисел

def getMaxNum(*nums):
  maxNum = None
  for num in nums:
    if(maxNum == None or maxNum < num):
      maxNum = num
  return maxNum

print(getMaxNum(2, -7, 3, 4, 1))
