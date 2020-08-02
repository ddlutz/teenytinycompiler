from lex import *

input = "IF+0123 foo123.432 *THEN/\"this is my string\"#comment me out\nWHILE"
#input = '"thisisaquote"'
lexer = Lexer(input)

tok = lexer.getToken()
while tok.kind != TokenType.EOF:
    print(str(tok.kind) + ":" + str(tok.text))
    tok = lexer.getToken()