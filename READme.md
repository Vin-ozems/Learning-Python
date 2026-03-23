# 🐍 Python Beginner Challenges

A structured collection of Python exercises organized by topic — from basic input/output all the way to advanced built-in functions and mini projects.

---

## 📁 File

`python_challenges.py`

---

## 📚 Sections Overview

| # | Section | Topics Covered |
|---|---------|---------------|
| 1 | Beginner Basics | Variables, input/output, strings, type conversion, indexing, swapping |
| 2 | Control Flow | `if`, `elif`, `else` conditionals |
| 3 | Loops | `for` loops, `range()`, accumulation |
| 4 | Data Structures | Lists, iteration |
| 5 | Functions | `def`, `*args`, `return`, string methods |
| 6 | Mini Projects | Calculator, Info Formatter, Temperature Converter |
| 7 | Built-in Functions | `enumerate`, `reversed`, `zip`, `map`, `filter`, `lambda` |
| 8 | Bonus Challenge | Combining all built-in functions |

---

## 🔍 Section Breakdown

### Section 1 — Beginner Basics
Covers the foundations of Python:
- Greeting a user by name and age
- Arithmetic with two numbers (BODMAS order)
- Calculating age from birth year
- Converting string case (`upper`, `lower`)
- Swapping two variables in one step
- Building a full name from first and last name
- Accessing characters in a string using indexing

### Section 2 — Control Flow
- **Even or Odd Checker** — uses `%` (modulus) to determine parity
- **Grade Calculator** — assigns letter grades using `if/elif/else` chains

### Section 3 — Loops
- Print only even numbers from 1 to 50
- Double each number from 1 to 50
- Print the 7 times multiplication table

### Section 4 — Data Structures
- Iterate over a list of fruits and print in lowercase
- Sum numbers from 1 to 10 using accumulation

### Section 5 — Functions
- `text_clean(fname, lname)` — strips and lowercases two name inputs
- `total(*args)` — sums any number of arguments using `*args`
- `text_clean_single(fname)` — demonstrates a common bug: returning `None` when `return` is commented out

### Section 6 — Mini Projects
Three complete programs combining all skills above:

- **Personal Info Formatter** — collects name, age, and country, then prints a formatted profile
- **Simple Calculator** — supports add, subtract, divide, multiply using a menu-driven interface
- **Temperature Converter** — converts Celsius ↔ Fahrenheit using nested functions

### Section 7 — Built-in Functions
Ten practical tasks using Python's powerful built-in tools:

| Task | Built-in Used |
|------|--------------|
| Student Position Tracker | `enumerate()` |
| Countdown System | `reversed()` |
| Product & Price Pairing | `zip()` |
| Convert Names to Uppercase | `map()` + `lambda` |
| Extract Passing Scores | `filter()` + `lambda` |
| Add Bonus to Salaries | `map()` + `lambda` |
| Filter Even Numbers | `filter()` + `lambda` |
| Rank Players by Score | `zip()` + `enumerate()` |
| Reverse & Index Names | `reversed()` + `enumerate()` |
| Filter & Transform Products | `filter()` + `map()` + `lambda` |

### Section 8 — Bonus Challenge
Combines `zip()`, `filter()`, `enumerate()`, and `lambda` in a single expression to print only passing students (score ≥ 50) with numbering.

---

## ▶️ How to Run

Make sure you have Python 3 installed, then run:

```bash
python python_challenges.py
```

> **Note:** Many sections use `input()`, so the program will pause and wait for you to type values in the terminal.

---

## 🛠️ Requirements

- Python 3.x
- No external libraries needed — uses only Python built-ins

---

## 💡 Key Concepts Quick Reference

```python
# enumerate — adds index to iteration
for i, item in enumerate(list, start=1): ...

# zip — pairs two lists together
for a, b in zip(list1, list2): ...

# reversed — iterates in reverse order
for item in reversed(list): ...

# map + lambda — transform every item in a list
result = list(map(lambda x: x * 2, numbers))

# filter + lambda — keep only items that match a condition
result = list(filter(lambda x: x > 50, scores))
```

---

## 📝 Notes

- Variable names follow Python convention (`snake_case`)
- All functions use `return` for reusability (except where noted)
- Comments are included throughout to explain each step