# TP4: Analisador Léxico

## Compilar:
```
python3 analisadorLexico.py
```

## Objetivo:
Construir um analisador léxico para uma liguagem de query com a qual se podem escrever frases do género:
`Select id, nome, salario From empregados Where salario >= 820`
  
[^2]: O programa inicia com o comportamento "On" ligado.

## Resultado:

### Input

```
Select id, nome, salario From empregados Where salario >= 820
```

### Output

```
LexToken(SELECT,'SELECT',1,0)
LexToken(IDENTIFIER,'id',1,7)
LexToken(COMMA,',',1,9)
LexToken(IDENTIFIER,'nome',1,11)
LexToken(COMMA,',',1,15)
LexToken(IDENTIFIER,'salario',1,17)
LexToken(FROM,'From',1,25)
LexToken(IDENTIFIER,'empregados',1,30)
LexToken(WHERE,'Where',1,41)
LexToken(IDENTIFIER,'salario',1,47)
LexToken(OPERATOR,'>=',1,55)
LexToken(NUMBER,'820',1,58)
```