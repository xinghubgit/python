print("Hello python")
arr = [1, 2,3]
s = {1, 2, 3, 3, 4}
'''
for i in arr:
	print((i + 5)%3)
'''
print(s)

for i in range(3, 12, 4):
	if (i == 11):
		break
	print(i + 1.5)
else:
	print("Start 3 End 12 Done")

print(list(range(3)))
print(len(s))


for string in 'Hello':
	print(string)


def first_function(name):
	print("Hello Function " + name)

first_function('A')


def factorial(x):
	if x == 1:
		return 1
	else:
		return x * factorial(x - 1)

num = 5
print("The factorial of ", num, " is ", factorial(num))




