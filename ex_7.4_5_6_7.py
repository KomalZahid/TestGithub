#Exercise # 7.4

prompt = ('enter a series of pizza toppings')
prompt += ("\n Enter 'quit' when you finish")
toppings = ''


active = True
while active:
    toppings = input(prompt)
    if toppings == 'quit':
        active = False
    else:
        print('We will add ' + toppings + ' to your pizza.')

###  x--------------------------------------x
# Exercise # 7.5:
prompt = ('What is your age?')
prompt += ("\n Enter 'quit' when you finish")

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    elif int(age) <=3 :
        print('Your ticket is free of cost')
    elif int(age) >=3 and int(age) <=12:
        print('Your Ticket price is 10$')
    else:
        print('Your Ticket price is 15$')

###  x--------------------------------------x
# Exercise # 7.6:
#version 1
prompt = ('enter a series of pizza toppings')
prompt += ("\n Enter 'quit' when you finish")
toppings = ''
while toppings != 'quit':
    toppings = input(prompt)
    if toppings != 'quit':
        print('We will add ' + toppings + ' to your pizza.')

#version 2:
prompt = ('enter a series of pizza toppings')
prompt += ("\n Enter 'quit' when you finish")
toppings = ''


active = True
while active:
    toppings = input(prompt)
    if toppings == 'quit':
        active = False
    else:
        print('We will add ' + toppings + ' to your pizza.')


#version 3:
prompt = ('enter a series of pizza toppings')
prompt += ("\n Enter 'quit' when you finish")
toppings = ''

while True:
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print('We will add ' + toppings + ' to your pizza.')
###  x--------------------------------------x
# Exercise # 7.7:

x = 1
while x<5:
    print('hello world')
