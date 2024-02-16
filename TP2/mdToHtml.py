import re
import sys

html = """
<!DOCTYPE html>
<html>
<head>
    <title>TPC2 - PL2024</title>
    <meta charset="UTF-8"/>
</head>
<body>
"""

inOrderedList = False

def mdToHtml(line):
    global inOrderedList
    if line == "\n":
        line = "<p></p>"
        if inOrderedList:
            inOrderedList = False
            line = "\t</ol>\n" + "\t" + line
        return line
    headerMatch = re.match(r'^(#{1,3})\s*(.*)',line)
    if headerMatch:
        hastags, content = headerMatch.groups()
        level = len(hastags)
        return f"<h{level}>{mdToHtml(content.strip())}</h{level}>"

    orderedListMatch = re.match(r'[0-9]+\.\s+(.*)', line)
    if orderedListMatch:
        content = orderedListMatch.group(1)
        if not(inOrderedList):
            inOrderedList = True
            line = f"\t<ol>\n\t\t\t<li>{content}</li>"
        else:
            line = f"\t\t<li>{content}</li>"
    else:
        if inOrderedList:
            inOrderedList = False
            line = "\t</ol>\n" + line
    
    # Bold
    line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
    line = re.sub(r'__(.*?)__', r'<b>\1</b>', line)

    # Itálico
    line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', line)
    line = re.sub(r'_(.*?)_', r'<i>\1</i>', line)

    # imagem
    line = re.sub(r'!\[([^\]]+)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', line)

    # link
    line = re.sub(r'\[([^\]]+)\]\((.*?)\)', r'<a href="\2">\1</a>', line)

    return line


for line in sys.stdin:
    htmlLine = "\t" + mdToHtml(line)
    if not(htmlLine.endswith("\n")):
        htmlLine += "\n"
    html += htmlLine

html += "</body>\n</html>"

file = open("example.html", 'w', encoding="utf-8")
file.write(html)
file.close()