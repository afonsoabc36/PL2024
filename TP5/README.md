# TP5: Máquina de Vending

## Compilar:
```
python3 vendingMachine.py
```

## Objetivo:
Construir um programa que simule uma máquina de vending.

## Exemplo:

```
maq: 2024-03-08, Stock carregado, Estado atualizado.
maq: Bom dia. Estou disponível para atender o seu pedido.
>> LISTAR
maq:
cod | nome | quantidade |  preço
---------------------------------
A23 água 0.5L 8 0.7
...
>> MOEDA 1e, 20c, 5c, 5c .
maq: Saldo = 1e30c
>> SELECIONAR A23
maq: Pode retirar o produto dispensado "água 0.5L"
maq: Saldo = 60c
>> SELECIONAR A23
maq: Saldo insufuciente para satisfazer o seu pedido
maq: Saldo = 60c; Pedido = 70c
>> ...
...
maq: Saldo = 74c
>> SAIR
maq: Pode retirar o troco: 1x 50c, 1x 20c e 2x 2c.
maq: Até à próxima
```

## Extras:

Adicionei as funcionalidades de alteração de preço/quantidade e a adição/remoção de um produto e um menu de ajuda.

```
>> ALTERARQ A29 4
maq: Quantidade alterada! Produto A29 com quantidade 4
>> ALTERARP A29 0.9
maq: Preço alterado! Produto A29 com preço 0.9e
>> ADICIONARP A31 "batatas fritas" 10 1.0
maq: Produto A31 adicionado com sucesso.
>> REMOVERP A31
maq: Produto A31 removido!
>> AJUDA
maq:
Ações possíveis:
LISTAR -> Mostra a lista de produtos disponíveis.
MOEDA (1e, 20c, 5c.) -> Carrega dinheiro na máquina.
SELECIONAR (A00) -> Seleciona um produto para compra.
SAIR -> Retira o troco.
Ações de Administrador:
ALTERARQ (A00 0) -> Altera a quantidade de um produto.
ALTERARP (A00 0.0) -> Alterar o preço de um produto.
ADICIONARP (COD "NOME" QUANT PRECO) -> Adiciona um novo produto à máquina.
REMOVERP (A00) -> Remove um produto da máquina.
```