import json
import re
from datetime import date

stock = []
saldo = 0 # Em cêntimos

codProd = r'[A-Z]+[0-9]+'
preço = r'\d+(?:\.\d+)?'

listar = r'listar\s*'
moeda = r'moeda\s+(.*)$'
selecionar = fr'selecionar\s+({codProd})\s*$'
sair = r'sair\s*'
ajuda = r'ajuda\s*'
alterarQ = fr'alterarq\s+({codProd})\s+([0-9]+)$'
alterarP = fr'alterarp\s+({codProd})\s+({preço})$'
adicionarP = fr'adicionarp\s+({codProd})\s+("[a-zA-Z\s]+")\s+([0-9]+)\s+({preço})$'
removerP = fr'removerp\s+({codProd})\s*$'

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
    print("maq:")
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
            print(f"maq: Moeda inválida: {coin}")
    
    print("maq: Saldo = " + showMoney(saldo))

def selectItem(idProd):
    global saldo, stock
    found = False
    index = 0

    while index < len(stock) and not found:
        item = stock[index]
        
        if item['cod'] == idProd:
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
        print(f"maq: Produto {idProd} inexistente")

def alterQuant(idProd, newQuantity):
    global stock
    found = False
    index = 0

    while index < len(stock) and not found:
        item = stock[index]
        
        if item['cod'] == idProd:
            found = True
            item['quant'] = newQuantity
            print(f"maq: Quantidade alterada! Produto {item['cod']} com quantidade {item['quant']}")
        index += 1

    if not found:
        print(f"maq: Produto {idProd} inexistente")

def alterPrice(idProd, newPrice):
    global stock
    found = False
    index = 0

    while index < len(stock) and not found:
        item = stock[index]
        
        if item['cod'] == idProd:
            found = True
            item['preco'] = newPrice
            print(f"maq: Preço alterado! Produto {item['cod']} com preço {item['preco']}e")
        index += 1

    if not found:
        print(f"maq: Produto {idProd} inexistente")

def addProduct(cod, nome, quant, preco):
    global stock
    found = False
    index = 0
    prod = {
        "cod": cod,
        "nome": nome[1:-1],
        "quant": quant,
        "preco": preco
    }

    while index < len(stock) and not found:
        item = stock[index]
        if item['cod'] == cod:
            found = True
            print(f"maq: Produto com código {cod} já exite.")
        index += 1
    
    if not found:
        stock.append(prod)
        print(f"maq: Produto {cod} adicionado com sucesso.")

def removeProduct(cod):
    global stock
    found = False
    index = 0

    while index < len(stock) and not found:
        item = stock[index]
        if item['cod'] == cod:
            found = True
            del stock[index]
            print(f"maq: Produto {item['cod']} removido!")
        index += 1
    
    if not found:
        print(f"maq: Produto {cod} inexistente.")

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
    print("maq:")
    print("Ações possíveis:")
    print("LISTAR -> Mostra a lista de produtos disponíveis.")
    print("MOEDA (1e, 20c, 5c.) -> Carrega dinheiro na máquina.")
    print("SELECIONAR (A00) -> Seleciona um produto para compra.")
    print("SAIR -> Retira o troco.")
    print("Ações de Administrador:")
    print("ALTERARQ (A00 0) -> Altera a quantidade de um produto.")
    print("ALTERARP (A00 0.0) -> Alterar o preço de um produto.")
    print('ADICIONARP (COD "NOME" QUANT PRECO) -> Adiciona um novo produto à máquina.')
    print("REMOVERP (A00) -> Remove um produto da máquina.")


def main():
    if not loadStockFromFile():
        print("maq: Erro ao carregar o stock do ficheiro JSON.")
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
        elif match := re.match(alterarQ, text, re.I):
            alterQuant(match.group(1), match.group(2))
        elif match := re.match(alterarP, text, re.I):
            alterPrice(match.group(1), match.group(2))
        elif match := re.match(adicionarP, text, re.I):
            addProduct(match.group(1), match.group(2), match.group(3), match.group(4))
        elif match := re.match(removerP, text, re.I):
            removeProduct(match.group(1))
        elif re.match(ajuda, text, re.I):
            help()
        else:
            print("maq: Comando não disponível!\nmaq: Escreva 'AJUDA' para ver as ações possíveis!")

        text = input(">> ")

    leave()



if __name__ == "__main__":
    main()