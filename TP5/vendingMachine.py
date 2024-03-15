import json
import re
from datetime import date

stock = []
saldo = 0 # Em cêntimos

listar = r'listar\s*'
moeda = r'moeda\s+(.*)$'
selecionar = r'selecionar\s+([A-Z]+[0-9]+)$'
sair = r'sair\s*'
ajuda = r'ajuda\s*'


def showMoney(money):
    money = int(money)
    moneyString = ""
    if money / 100 >= 1:
        moneyString += str(int(money / 100)) + "e"
    
    moneyString += str(int(money % 100)) + "c"

    return moneyString

def loadStockFromFile():
    global stock
    try:
        with open("stock.json", "r") as stockFile:
            stock = json.load(stockFile)
            return True
    except:
        return False

def listItems():
    print("   cod   |   nome   |   quantidade   |   preço   ")
    print("-------------------------------------------------")
    for prod in stock:
        print(f"   {prod['cod']}   |   {prod['nome']}   |   {prod['quant']}   |   {prod['preco']}e")
        print("-------------------------------------------------")
    print("\n")

def loadMoney(group):
    global saldo
    coins = group.split(",")

    for coin in coins:
        if match := re.match(r'\s*([12])e', coin, re.I):
            saldo += int(match.group(1)) * 100
        elif match := re.match(r'\s*([125][0]|[521])c', coin, re.I):
            saldo += int(match.group(1))
        else:
            print(f"Moeda inválida: {coin}")
    
    print("maq: Saldo = " + showMoney(saldo))

def selectItem(group):
    global saldo, stock
    found = False
    index = 0

    while index < len(stock) and not found:
        item = stock[index]
        
        if item['cod'] == group:
            found = True
            if item['quant'] > 0:
                if item['preco'] <= saldo:
                    item['quant'] -= 1
                    saldo -= item['preco'] * 100
                    print(f'maq: Pode retirar o produto dispensado "{item["nome"]}"')
                    print(f"maq: Saldo = {showMoney(saldo)}")
                else:
                    print("maq: Saldo insufuciente para satisfazer o seu pedido")
                    print(f"maq: Saldo = {showMoney(saldo)}; Pedido = " + showMoney(item['preco']*100))
            else:
                print(f"maq: Produto {item['cod']} com stock insufuciente para satisfazer o seu pedido")
        
        index += 1

    if not found:
        print(f"maq: Produto {group} inexistente")

def troco():
    global saldo
    coins = {
        "2e" : 200,
        "1e" : 100,
        "50c" : 50,
        "20c" : 20,
        "10c" : 10,
        "5c" : 5,
        "2c" : 2,
        "1c" : 1
    }

    change = []

    for coin, value in coins.items():
        if saldo // value > 0:
            count = int(saldo // value)
            saldo -= count * value
            change.append(f"{count}x {coin}")

    if len(change) > 1:
        return ", ".join(change[:-1]) + " e " + change[-1] + "."
    elif change:
        return change[0]
    else:
        return "0c"

def leave():
    global saldo
    with open("stock.json", "w") as stock_file:
        json.dump(stock, stock_file, indent=4)
    print("maq: Pode retirar o troco: " + troco())
    print("maq: Até à próxima.")

def help():
    print("Ações possíveis:")
    print("LISTAR -> Mostra a lista de produtos disponíveis.")
    print("MOEDA (1e, 20c, 5c.) -> Carrega dinheiro na máquina.")
    print("SELECIONAR (A00) -> Seleciona um produto para compra.")
    print("SAIR -> Retira o troco.")


def main():
    if not loadStockFromFile():
        print("Erro ao carregar o stock do ficheiro JSON.")
        return
    print(f"maq: {date.today()}, Stock carregado, Estado atualizado.")
    print("maq: Bom dia. Estou disponível para atender o seu pedido.")

    text = input(">> ")
    while not re.match(sair, text, re.I):
        if re.match(listar, text, re.I):
            listItems()
        elif match := re.match(moeda, text, re.I):
            loadMoney(match.group(1))
        elif match := re.match(selecionar, text, re.I):
            selectItem(match.group(1))
        elif re.match(ajuda, text, re.I):
            help()
        else:
            print("Comando não disponível!\nEscreva 'AJUDA' para ver as ações possíveis!")

        text = input(">> ")

    leave()



if __name__ == "__main__":
    main()