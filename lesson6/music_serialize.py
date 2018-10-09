import json
import pickle

group = {
  'name': 'Oomph',
  'tracks': ['Augen auf!','Supernova'],
  'albums': [{'name': 'Ego', 'year': 2001},{'name': 'Wahrheit oder Pflicht', 'year': 2004}]
}

groupBytes = pickle.dumps(group)
groupJson = json.dumps(group)

print('in bytes:', '\n', groupBytes, '\n')
print('in JSON:', '\n', groupJson)

with open('group.pickle', 'wb') as f:
  f.write(groupBytes)
  pass

with open('group.json', 'w', encoding='utf-8') as f:
  f.write(groupJson)
  pass
