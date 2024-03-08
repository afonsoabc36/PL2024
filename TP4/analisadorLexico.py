import ply.lex as lex

# Palavras reservadas para queries select do sql
reservedWords = {
    'select': 'SELECT',
    'from': 'FROM',
    'where': 'WHERE',
    'and': 'AND',
    'or': 'OR',
    'inner': 'INNER',
    'outer': 'OUTER',
    'like': 'LIKE',
    'full': 'FULL',
    'left': 'LEFT',
    'right': 'RIGHT',
    'on': 'ON',
    'join': 'JOIN',
    'group': 'GROUP',
    'by': 'BY',
    'having': 'HAVING',
    'union': 'UNION',
    'order': 'ORDER',
    'limit': 'LIMIT',
    'as': 'AS',
}

tokens = [
    'IDENTIFIER',
    'EVERYTHING',
    'COMMA',
    'NUMBER',
    'PERIOD',
    'OPERATOR',
    'LPAREN',
    'RPAREN',
    'SEMICOLON'
] + list(reservedWords.values())

t_COMMA = r'\,'
t_EVERYTHING = r'\*'
t_NUMBER = r'\d+'
t_PERIOD = r'\.'
t_OPERATOR = r'[+\-/=<>]+'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_SEMICOLON = r'\;'
t_ignore  = ' \t'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reservedWords.get(t.value.lower(), 'IDENTIFIER')  # Check for reserved words
    return t

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

data = "SELECT id, nome, salario From empregados Where salario >= 820"

lexer.input(data)

for token in lexer:
    print(token)