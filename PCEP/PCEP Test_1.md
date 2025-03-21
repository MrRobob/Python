# PCEP Test

Below is an **Advanced PCEP‑30‑02 Practice Test** modeled after real‐exam challenges. This test features detailed, branching questions—many of which require careful code‑reading and may have multiple correct answers. Some questions ask you to “select all that apply,” while others expect a single choice. Read each question carefully, work through the code in your head (or on paper), and then record your answers (for example, “1: A,C; 2: A; 3: D; …”). When you’re ready, share your answers and we’ll review them together.

---

> **Note:** You have 40 minutes to complete this test. Good luck—focus on the nuances of Python’s fundamentals, control flow, data collections, and functions/exceptions.

---

## Section 1 – Fundamentals, Literals, Variables, and Operators

**Question 1 (Multiple Answers Possible):**  
Consider the following code:

```python
def greet():
    print("Hello")
     print("World")
greet()
```

Which statements about the error (if any) are correct? *(Select all that apply)*

- **A.** An `IndentationError` is raised because the second `print` is misaligned.
- **B.** A `SyntaxError` is raised due to an unexpected indent.
- **C.** The error occurs at compile‑time, not at runtime.
- **D.** No error is raised because Python automatically adjusts indentation.

---

**Question 2 (Multiple Answers Possible):**  
Which of the following statements correctly describe the roles of lexical analysis, syntax, and semantics in Python? *(Select all that apply)*

- **A.** Lexical analysis breaks the source code into tokens.
- **B.** Syntax defines the rules for structuring tokens into valid statements.
- **C.** Semantics determines the meaning and runtime behavior of the code.
- **D.** Lexical analysis and syntax refer to the same process.

---

**Question 3 (Multiple Answers Possible):**  
Which statements accurately describe how the Python interpreter works? *(Select all that apply)*

- **A.** The interpreter reads and executes code line by line.
- **B.** It performs both lexical and syntactic analyses before executing code.
- **C.** It compiles the entire code directly into machine code before execution.
- **D.** It converts Python source code into bytecode, which is then executed.

---

**Question 4:**  
Examine the following I/O code:

```python
print("A", "B", sep="-", end="*")
print("C")
```

What is the output displayed on the console?

- **A.** A-B*C
- **B.** A-B C
- **C.** A-B*C*
- **D.** A B C

---

**Question 5 (Multiple Answers Possible):**  
Consider this code that uses different numeral systems:

```python
a = 0b101
b = 0x1F
c = 0o17
print(a, b, c)
```

Which of the following correctly describes the printed output? *(Select all that apply)*

- **A.** 5 31 15
- **B.** 5 16 15
- **C.** 101 1F 17
- **D.** 5 31 17

---

**Question 6:**  
Which of the following variable names BEST follows PEP‑8 recommendations for naming ordinary (non‑class) variables?

- **A.** `my_variable`
- **B.** `MyVariable`
- **C.** `myVariable`
- **D.** `my-variable`

---

**Question 7 (Multiple Answers Possible):**  
Analyze the code below:

```python
x = 7 / 2
y = 7 // 2
print(x, y, type(x), type(y))
```

Which of the following statements are true? *(Select all that apply)*

- **A.** `x` evaluates to 3.5 and `y` evaluates to 3.
- **B.** The type of `x` is `<class 'float'>`.
- **C.** The type of `y` is `<class 'int'>`.
- **D.** The `/` operator always returns a float—even if the result is mathematically whole.

---

**Question 8:**  
What is the output of the following type‑casting code?

```python
a = "100"
b = int(a)
c = float(a)
print(b + 50, c + 0.5)
```

- **A.** 150 and 100.5
- **B.** 10050 and 1000.5
- **C.** 150 and 100.0
- **D.** Runtime error converting the string

---

**Question 9:**  
Determine the value printed by this compound assignment code:

```python
x = 5
x += 3
x *= 2
print(x)
```

- **A.** 16  
- **B.** 13  
- **C.** 20  
- **D.** 10

---

**Question 10 (Multiple Answers Possible):**  
Review the bitwise operations in the following snippet:

