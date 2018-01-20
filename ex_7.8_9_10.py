#Exercise #7.8:

sandwich_order= ['club sandwich', 'cheese sandwich','vegetable sandwich','yummy sandwich']
finish_sandwiches = []

while sandwich_order :
    order = sandwich_order.pop()
    print("I made your " + order.title())
    finish_sandwiches.append(order)

print('\nYour order is : ')
for finish_sandwich in finish_sandwiches:
    print (finish_sandwich)

###  x--------------------------------------x
# Exercise # 7.9:

sandwich_order= ['club sandwich','Pastrami', 'cheese sandwich','vegetable sandwich','Pastrami','yummy sandwich','Pastrami']
finish_sandwiches = []

print("I'm sorry, we're all out of pastrami today.. \n")
while 'Pastrami' in sandwich_order:
    sandwich_order.remove('Pastrami')

while sandwich_order :
    order = sandwich_order.pop()
    print("I made your " + order.title())
    finish_sandwiches.append(order)

print('\nYour order is : ')
for finish_sandwich in finish_sandwiches:
    print (finish_sandwich)


###  x--------------------------------------x
# Exercise # 7.10:
dream_vacation = {}
active = True
while active:
    name= input('Whats your name?')
    place =input('If you could visit one place in the world, where would you go?')
    dream_vacation[name] = place
    cont = input('Continue? yes/no')

    if cont == 'no':
        active = False

print('======= Results =======')
for name,place in dream_vacation.items():
    print(name + " would visit to " + place)

