#Exercise # 6.4:
glossory = {'variable': 'place holder',
            'string' :  'set of character',
            'list': 'can store collection of items',
            'tuple': 'immutable ,tuple can not ulter',
            'dictionary':'a key,value pair'
            }
glossory['function'] = 'set of instructions'
glossory['naming convention'] = 'setting names'
glossory['sort'] = 'order by ascending or descending'
glossory['move'] = 'delete from one place then copy to another place'
glossory['loop'] = 'iterations'

for key, value in glossory.items():
    print(key + " : " + value)

###  x--------------------------------------x
# Exercise # 6.5:
rivers = {'sindh':'sindh river',
          'Punjab': 'chanab river',
          'Punjab': 'jehlum river',
          'kashmir':'neelum river'}
for key, value in rivers.items():
    print(value + " runs through  " + key)
for key in rivers.keys():
    print("Province :   " + key)
for value in rivers.values():
    print(" River : " + value)

 ###  x--------------------------------------x
# Exercise # 6.6:

favorite_languages = {
                        'jen': 'python',
                        'sarah': 'c',
                        'edward': 'ruby',
                        'phil': 'python',
                     }
people = ['john','james','sarah','henry','phil']

for i in people:
    if i in favorite_languages.keys():
        print("Thank you for your responce")
    else:
        print("Hey.. we are inviting you to take the poll.")

