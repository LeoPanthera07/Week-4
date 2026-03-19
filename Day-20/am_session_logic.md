# Day 20 AM – Logic and Explanations

## Part A

### 1. Maximum, minimum, and frequency
- Maximum and minimum are found by scanning the list once and updating the current best values.
- Frequency counting uses a dictionary where each element becomes a key and its count is updated manually.

### 2. While loop problems
- Reversing a number is done by repeatedly taking the last digit using `% 10` and building the reversed number.
- A palindrome number is one that remains the same after reversal.

### 3. Tuples and dictionaries
- A list of tuples like `[("a", 10), ("b", 25)]` can be converted into a dictionary by looping through each pair and assigning `result[key] = value`.
- The key with the highest value is found by tracking the current best key while iterating over the dictionary.

### 4. `*args`
- `*args` collects multiple positional arguments into a tuple.
- Sum and average are computed manually using a loop, without `sum()`.

### 5. `**kwargs`
- `**kwargs` collects named arguments into a dictionary.
- The student with the highest marks is found by iterating through the dictionary and tracking the maximum.

## Part B

### Custom `Vector` class
- `__add__` performs element-wise vector addition.
- `__sub__` performs element-wise vector subtraction.
- `__mul__` performs scalar multiplication.
- `__repr__` provides readable output such as `Vector(1, 2, 3)` style display.

This shows operator overloading, where Python operators work with custom objects.

## Part C

### Q1. `*args` vs `**kwargs`
- `*args` is used when the number of positional arguments is unknown.
- `**kwargs` is used when named arguments are needed and the names may vary.

### Q2. `Student` class
- The class stores `name` and `marks`.
- Grade logic:
  - A for marks >= 80
  - B for marks >= 60
  - C otherwise
- `__str__` makes object printing readable.

### Q3. Dunder methods
Dunder methods are special methods with double underscores that define built-in behavior for objects.

Examples:
- `__init__` → object creation
- `__str__` / `__repr__` → object display
- `__add__` → behavior of `+`

They are important because they make custom classes behave like built-in Python objects.

## Part D

### AI evaluation
- The AI explanation is correct because it identifies real dunder methods such as `__init__`, `__str__`, and `__add__`.
- The sample custom class is logically correct and runnable.
- A stronger answer would include more examples of operator overloading and explain when each dunder method is triggered.

## Implementation notes
- Keep the script simple and executable in one run.
- Save this code as `AM_Session.py`.
- Save this explanation file as `AM_Session_Logic.md`.
- Push both files to your GitHub repo and submit the repo link on LMS.

https://github.com/LeoPanthera07/Week-4/tree/60814909838cc380d65bbc89e0517ae74cac40c6/Day-20