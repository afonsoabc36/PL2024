import re
import sys

inOrderedList = False
inUnOrderedList = False

def mdToHtml(line):
    global inOrderedList, inUnOrderedList
    if line == "": # "\n" line after the strip()
        line = "<p></p>"
        if inOrderedList:
            inOrderedList = False
            line = "\t</ol>\n" + "\t" + line
        if inUnOrderedList:
            inUnOrderedList = False
            line = "\t</ul>\n" + "\t" + line
        return line
    
    # horizontal rule
    horizontalRuleMatch = re.match(r'^\s*(\*{3,}|-{3,}|_{3,})\s*$', line)
    if horizontalRuleMatch:
        return "<hr />"
    
    # Bold and italic text
    line = re.sub(r'\*\*\*(.*?)\*\*\*', r'<b><i>\1</i></b>', line)
    line = re.sub(r'___(.*?)___', r'<b><i>\1</i></b>', line)

    # Bold
    line = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', line)
    line = re.sub(r'__(.*?)__', r'<b>\1</b>', line)

    # Italic
    line = re.sub(r'\*(.*?)\*', r'<i>\1</i>', line)
    line = re.sub(r'_(.*?)_', r'<i>\1</i>', line)

    # imagem
    line = re.sub(r'!\[([^\]]+)\]\((.*?)\)', r'<img src="\2" alt="\1"/>', line)

    # link
    line = re.sub(r'\[([^\]]+)\]\((.*?)\)', r'<a href="\2">\1</a>', line)

    # code
    line = re.sub(r'`([^`]*)`', r'<code>\1</code>',line)

     # header
    headerMatch = re.match(r'^(#{1,3})\s*(.*)',line)
    if headerMatch:
        hastags, content = headerMatch.groups()
        level = len(hastags)
        return f"<h{level}>{content}</h{level}>"

    # ordered list
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

    # unordered list
    unorderedListMatch = re.match(r'-\s+(.*)', line)
    if unorderedListMatch:
        content = unorderedListMatch.group(1)
        if not(inUnOrderedList):
            inUnOrderedList = True
            line = f"\t<ul>\n\t\t\t<li>{content}</li>"
        else:
            line = f"\t\t<li>{content}</li>"
    else:
        if inUnOrderedList:
            inUnOrderedList = False
            line = "\t</ul>\n" + line

    # blockquote
    blockquoteMatch = re.match(r'^>\s*(.*)',line)
    if blockquoteMatch:
        content = blockquoteMatch.group(1)
        return f"<blockquote>{content}</blockquote>"

    return line

def suitableParagraphLine(line):
    return not re.search(r'(<h\d>|<li>|<ul>|<ol>|<p>|<hr|<img|<blockquote>|</h\d>|</li>|</ul>|</ol>|</p>|</img>|</blockquote>)', line.strip())

def main():
    outputFilename = "output.html"
    if len(sys.argv) > 1:
        outputFilename = sys.argv[1]

    html = f"""<!DOCTYPE html>
<html>
<head>
    <title>{outputFilename[:-5].capitalize()}</title>
    <meta charset="UTF-8"/>
</head>
<body>
"""

    for line in sys.stdin:
        htmlLine = mdToHtml(line.strip())

        if suitableParagraphLine(htmlLine):
            htmlLine = "<p>" + htmlLine + "</p>"
        
        # formatação
        htmlLine = "\t" + htmlLine + "\n"

        html += htmlLine

    html += "</body>\n</html>"

    file = open(outputFilename, 'w', encoding="utf-8")
    file.write(html)
    file.close()

if __name__ == "__main__":
    main()