# Docs

## Comments
```
( this is a single line comment )
```

```
( this is a 
  multi line comment )
```

## Function documentation
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
```
( |...| x | y | (swap)> |...| y | x | )
```

* `|...|`: several not relevant elements
* `| x |`: element represented by `x`
* `---->`: transformation by some operation
* `(op)>`: transformation by the `op` operation
* Branching:
    * `(cond)(T)?`: if the condition is true
    * `(cond)(F)?`: if the condition is false


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