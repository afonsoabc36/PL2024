# TP2: Conversor de MD para HTML

## Compilar:
```python3 mdToHtml.py < input.md``` [^1]
```python3 mdToHtml.py output.html < input.md```

[^1]: Se não for especificado o nome do ficheiro de output o nome default é *output.html*

## Objetivo:
Criar em Python um pequeno conversor de MarkDown para HTML para os elementos descritos na "Basic Syntax" da [Cheat Sheet](https://www.markdownguide.org/cheat-sheet/).

## Resultado:

### Input

```
# Header 1
## Header 2
### Header 3

This is a paragraph with **bold**, *italic* and ***bold and italic*** text.

Here is an ordered list:
1. *First* item
2. **Second** item
3. ***Third*** item

Here is an unordered list:
- Item _one_
- Item __two__
- Item ___three___

> This is a blockquote.

`Inline Code`

---

Here is a [link](https://www.example.com).

![Image text](https://www.example.com/image.png)
```

### Output

```
<!DOCTYPE html>
<html>
<head>
    <title>Output</title>
    <meta charset="UTF-8"/>
</head>
<body>
	<h1>Header 1</h1>
	<h2>Header 2</h2>
	<h3>Header 3</h3>
	<p></p>
	<p>This is a paragraph with <b>bold</b>, <i>italic</i> and <b><i>bold and italic</i></b> text.</p>
	<p></p>
	<p>Here is an ordered list:</p>
		<ol>
			<li><i>First</i> item</li>
			<li><b>Second</b> item</li>
			<li><b><i>Third</i></b> item</li>
		</ol>
	<p></p>
	<p>Here is an unordered list:</p>
		<ul>
			<li>Item <i>one</i></li>
			<li>Item <b>two</b></li>
			<li>Item <b><i>three</i></b></li>
		</ul>
	<p></p>
	<blockquote>This is a blockquote.</blockquote>
	<p></p>
	<p><code>Inline Code</code></p>
	<p></p>
	<hr />
	<p></p>
	<p>Here is a <a href="https://www.example.com">link</a>.</p>
	<p></p>
	<img src="https://www.example.com/image.png" alt="Image text"/>
</body>
</html>
```