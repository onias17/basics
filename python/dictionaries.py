# Dictionaries

dict = {'key1':'val1', 'key2':[1,2,3], 'key3':123, 'key4':{'123':[1,2,'onias']}}
print(dict)
print(dict['key2'])
print(dict['key4']['123'][2]) 
print(dict['key4']['123'][2].upper())
dict['key4']['123'][1] = 'nephi'
print(dict['key4'])
dict['key5'] = 'isaiah 26:3'
print(dict)