from math import isclose

def find_max_min(data):
    maximum = data[0]
    minimum = data[0]
    for x in data:
        if x > maximum:
            maximum = x
        if x < minimum:
            minimum = x
    return maximum, minimum

def frequency_count(data):
    freq = {}
    for x in data:
        if x in freq:
            freq[x] += 1
        else:
            freq[x] = 1
    return freq

def reverse_number(n):
    num = n
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num //= 10
    return rev

def is_palindrome_number(n):
    return n == reverse_number(n)

def tuples_to_dict(pairs):
    result = {}
    for item in pairs:
        key = item[0]
        value = item[1]
        result[key] = value
    return result

def max_value_key(data):
    keys = list(data.keys())
    best_key = keys[0]
    best_value = data[best_key]
    for key in data:
        if data[key] > best_value:
            best_value = data[key]
            best_key = key
    return best_key

def sum_and_average(*args):
    total = 0
    count = 0
    for x in args:
        total += x
        count += 1
    avg = total / count if count > 0 else 0
    return total, avg

def top_student(**kwargs):
    names = list(kwargs.keys())
    best_name = names[0]
    best_marks = kwargs[best_name]
    for name in kwargs:
        if kwargs[name] > best_marks:
            best_marks = kwargs[name]
            best_name = name
    return best_name, best_marks

class Vector:
    def __init__(self, values):
        self.values = values

    def __add__(self, other):
        result = []
        i = 0
        while i < len(self.values):
            result.append(self.values[i] + other.values[i])
            i += 1
        return Vector(tuple(result))

    def __sub__(self, other):
        result = []
        i = 0
        while i < len(self.values):
            result.append(self.values[i] - other.values[i])
            i += 1
        return Vector(tuple(result))

    def __mul__(self, scalar):
        result = []
        i = 0
        while i < len(self.values):
            result.append(self.values[i] * scalar)
            i += 1
        return Vector(tuple(result))

    def __repr__(self):
        return f"Vector{self.values}"

class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def calculate_grade(self):
        if self.marks >= 80:
            return "A"
        elif self.marks >= 60:
            return "B"
        else:
            return "C"

    def __str__(self):
        return f"Student(name={self.name}, marks={self.marks}, grade={self.calculate_grade()})"

sample_list = [4, 2, 9, 4, 7, 2, 1, 9, 9]
max_val, min_val = find_max_min(sample_list)
freq = frequency_count(sample_list)

print("Part A")
print("Max:", max_val)
print("Min:", min_val)
print("Frequency:", freq)

number = 12321
print("Reverse:", reverse_number(number))
print("Palindrome:", is_palindrome_number(number))

pairs = [("a", 10), ("b", 25), ("c", 18)]
pair_dict = tuples_to_dict(pairs)
print("Tuple to dict:", pair_dict)
print("Highest value key:", max_value_key(pair_dict))

total, avg = sum_and_average(10, 20, 30, 40, 50)
print("Sum and average:", total, avg)

best_name, best_marks = top_student(Aman=72, Riya=91, Kunal=85, Sneha=88)
print("Top student:", best_name, best_marks)

print("\nPart B")
v1 = Vector((1, 2, 3))
v2 = Vector((4, 5, 6))
print("v1:", v1)
print("v2:", v2)
print("v1 + v2:", v1 + v2)
print("v2 - v1:", v2 - v1)
print("v1 * 3:", v1 * 3)

print("\nPart C")
student = Student("Riya", 84)
print(student)
print("Grade:", student.calculate_grade())

print("\nQ1")
print("*args collects positional arguments into a tuple.")
print("**kwargs collects keyword arguments into a dictionary.")

print("\nQ3")
print("__init__ initializes objects.")
print("__repr__ gives readable object representation.")
print("__add__ defines behavior for + operator.")

print("\nPart D")
prompt = "Explain Python dunder methods with examples for beginners and include a custom class implementation."
ai_output = """
Dunder methods are special Python methods with double underscores.
Examples:
- __init__ for object initialization
- __str__ for readable printing
- __add__ for operator overloading

class Book:
    def __init__(self, title):
        self.title = title
    def __str__(self):
        return self.title
"""
print("Prompt:", prompt)
print("AI Output:", ai_output)
print("Evaluation:")
print("Examples are correct.")
print("The class implementation works for initialization and string display.")
print("It would be better if the AI also showed arithmetic-style dunder methods like __add__.")