```python
a = 10  # binary: 1010
b = 4   # binary: 0100
print(a & b, a | b, a ^ b, ~a)
```

Which of the following assertions are true? *(Select all that apply)*

- **A.** `a & b` equals 0.
- **B.** `a | b` equals 14.
- **C.** `a ^ b` equals 14.
- **D.** `~a` equals -11.

---

**Question 11:**  
What does the following Boolean expression print?

```python
print(True and False or True)
```

- **A.** True  
- **B.** False  
- **C.** Error  
- **D.** Undefined due to operator precedence

---

**Question 12 (Multiple Answers Possible):**  
Consider this I/O and conversion code:

```python
a = input("Enter a number: ")
print("Result:", int(a) * 2)
```

Which of these statements about the code are correct? *(Select all that apply)*

- **A.** The `input()` function always returns a string.
- **B.** The `int()` function converts the user’s input from a string to an integer.
- **C.** If the user enters `"5"`, the code prints: `Result: 10`.
- **D.** The prompt `"Enter a number:"` is displayed on the console.

---

## Section 2 – Control Flow: Conditionals and Loops

**Question 13:**  
Examine the following conditional code:

```python
x = 2
if x > 3:
    print("A")
elif x == 2:
    print("B")
elif x < 5:
    print("C")
else:
    print("D")
```

What is printed?

- **A.** A  
- **B.** B  
- **C.** C  
- **D.** D

---

**Question 14:**  
Review this nested conditional:

```python
x = 3
if x > 0:
    if x % 2 == 0:
        print("Even")
    else:
        print("Odd")
else:
    print("Non‑positive")
```

Which of the following statements are true?  

- **A.** For `x = 3`, it prints “Odd”.
- **B.** For `x = 2`, it would print “Even”.
- **C.** For `x = 0`, it would print “Non‑positive”.
- **D.** All of the above.

---

**Question 15:**  
Consider the code with a for‑loop and an `else` clause:

```python
for i in range(3):
    if i == 2:
        break
    print(i, end=" ")
else:
    print("Done")
```

What does this code print?

- **A.** 0 1 Done  
- **B.** 0 1  
- **C.** 0 1 2  
- **D.** Done

---

**Question 16:**  
What is the output of the following while‑loop featuring `continue`?

```python
x = 0
while x < 5:
    x += 1
    if x % 2 == 0:
        continue
    print(x, end=" ")
```

- **A.** 1 3 5  
- **B.** 1 2 3 5  
- **C.** 2 4  
- **D.** 1 3

---

**Question 17:**  
Analyze the behavior of this while‑loop with an `else` clause:

```python
i = 0
while i < 3:
    print(i, end=" ")
    i += 1
else:
    print("Finished")
```

What does it print?

- **A.** 0 1 2 Finished  
- **B.** 0 1 2  
- **C.** Finished  
- **D.** 0 1 2 None

---

**Question 18:**  
Determine the output of this nested loop:

```python
for i in range(2):
    for j in range(2):
        if i == j:
            print("X", end="")
        else:
            print("O", end="")
    print()
```

Which output matches the printed result?

- **A.**  

  ```python
  XO
  OX
  ```

- **B.**  

  ```python
  OX
  XO
  ```

- **C.**  

  ```python
  XX
  OO
  ```

- **D.**  

  ```python
  XO XO
  ```

---

## Section 3 – Data Collections: Lists, Tuples, Dictionaries, and Strings

**Question 19:**  
What is the result of this list slicing?

```python
lst = [0, 1, 2, 3, 4, 5]
result = lst[1:-1]
print(result)
```

- **A.** [1, 2, 3, 4]  
- **B.** [1, 2, 3, 4, 5]  
- **C.** [0, 1, 2, 3, 4]  
- **D.** [1, 2, 3]

---

**Question 20:**  
Examine the following list‐modification code:

```python
ls = [3, 1, 2]
ls.insert(1, 9)
ls.append(0)
print(ls)
```

What is printed?

