import json
import pickle

with open('group.pickle', 'rb') as f:
  groupFromBytes = pickle.load(f)
  pass

with open('group.json', 'r') as f:
  groupFromJson = json.load(f)
  pass

print('from bytes:', '\n', groupFromBytes, '\n')
print('from JSON:', '\n', groupFromJson)