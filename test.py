""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

# Python Tutorial


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

"""""""""

1)Variables

"""""""""

name = "Bill"
print(name)

age = 25
print("The age is " + str(age))
print("The age is ", age)

print("Thanks, " + name)  # Concatenation

"""""""""

2)IF ELSE

"""""""""

var = 100

if (var > 10):
    print("Greater than Ten")
    print("Var is Greater than Ten")
else:
    print("Less")

"""""""""

3)IF ELSE Nested

"""""""""

var = 100

if (var % 2 == 0):
    print("Divisible By 2")

    if (var % 5 == 0):
        print("Divisible by 5 Also")
    else:
        print("Not Divisible by 5 Also")
else:
    print("Not Divisible By 2")

"""""""""

4)FOR Nested

"""""""""

for i in range(1, 10):
    print("The number = ", i)

for i in range(1, 10):
    print("The number Format  = ", i)
    i = i + 3

for i in range(1, 10, 2):
    print("The number = ", i)

# for i in range (1,10,3):   for steps of 3!!!
# use break and continue normally


for i in range(1, 10):
    if (i % 3 == 0):
        continue
    print("NEW = ", i)

""""""
# 5)Examples

""""""

for i in range(1, 5):
    print(i, end=" ")
print("\n#################")

for i in range(1, 5):
    for j in range(0, i):
        print(i, end=" ")
    print("")

print("\n#################")
counter = 0
for i in range(1, 5):
    for j in range(0, i):
        counter += 1
        print(counter, end=" ")
    print("")

""""""
# 6)WHILE

""""""

x = 0

while (x < 10):
    x = x + 1
    print(" X = ", x)

num = input("Please enter something")
print("You entered ", num)

num2 = int(num)
print("You entered ", num2 * 2)

print("You entered ", num * 2)  # string multiplied will copy it

print("A", end=" - ")  # for python 2, use:  print("A"),
print("B")

""""""
# 7)LIST

""""""

employees = ["Bill", "Sam", "Bob", 4, "Tom", "John", "Ben"]

print(employees[0])

for i in range(0, len(employees)):
    print("Employee = ", employees[i])

for e in employees:
    print("E=", e)

print("Second Last: " + employees[-2]);
print(employees[2:5]);

""""""
# 8)DICT

""""""

data = {
    "name": "John",
    "designation": "Programmer",
    "city": "Kolkata"
}

print(data["name"])

for key in data:
    print("Key = ", key, " Value = ", data[key])

""""""
# 9)FUNCTION

""""""


def sum(a, b):
    c = a + b
    return c


s = sum(5, 3)
print("The Sum is ", s)


def sayHello():
    print("Hello World!")


sayHello()
sayHello()

""""""
# 10)CLASS

""""""


class Pen:
    name = "Linc"

    # Constructor - Overloading not allowed, only one please
    def __init__(self, n):
        self.name = n

    def sayHello(self):
        print("Hello, I am a ", self.name, " Pen")

    def sayBye(self):
        print("Thanks!")


p = Pen("Parker")

print(p.name)
p.sayHello()






























