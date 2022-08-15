# If True

**If True** is a Command line interface (CLI) for building Logic tables from a given logic expression.

- [GitHub](https://github.com/Force4760/IfTrue)

## Stack
* Languages: Nim
* Libraries: Cligen

## Example
```sh
$ ./iftrue
  Logic Expression: A -> (B v ~A)
  | A | B | ~A | (B v ~A) | (A -> (B v ~A)) |
  |---|---|----|----------|-----------------|
  | T | T | F  |    T     |        T        |
  | T | F | F  |    F     |        F        |
  | F | T | T  |    T     |        T        |
  | F | F | T  |    T     |        T        |
```

## Syntax
- and: &&, ^
- or: ||, v
- nand: ~^, /
- nor: ~v, \
- implication: >, ->
- converse: <, <-
- iff: ==, <->
- xor: !=, x
- not: !, ~
- variables: A, B, ..., Z
- grouping: ()

## Output
The output format can be specified with the *-o* argument and can be in the form of:
- `md`: MarkDown
- `json`: JSON (JavaScript Object Notation)
- `csv`: CSV (Comma Separated Value)
- `html`: HTML (HyperText Markup Language)