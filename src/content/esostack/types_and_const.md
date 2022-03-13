# Types
-----

<br>

## Number
EsoStack only knows one type: **Number**

A stack can hold as many **Numbers** as you want (i.e. as your Computer allows)

This **Numbers** can be added to the stack by simply typing them. They are represented only with 2 decimal places, but internally they are stored with higher precision.

*Examples:*
```
-> 42 420 100
   | 42.00 | 420.00 | 100.00 |

-> 4.2 42.0 123.123
   | 4.20 | 42.00 | 123.12 |
``` 

<br>

## Boolean
In EsoStack even **Booleans** are **Numbers**.

**true** corresponds to **1**

**false** corresponds to **0**

*Examples:*
```
-> true 5 &&
   | 1.00 | 5.00 | -> | 1.00 |

-> false 0 ==
   | 0.00 | 0.00 | -> | 1.00 |

-> true 3 +
   | 1.00 | 3.00 | -> | 4.00 |
```

<br>

## Constants
EsoStack provides some constants to help with calculations.

### Pi
*Tokens:* π, pi

*Value:* 3.1415926536

### Tau
*Tokens:* τ, 2π, tau

*Value:* 6.2831853072

### Phi
*Tokens:* ϕ, phi

*Value:* 1.6180339887

### Euler's Number
*Tokens:* e

*Value:* 2.7182818285