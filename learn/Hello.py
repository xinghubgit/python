#"translate_tabs_to_spaces":true
#python only execute the default arguments once when the function was called first time;So we need to do that inside the function


from getpass import getpass
from datetime import datetime
from time import sleep

#as a directory can contain subdirectories and files, a Python package can have sub-packages and modules.
#A directory must contain a file named __init__.py in order for Python to consider it as a package.

condition = True
x = 1 if condition else 0
print(x)

min_num = 1_000_000
max_num = 1_000_000_000
total = min_num + max_num
print(f'{total:,}')


#Unpacking
a, _ = (1, 2)
a, b, *c, d = (1, 2, 3, 4, 5, 6, 7)
# print(a)
# print(b)
# print(c)
# print(d)


class Person:
    pass

person = Person();
first_name = "allen"
second_name = "jin"

first = "first"

person_info = {"allen":"jin", "james":"Gordan", "Elon":"Mask"}
for key,value in person_info.items():
    print(key, value)


setattr(person, first, first_name)
setattr(person, 'last', second_name)

# print(getattr(person, 'first'))
print(person.first)
print(person.last)

def display_time(time=datetime.now()):
    print(time.strftime("%Y/%m/%d %H:%M:%S"))

# def display_time(time=None):
#     if time is None:
#         time = datetime.now()
#     print(time.strftime("%Y/%m/%d %H:%M:%S"))

display_time()
sleep(1)
display_time()
sleep(1)
display_time()