- **A.** [3, 9, 1, 2, 0]  
- **B.** [9, 3, 1, 2, 0]  
- **C.** [3, 9, 1, 2]  
- **D.** [9, 1, 2, 0]

---

**Question 21:**  
Consider the following list comprehension that constructs a “matrix”:

```python
matrix = [[j for j in range(3)] for i in range(2)]
print(matrix)
```

What is the output?

- **A.** [[0, 1, 2], [0, 1, 2]]  
- **B.** [[0, 1], [0, 1], [0, 1]]  
- **C.** [[0, 1, 2], [1, 2, 3]]  
- **D.** [[0, 1, 2, 3]]

---

**Question 22:**  
Evaluate the following tuple (and mutability) example:

```python
t = (1, 2, [3, 4])
t[2].append(5)
print(t)
```

What is printed?

- **A.** (1, 2, [3, 4, 5])
- **B.** Error because tuples cannot be modified.
- **C.** (1, 2, [3, 4])
- **D.** ([1, 2, 3, 4, 5])

---

**Question 23:**  
Analyze this dictionary manipulation:

```python
d = {"a": 1, "b": 2}
d["c"] = d["a"] + d.get("b")
print(sorted(d.items()))
```

What is the output?

- **A.** [('a', 1), ('b', 2), ('c', 3)]
- **B.** [('c', 3), ('b', 2), ('a', 1)]
- **C.** {'a': 1, 'b': 2, 'c': 3}
- **D.** An error occurs because dictionaries are unordered.

---

**Question 24:**  
What does the following string (with escapes) print?

```python
s = "It\'s a \"test\".\nNew line"
print(s)
```

- **A.**  
  
  ```python
  It's a "test".
  New line
  ```

- **B.** It\'s a \"test\". \nNew line  
- **C.** It's a "test". New line (all in one line)  
- **D.** Error

---

**Question 25:**  
Given the multi‑line string code:

```python
s = """Line1
Line2
Line3"""
print(s.splitlines())
```

What is printed?

- **A.** ['Line1', 'Line2', 'Line3']
- **B.** "Line1Line2Line3"
- **C.** ['Line1\n', 'Line2\n', 'Line3']
- **D.** Error

---

## Section 4 – Functions and Exceptions

**Question 26:**  
Consider this function with a default parameter:

```python
def subtract(a, b=5):
    return a - b

print(subtract(10))
print(subtract(b=3, a=10))
```

Which of the following describes the printed output?

- **A.** 5 on the first line and 7 on the second line.
- **B.** 7 on the first line and 5 on the second line.
- **C.** Both calls print the same value.
- **D.** The code raises an error due to keyword argument ordering.

---

**Question 27:**  
Review the following code on scopes and shadowing:

```python
x = 10
def foo():
    x = 5
    def bar():
        print(x)
    bar()
foo()
print(x)
```

Which output is produced?

- **A.** 5 then 10 (first from `bar()`, then the global `x`)
- **B.** 10 then 5
- **C.** 5 then 5
- **D.** 10 then 10

---

**Question 28:**  
Determine what the recursive function prints:

```python
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(4))
```

- **A.** 24  
- **B.** 4  
- **C.** 16  
- **D.** It raises a recursion error.

---

**Question 29:**  
Evaluate the exception handling in this snippet:

```python
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError:
    print("Index error")
except Exception:
    print("General error")
```

What is printed?

- **A.** Index error  
- **B.** General error  
- **C.** No output (silent failure)  
- **D.** A traceback is printed

---

**Question 30:**  
Consider the following code on exception propagation:

```python
def inner():
    raise ValueError("Invalid value")

def outer():
    try:
        inner()
    except TypeError:
        print("Type error")
    # No handling for ValueError here

outer()
```

What happens when `outer()` is called?

- **A.** The program prints nothing and then terminates with a `ValueError`.
- **B.** It prints "Type error".
- **C.** It prints "Invalid value".
- **D.** The exception is caught and a generic error message is printed.

---

When you’re ready, please provide your answers (e.g., “1: A,B; 2: A,B,C; 3: A,D; …”) and we’ll review each one together. Good luck!
