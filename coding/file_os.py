import os
#The best way to close a file is by using the with statement. This ensures that the file is closed when the block inside the with statement is exited.
input = "D:\\github\\product.csv"
# with open(input, mode='r', encoding="utf-8") as f:
#     f.read()

output = "D:\\github\\output.txt"
# with open(output, mode='w', encoding='utf-8') as f:
#     f.write("First line\n")
#     # f.newlines
#     f.write("Second line\n")
#     f.write("End\n")

with open(input, mode='r', encoding="utf-8") as f:
    for line in f:
        print(line, end='')

# f = open(output, 'r', encoding='utf-8')
# f.read()
# f.tell()
# f.seek(0)

#A file can be removed (deleted) using the remove() method.
#Similarly, the rmdir() method removes an empty directory.

print(os.getcwd())
os.chdir('D:\\github\\python')
print(os.listdir())

#There are plenty of built-in exceptions in Python that are raised when corresponding errors occur. We can view all the built-in exceptions using the built-in local() function as follows:
#When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.
print(dir(locals()['__builtins__']))


#Here, we have created a user-defined exception called CustomError which inherits from the Exception class. This new exception, like other exceptions, can be raised using the raise statement with an optional error message.
class SalaryNotInRangeError(Exception):
    """Exception raised for errors in the input salary.

    Attributes:
        salary -- input salary which caused the error
        message -- explanation of the error
    """

    def __init__(self, salary, message="Salary is not in (5000, 15000) range"):
        self.salary = salary
        self.message = message
        super().__init__(self.message)


salary = int(input("Enter salary amount: "))
if not 5000 < salary < 15000:
    raise SalaryNotInRangeError(salary)


