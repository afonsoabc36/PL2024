import sys
import re

def processText(text, sum, openOn):
    partialSum = 0
    matches = re.findall(r'\d+|=',text) # Encontrar números e '='

    for match in matches:
        if match == "=":
            print(sum + partialSum)
        else:
            if openOn:
                partialSum += int(match)

    sum += partialSum
    return sum

def main():
    sum = 0
    openOn = False

    for line in sys.stdin:
        if openOn:
            offMatch = re.match(r'(.*)\s+off\s+', line)
            if offMatch:
                sum = processText(line, sum, openOn)
                openOn = False
            else:
                sum = processText(line, sum, openOn)
        else:
            fullMatch = re.match(r'.*\s+on\s+(.*?)\s+off\s+.*$', line)
            onMatch = re.match(r'.*\s+on\s+(.*)$',line)
            if fullMatch:
                openOn = True
                sum = processText(fullMatch.group(1), sum, openOn)
                openOn = False
            elif onMatch:
                openOn = True
                sum = processText(onMatch.group(1), sum, openOn)
            else: # elif
                sum = processText(line, sum, openOn)
    # match e retirar as strings dentro do on e do off
    # maybe findall mas pode não funcionar por ser linhas diferentes
    # if not openOn : try findall começa on acaba off, se for none começa match on(.) e fazer o parse auxiliar de \1
    # if openOn : try match (.*?)off
    # verificar se off ou \s+off\s+
    # parse das strings, retirar os números e os iguais em função auxiliar
    # passar como argumento um bool a dizer se está dentro de um on maybe
    # se encontrar um número junta à soma, se encontrar um igual dá print à soma
    # Maybe juntar tudo a uma lista e processar os números e prints por ordem no main
    # repetir e iterar por todas

if __name__ == '__main__':
    main()