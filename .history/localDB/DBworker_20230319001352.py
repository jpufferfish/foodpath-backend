from replit import db

keys = db.keys()
print(keys)
k = ''

# for i in keys:
#   for j in db[i]:
#     k = j['username']
#     print('exercise:', j['exercise'])
#     print('weight:', j['weight'])
#     print('repitions:', j['repitions'])
#     print('time:', j['time'])
#     print('\n')
# print(k)
# dict = {}
# k =0
# for i in keys:
#   for j in db[i]:
#     dict.update( {
#       i : {
#        j['username'],
#        j['exercise'],
#        j['weight'],
#        j['repitions'],
#        j['time']
#       }
#     } )

# foodpath:
# exercise = light medium or extreme
for i in keys:
  for j in db[i]:
    k = j['username']
    print('exercise:', j['exercise'])
    print('weight(lbs):', j['weight'])
    # print('repitions:', j['repitions'])
    print('entryTime:', j['entryTime'])
    print('\n')
print(k)
dict = {}
k =0
for i in keys:
  for j in db[i]:
    dict.update( {
      i : {
       j['username'],
       j['entryID'],
       j['exercise'],
       j['weight'],
       j['food'],
       j['servings'],
       j['entryTime'],
      }
    } )

print(dict)
