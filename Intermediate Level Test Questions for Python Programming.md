Summary of topics: Data Types, Strings, Loops, Functions, Lists, Dictionaries, Classes, File I/O, Exceptions, Modules.

## Intermediate Level Test Questions for Python Programming

### Question 1: Data Types
What is the output of the following code snippet?

```python
a = 5
b = 2.5
c = "Hello World"
d = True

print(type(a), type(b), type(c), type(d))
```

A. `<class 'int'>, <class 'float'>, <class 'str'>, <class 'bool'>`  
B. `<class 'int'>, <class 'str'>, <class 'float'>, <class 'bool'>`  
C. `<class 'float'>, <class 'int'>, <class 'str'>, <class 'bool'>`  
D. `<class 'str'>, <class 'int'>, <class 'float'>, <class 'bool'>`



### Question 2: Strings
What is the output of the following code snippet?

```python
message = "Hello, World!"
print(message[7:12])
```

A. `World`  
B. `World!`  
C. `World!`  
D. `Worl`



### Question 3: Loops
What is the output of the following code snippet?

```python
for i in range(1, 6):
    if i % 2 == 0:
        print(i, end=" ")
```

A. `2 4`  
B. `1 3 5`  
C. `1 2 3 4 5`  
D. `2 4 6 8 10`



### Question 4: Functions
What is the output of the following code snippet?

```python
def multiply(a, b):
    return a * b

print(multiply(3, 4))
```

A. `7`  
B. `10`  
C. `12`  
D. `None`



### Question 5: Lists
What is the output of the following code snippet?

```python
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
print(squares)
```

A. `[1, 4, 9, 16, 25]`  
B. `[1, 3, 5, 7, 9]`  
C. `[2, 4, 6, 8, 10]`  
D. `[0, 1, 4, 9, 16]`



### Question 6: Dictionaries
What is the output of the following code snippet?

```python
my_dict = {"apple": 3, "banana": 2, "orange": 1}
print(my_dict["banana"])
```

A. `1`  
B. `2`  
C. `3`  
D. `KeyError`



### Question 7: Classes
What is the output of the following code snippet?

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

my_car = Car("Honda", "Civic")
print(my_car.make)
```

A. `Honda`  
B. `Civic`  
C. `Honda Civic`  
D. `Car`



### Question 8: File I/O
What is the output of the following code snippet?

```python
with open("example.txt", "w") as f:
    f.write("Hello, World!")

with open("example.txt", "r") as f:
    contents = f.read()

print(contents)
```

A. `Hello, World!`  
B. `World!`  
C. `Hello`  
D. `None`



### Question 9: Exceptions
What is the output of the following code snippet?

```python
try:
    print(1 / 0)
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Done")
```

A. `Cannot divide by zero`  
B. `Done`  
C. `Cannot divide by zero Done`  
D. `ZeroDivisionError`



### Question 10: Modules
What is the output of the following code snippet?

```python
import math

print(math.sqrt(16))
```

A. `2`  
B. `4`  
C. `8`  
D. `16`



