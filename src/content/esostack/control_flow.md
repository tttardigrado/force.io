# Control Flow
-----

<br>

# If
*Syntax:* 
```
if{ (then-block) }{ (else-block) }
```

The **If** statement allows you to execute conditional blocks of code. It checks (and drops) the top element of the stack.

If that element is **true**, the **then-block** is executed.

If that element is **false**, the **else-block** is executed.

<br>

# For
*Syntax:* 
```
for{ (body-block) }
```

The **For** statement allows you to execute the same block of code multiple times. It drops the top element of the stack and executes the **body-block** that number of times.

<br>

# User Functions

The main file isn't an EsoStack file. The main file works as a sequence of functions to be executed.

```
test1

fun2

func3
```

As an example, this file would be interpreted in the following way:
* Initialize a stack (always happens at the beggining)
* Try to run the *test1* function
* Blank lines are ignored
* Try to run the *fun2* function
* Blank lines are ignored
* Try to run the *func3* function

If an error occurs or a function is not found inside the *funcs* folder, the program will halt