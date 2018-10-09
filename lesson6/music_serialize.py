import json
import pickle

group = {
  'название': 'Oomph',
  'треки': ['Augen auf!','Supernova'],
  'альбомы': [{'название': 'Ego', 'год': 2001},{'название': 'Wahrheit oder Pflicht', 'год': 2004}]
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
