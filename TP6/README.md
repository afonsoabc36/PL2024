# TP6: Gramática Independente de Contexto (GIC)

Gramática para um programa na seguinte linguagem de programação:

```
? a
b = a * 2 / (27 - 3)
! a + b
c = a * b / (a / b)
```

## Gramática

**Gramática = (T,N,S,P)**

**T** (*Símbolos Terminais*) -> { '**?**', **id**, '**=**', '__*__', **num**, '**/**', '**(**', '**-**', '**)**', '**!**', '**+**' }

**N** (*Símbolos Não Terminais*) -> { **S**, **Input**, **Output**, **Assign**, **Expression**, **Operation**, **Operation2** }

**S** (*Starting Simbol* ou *Axioma*) -> **S**

**P** (*Production Rules*) ↓ 

```
S ->  '?' id
    | '!' Expression
    | id '=' Expression
LA(S) = {'?', '!', id}

Expression -> Operation Operation2
LA(Expression) = {id, num, '('}

Operation -> id
            | num
            | '(' Expression ')'
La(Operation) = {id, num, '('}

Operation2 -> '+' Expression
            | '-' Expression
            | '*' Expression
            | '/' Expression
            | ε
LA(Operation2) = {'+', '-', '*', '/', ε}
```
