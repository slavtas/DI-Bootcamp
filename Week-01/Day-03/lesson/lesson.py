# Differences between Lists and Dictionaries

# fruits = ['banana', 'apple', 'kiwi']
# print(fruits[1]) # in list you can acces items by index

user_info = ['Slava', 'slavtas@gmail.com', 39, True, 1.71]

user_info_dict = {'Name':'Slava',
                  'email':'slavtas@gmail.com',
                  'age':39,
                  'is female': False,
                  'height': 1.71,
                  'pets':['Finn', 'Milo', 'Bubbles'],
                  'family':[{'name':'Nata',
                            'age':32,
                            'relation':'wife'}],
                            'hobbies':[('yoga',3),('tennis',1),('chess',3)]                        
                            }

print(user_info_dict['Name'])
print(user_info_dict['pets'][1])
# print(user_info_dict['family']['relation'])
print(user_info_dict['hobbies'][2][-1])

# for key in user_info_dict.keys():
#     print(key)

# for value in user_info_dict.values():
#     print(value)

for key,value in user_info_dict.items():
    print(f'key:{key}')
    print(f'value:{value}')

#chaniging values

user_info_dict['email'] = 'slavtas@mail.ru' #replaces the value in given key

#adding values

user_info_dict['profession'] = 'Fullstack Developer'

#deleting key value

del user_info_dict['profession']

#checking if key/value exist in dict

print('pets' in user_info_dict.keys())
print('Slava' in user_info_dict.values())

print(user_info_dict)

#update() merge dicts

user_info_dict.update({'address': 'Arad'})

user_info_dict['family'].append({'name': 'Nathan',
                                 'age': 5,
                                 'relation': 'son'})

print(user_info_dict)

user_info2 = {'origin': 'Russia',
              'phone number': +972539528662,
              'car owner': True
              }
user_info_dict.update(user_info2)

print(user_info_dict)

# sample_dict = { 
#    "class":{ 
#       "student":{ 
#          "name":"Mike",
#          "marks":{ 
#             "physics":70,
#             "history":80
#          }
#       }
#    }
# }

# print(sample_dict['class']['student']['marks']['history'])

#for loops in dictionaries




