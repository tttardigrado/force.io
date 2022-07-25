# Docs

## Comments

Especially in an esoteric language, comments are a great help in understanding code. Esostack, allows you to write either _Multi line_ or _Single line_ comments using _parentheses ( )_

```
( this is a single line comment )
```

```
( this is a
  multi line comment )
```

## Function documentation

Functions can become complex, but their _inputs_ and _outputs_ have meaning. Documenting our functions makes them as easy to understand at 2am or 5 months from know as they are when they are being written.

```
( Desc: <description of the function>

  Args:
    ( <arg-1-name>: <arg-1-explanation> )
    ( <arg-2-name>: <arg-2-explanation> )
    ( ................................. )

  Returns:
    ( <ret-1-name>: <ret-1-explanation> )
    ( <ret-2-name>: <ret-2-explanation> )
    ( ................................. )
)
```

## Stack Docs

Sometimes the stack operations we are creating are not trivial and we need to show how the stack evolves. For this cases, EsoStack recomends the use of a special kind of documentation: _Stack Docs_:

```
( |...| x | y | (swap)> |...| y | x | )
```

- `|...|`: several not relevant elements
- `| x |`: element represented by `x`
- `---->`: transformation by some operation
- `(op)>`: transformation by the `op` operation
- Branching:
  - `(cond)(T)?`: if the condition is true
  - `(cond)(F)?`: if the condition is false

Examples:

```
( |...| x | y | ----> |...| y-x | )
x y -
```

```
( |...| x | y | (*)> |...| y*x | )
x y *
```

```
( |...| x | y | (==)(T)? |...| 2 |
                (==)(F)? |...| 4 | )
x y == if {
    2
}{
    4
}
```
