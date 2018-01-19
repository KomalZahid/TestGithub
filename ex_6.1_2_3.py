# Exercise # 6.1:
data = {'first_name' : 'komal','last_name':'zahid','age':'23','city':'karachi'}

for key, value in data.items():
    print(key + " : " + value)
###  x--------------------------------------x
# Exercise # 6.2:
dict = {'komal' : '3',
        'sana': '4',
        'saba' : '36',
        'sadia': '9',
        'shazia' : '7'
        }
for key, value in dict.items():
    print(key + "'s favourite number is " + value)
  ###  x--------------------------------------x
# Exercise # 6.3:
glossory = {'variable': 'place holder',
            'string' :  'set of character',
            'list': 'can store collection of items',
            'tuple': 'immutable ,tuple can not ulter',
            'dictionary':'a key,value pair'
            }
for key, value in glossory.items():
    print(key + " : " + value)

for key, value in glossory.items():
    print(key + " \n " + value)

