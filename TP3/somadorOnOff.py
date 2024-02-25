import sys
import re

onlyOff = r'(.*?)\b[Oo][Ff]{2}\b' # linha que contém um 'off'
onlyOn = r'(.*?)\b[oO][nN]\b(.*)' # linha que contém um 'on'
onAndOff = r'\b[oO][nN]\b(.*?)\b[oO][fF]{2}\b' # linha que contém um 'on' seguido de um 'off'
multipleOn = r'\b[oO][nN]\b(?!.*\b[oO][nN]\b)(.*)' # linha com múltiplos 'on'


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


def onProcessing(line, sum, openOn):
    offMatch = re.match(onlyOff, line)

    if offMatch:
        sum = processText(offMatch.group(1), sum, openOn)
        openOn = False
        endIndex = offMatch.end()
        sum, openOn = notOnProcessing(line[endIndex:],sum, openOn)
    else:
        sum = processText(line, sum, openOn)
    
    return sum, openOn


def notOnProcessing(line, sum, openOn):
    fullMatchIter = re.finditer(onAndOff, line)
    onMatch = re.match(onlyOn,line)
    multipleOnMatches = re.findall(multipleOn, line)
    
    fullMatch = list(fullMatchIter)
    if fullMatch:
        index = 0
        for match in fullMatch:    
            startIndexMatch = match.start()
            if startIndexMatch != index:
                sum = processText(line[index:startIndexMatch], sum, openOn)
            openOn = True
            sum = processText(match.group(1), sum, openOn)
            openOn = False
            index = match.end()
        
        if multipleOnMatches and 'off' not in multipleOnMatches[-1].lower():
            openOn = True
            sum = processText(multipleOnMatches[-1], sum, openOn)

    elif onMatch: # and fullMatch is None
        openOn = True

        if onMatch.group(1) != "":
            sum = processText(onMatch.group(1), sum, openOn)
        
        sum = processText(onMatch.group(2), sum, openOn)
    
    else:
        sum = processText(line, sum, openOn)
    
    return sum, openOn


def main():
    sum = 0
    openOn = False

    for line in sys.stdin:
        if openOn:
            sum, openOn = onProcessing(line, sum, openOn)
        else:
            sum, openOn = notOnProcessing(line, sum, openOn)


if __name__ == '__main__':
    main()