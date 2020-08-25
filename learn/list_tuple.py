#List comprehension is an elegant and concise way to create a new list from an existing list in Python.
#A tuple in Python is similar to a list. The difference between the two is that we cannot change the elements of a tuple once it is assigned whereas we can change the elements of a list.

names = ["james", "wade", "allen", "Jordan", "Naluto", "Elon", "Bezos"]
# for index, name in enumerate(names):
#     print(name + " at " + f"{index}")


locations = ["USA", "China", "SH", "England", "France", "Japan"]

# for location, name in zip(locations, names):
#     print(name + " in " + location)

# for value in zip(locations, names):
#     print(value)


num_arr = [1, 2, 3, 4]

print(list(filter(lambda x: x %2 == 0, num_arr)))
print(list(map(lambda x: x ** 2, num_arr)))


def recursion(num):
    if num == 1:
        return 1
    else:
        return recursion(num-1) * num

print(recursion(5))

squ = lambda x : x ** 2
print(squ(5))


list_comprehension = [x+y for x in ['Python ','C '] for y in ['Language','Programming']]
print(list_comprehension)


#A tuple can also be created without using parentheses. This is known as tuple packing.
#Having one element within parentheses is not enough. We will need a trailing comma to indicate that it is, in fact, a tuple.


# nested index
n_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(n_tuple[0][3])       # 's'
print(n_tuple[1][1])       # 4

my_tuple = 3, 4.6, "dog"
print(my_tuple)

my_tuple = ("hello")
my_tuple2 = ("hello",)
print(type(my_tuple))
print(type(my_tuple2))

#Tuple Advantages
#We generally use tuples for heterogeneous (different) data types and lists for homogeneous (similar) data types.
#Since tuples are immutable, iterating through a tuple is faster than with list. So there is a slight performance boost.
#Tuples that contain immutable elements can be used as a key for a dictionary. With lists, this is not possible.
#If you have data that doesn't change, implementing it as tuple will guarantee that it remains write-protected.

