#Furthermore, temperature was replaced with _temperature. An underscore _ at the beginning is used to denote private variables in Python.
import re
import datetime
import pytz
import threading

class Celsius:
    def __init__(self, temperature = 0):
        self._temperature = temperature

    def get_temperature(self):
        return self._temperature

    def set_temperature(self, value):
        if value < -273.15:
            raise ValueError("Temperature below 273.15 is impossible.")
        self._temperature = value

    def to_fahrenheit(self):
        return (self.get_temperature() * 1.8) + 32

human = Celsius(37)
print(human.get_temperature())
print(human.to_fahrenheit())


pattern = '^a...s$'
test_string = 'abcds'

result = re.match(pattern, test_string)
if result:
    print("match ...")
else:
    print("Not Mach...")


print(datetime.datetime.now())
for i in dir(datetime):
    print(i)

new_york = pytz.timezone('America/New_York')
london = pytz.timezone('Europe/London')
print(datetime.datetime.now(new_york))
print(datetime.datetime.now(london))

now = datetime.datetime.timestamp(datetime.datetime.now())
print(datetime.datetime.fromtimestamp(now))

def print_hello_tree_times():
    for i in range(3):
        print("Hello")

def print_hi_tree_times():
    for i in range(3):
        print("Hi")

# https://stackoverflow.com/questions/2846653/how-can-i-use-threading-in-python
t1 = threading.Thread(target=print_hello_tree_times())
t2 = threading.Thread(target=print_hi_tree_times())
t1.start()
t2.start()
