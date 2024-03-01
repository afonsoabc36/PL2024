# TP3: Somador on/off

## Compilar: [^1]
```
python3 somadorOnOff.py
```
```
python3 somadorOnOff.py < inputfile
```

[^1]: Se não for especificado o ficheiro de input o programa irá ler do stdin. Interromper a execução com Ctrl+D (EOF).

## Objetivo:
Pretende-se um programa que **some todas as sequências de dígitos** que encontre num texto:
- Sempre que encontrar a string “Off” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é desligado;
- Sempre que encontrar a string “On” em qualquer combinação de maiúsculas e minúsculas, esse comportamento é novamente ligado;[^2]
- Sempre que encontrar o caráter “=”, o resultado da soma é colocado na saída.
  
[^2]: O programa inicia com o comportamento "On" ligado.

## Resultado:

### Input

```
Iniciando a soma com 123 e 456 que dá um resultado =
oN agora somando 78 e 90 atualizando o resultado = parcial
OfF agora ignoramos 12 e 34 continuando com resultado = não diferente do anterior
ON somamos 56 ficando com resultado = oFf novamente ignoramos 78 
on finalizamos adicionando 9 e 3, ficando com o nosso resultado = final.
```

### Output

```
579
747
747
803
815
```

## Nota:
Assumi na realização deste trabalho que as palavras "On" e "Off" têm de aparecer por si só e não incluídas noutras palavras.[^3]
O mesmo não se verifica para os números e para o "=".


[^3]: A palavra "Afonso", embora contenha "On", não liga o comportamento de soma.