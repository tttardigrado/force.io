# Functions
-----

<br>

## Stack

### Swap
*Descirption:* Swap the order of the first 2 elements

*Args:* 2

*Tokens:* swap

*Example:*
```
|...|b|a| -> |...|a|b|
```

<br>

### Dup
*Descirption:* Duplicate the top element

*Args:* 1

*Tokens:* dup

*Example:*
```
|...|b|a| -> |...|b|a|a|
```

<br>

### Dup2
*Descirption:* Duplicate the top 2 elements

*Args:* 2

*Tokens:* dup2

*Example:*
```
|...|b|a| -> |...|b|a|b|a|
```

<br>

### Duplicate
*Descirption:* Duplicate the whole stack

*Args:* 0

*Tokens:* duplicate

*Example:*
```
|c|...|b|a| -> |c|...|b|a|c|...|b|a
```

<br>

### Drop
*Descirption:* Remove the top element

*Args:* 1

*Tokens:* drop

*Example:*
```
|...|b|a| -> |...|b|
```

<br>

### Over
*Descirption:* Copy the second element to the top

*Args:* 2

*Tokens:* over

*Example:*
```
|...|b|a| -> |...|b|a|b|
```

<br>

### Rot
*Descirption:* Rotate the top 3 elements

*Args:* 3

*Tokens:* rot

*Example:*
```
|...|c|b|a| -> |...|b|a|c|
```

<br>

### Size
*Descirption:* Push the size of the stack to itself

*Args:* 0

*Tokens:* size

*Example:*
```
|c|b|a| -> |c|b|a|3|
| |     -> |0|
```

<br>

-----

<br>

## Math

### Square Root
*Descirption:* Get the Square Root of the top element

*Args:* 1

*Error:* x can't be negative

*Tokens:* √x, sqrt

*Example:*
```
|...|a| -> |...|√a|
```

<br>

### Factorial
*Descirption:* Get the factorial of the top element

*Args:* 1

*Tokens:* x!, fact

*Example:*
```
|...|a| -> |...|a!|
```

<br>

### Exponential
*Descirption:* Get the exponential of the top element

*Args:* 1

*Tokens:* exp

*Example:*
```
|...|a| -> |...|exp(a)|
```

<br>

### Natural Logarithm
*Descirption:* Get the Natural Logarithm of the top element

*Args:* 1

*Error:* x can't be 0 or negative

*Tokens:* log

*Example:*
```
|...|a| -> |...|log(a)|
```

<br>

### Sine
*Descirption:* Get the Sine of the top element

*Args:* 1

*Tokens:* sin

*Example:*
```
|...|a| -> |...|sin(a)|
```

<br>

### Cosine
*Descirption:* Get the Cosine of the top element

*Args:* 1

*Tokens:* cos

*Example:*
```
|...|a| -> |...|cos(a)|
```

<br>

### Tangent
*Descirption:* Get the Tangent of the top element

*Args:* 1

*Tokens:* tan

*Example:*
```
|...|a| -> |...|tan(a)|
```

<br>

### Maximum
*Descirption:* Get the Maximum of the top 2 elements

*Args:* 2

*Tokens:* ↑, max

*Example:*
```
|...|b|a| -> |...|max(a,b)|
```

<br>

### Minimum
*Descirption:* Get the Minimum of the top 2 elements

*Args:* 2

*Tokens:* ↓, min

*Example:*
```
|...|b|a| -> |...|min(a,b)|
```

<br>

### Simetric
*Descirption:* Get the Simetric of the top element

*Args:* 1

*Tokens:* -x, sim

*Example:*
```
|...|a| -> |...|-a|
```

<br>

### Floor
*Descirption:* Get the largest integer before the top element

*Args:* 1

*Tokens:* ⌊x⌋, floor

*Example:*
```
|...|a| -> |...|⌊a⌋|
```

<br>

### Ceil
*Descirption:* Get the smallest integer after the top element

*Args:* 1

*Tokens:* ⌈x⌉, ceil

*Example:*
```
|...|a| -> |...|⌈a⌉|
```

<br>

### Absolute Value
*Descirption:* Get the Absolute Value of the top element

*Args:* 1

*Tokens:* |x|, abs

*Example:*
```
|...|a| -> |...| |a| |
```