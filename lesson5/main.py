import os
from task1 import *
from task2 import *

os.listdir(os.path.dirname(os.path.realpath(__file__)))

createDirs()
print(os.listdir(os.path.dirname(os.path.realpath(__file__))))

delDirs()
print(os.listdir(os.path.dirname(os.path.realpath(__file__))))

print(randEl(['123aee', 'ads', 3.2, 32]))