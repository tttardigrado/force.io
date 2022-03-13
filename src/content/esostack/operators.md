# Operators
-----

<br>

## Arithmetic

### Add
*Descirption:* Sum the top 2 elements

*Args:* 2

*Tokens:* +

*Example:*
```
|...|b|a| -> |...|a + b|
```

<br>

### Subtract
*Descirption:* Subtract the top 2 elements

*Args:* 2

*Example:*
```
|...|b|a| -> |...|a - b|
```

<br>

### Multiply
*Descirption:* Multiply the top 2 elements

*Args:* 2

*Tokens:* *

*Example:*
```
|...|b|a| -> |...|a * b|
```

<br>

### Divide
*Descirption:* Divide the top 2 elements

*Args:* 2

*Tokens:* /

*Example:*
```
|...|b|a| -> |...|a / b|
```

<br>

### Modulus
*Descirption:* Get the rest of the division of the top 2 elements

*Args:* 2

*Tokens:* %

*Example:*
```
|...|b|a| -> |...|a % b|
```

<br>

### Power
*Descirption:* Get the top element to the power of the second

*Args:* 2

*Tokens:* ^

*Example:*
```
|...|b|a| -> |...|a ^ b|
```

<br>

-----

<br>

## Logic

### And
*Descirption:* Logical And with the top 2 elements 

*Args:* 2

*Tokens:* &&, and

*Example:*
```
|...|1|1| -> |...|1|
|...|0|1| -> |...|0|
|...|1|0| -> |...|0|
|...|0|0| -> |...|0|
```

<br>

### Or
*Descirption:* Logical Or with the top 2 elements 

*Args:* 2

*Tokens:* ||, or

*Example:*
```
|...|1|1| -> |...|1|
|...|0|1| -> |...|1|
|...|1|0| -> |...|1|
|...|0|0| -> |...|0|
```

<br>

### Xor
*Descirption:* Logical Exclusive Or with the top 2 elements 

*Args:* 2

*Tokens:* XX, xor

*Example:*
```
|...|1|1| -> |...|0|
|...|0|1| -> |...|1|
|...|1|0| -> |...|1|
|...|0|0| -> |...|0|
```

<br>

### Not
*Descirption:* Logical Negation with the top element 

*Args:* 1

*Tokens:* !!, not

*Example:*
```
|...|1| -> |...|0|
|...|5| -> |...|0|
|...|0| -> |...|1|
```

<br>

-----

<br>

## Comparison

### Lesser
*Descirption:* Check if the top element is < than the second one 

*Args:* 2

*Tokens:* <

*Example:*
```
|...|1|5| -> |...|5 < 1| -> |...|0|
|...|5|1| -> |...|1 < 5| -> |...|1|
|...|5|5| -> |...|5 < 5| -> |...|0|

```

<br>

### Lesser or Equal
*Descirption:* Check if the top element is ≤ than the second one 

*Args:* 2

*Tokens:* <=

*Example:*
```
|...|1|5| -> |...|5 <= 1| -> |...|0|
|...|5|1| -> |...|1 <= 5| -> |...|1|
|...|5|5| -> |...|5 <= 5| -> |...|1|
```

<br>

### Greater
*Descirption:* Check if the top element is > than the second one 

*Args:* 2

*Tokens:* >

*Example:*
```
|...|1|5| -> |...|5 > 1| -> |...|1|
|...|5|1| -> |...|1 > 5| -> |...|0|
|...|5|5| -> |...|5 > 5| -> |...|0|
```

<br>

### Greater or Equal
*Descirption:* Check if the top element is ≥ than the second one 

*Args:* 2

*Tokens:* >=

*Example:*
```
|...|1|5| -> |...|5 >= 1| -> |...|1|
|...|5|1| -> |...|1 >= 5| -> |...|0|
|...|5|5| -> |...|5 >= 5| -> |...|1|
```

<br>

### Equal
*Descirption:* Check if the top 2 elements are equal

*Args:* 2

*Tokens:* ==

*Example:*
```
|...|1|5| -> |...|5 == 1| -> |...|0|
|...|5|5| -> |...|5 == 5| -> |...|1|
```

<br>

### Different
*Descirption:* Check if the top 2 elements are different

*Args:* 2

*Tokens:* !=

*Example:*
```
|...|1|5| -> |...|5 != 1| -> |...|1|
|...|5|5| -> |...|5 != 5| -> |...|0|
```

