#Exercise # 6.7
data_1 = {'first_name' : 'komal','last_name':'zahid','age':'23','city':'karachi'}
data_2 = {'first_name' : 'shazia','last_name':'parveen','age':'23','city':'karachi'}
data_3 = {'first_name' : 'sadia','last_name':'sabtain','age':'22','city':'karachi'}
people = [data_1,data_2,data_3]

for i in people:
    for key, value in i.items():
        print(key + " : " + value)
    print('\n')

###  x--------------------------------------x
# Exercise # 6.8:

buddy = {'owner': 'Zoha' ,"kind": "Percian cat"}
jimmy = {'owner': 'Rida' ,"kind": "dog"}
zigy = {'owner': 'Ali' ,"kind": "fenches"}

Pets = [buddy,jimmy,zigy]
for i in Pets:
    for key, value in i.items():
        print(key + " : " + value)
    print('\n')
###  x--------------------------------------x
# Exercise # 6.9:

favourite_languages = {'Komal':['karachi','kashmir','mury'],
                       'Shazia':['Islamabad','gilit','Lahore'],
                       'Sadia':['Multan','Islamabad','Peshawar']}

for key,value in favourite_languages.items():
         print( key + " favourite places are: ")
         for i in value:
             print(i)

###  x--------------------------------------x
# Exercise # 6.10:
dict = {'komal' : [3,9],
        'sana': [4,7,2],
        'saba' : [36,8,11],
        'sadia': [9],
        'shazia' : [7,66,32]
        }
for dict, numbers in dict.items():
    print(dict + "'s favourite number is ")
    for number in numbers:
        print(number)

###  x--------------------------------------x
# Exercise # 6.11:
cities = {'karachi':{'Country': 'Pakistan','Population' : '20 lacks','Fact': 'Lights of city'},
            'Lahore':{'Country': 'Pakistan','Population' : '9 lacks','Fact': 'Heart of Pakistan'},
            'Islamabad':{'Country': 'Pakistan','Population' : '7 lacks','Fact': 'Capital'}
          }
for city,value in cities.items():
    print(city + ' has the following information :')
    for info,information in value.items():
        print(info + " : " + information)


