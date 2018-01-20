# Exercise # 7.1:
car = input('what kind of rental car you would like?')
print('Let me see if I can find you a' + car)

###  x--------------------------------------x
# Exercise # 7.2:

no_of_people = input('how many people are in your dinner group?')
if int(no_of_people )>= 8:
    print('You’ll have to wait for a table')
else:
    print('your table is ready')

###  x--------------------------------------x
# Exercise # 7.3:
num = input("Enter a number, i'll tell you it's multiple of 10 or not?")
if int(num) % 10 == 0:
    print('Yes, it is multiple of 10')
else:
    print('No, it is not a multiple of 10')
