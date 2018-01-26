# Exercise 8.9:
magicians_names = ['Ali','rizwan','javaid']

def show_magician(list):
    for name in list:
        print(name)


show_magician(magicians_names)

###  -----------------------------------------------------###
# Exercise # 8.10:

magicians_names = ['Ali','rizwan','javaid']

def show_magician(list):
    for name in list:
        print("Before Modifying:" + name)


show_magician(magicians_names)
def make_great(list):
    for name in list:
        print(name + '.. the Great')


make_great(magicians_names)

###  -----------------------------------------------------###
# Exercise # 8.11:
magicians_names = ['Ali','Rizwan','Javaid']

def make_great(list):
    new_list=[]
    for name in list:
        new_list.append( name + '.. The Great')
    return new_list

def show_magician(list):
    for name in list:
        print(name)


print("ORIGINAL LIST:")
show_magician(magicians_names)

print("MODIFIED LIST:")
modified_list = make_great(magicians_names)
show_magician(modified_list)
