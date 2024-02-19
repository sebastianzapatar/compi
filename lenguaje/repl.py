from lenguaje.token import (
    Token,
    TokenType
)
from lenguaje.lexer import Lexer

def start_repl():
    print("Wellcome to lenguaje programming lenguage")
    while (source:=input(">>> ")) != "end":
        lexer = Lexer(source)
        while (token:=lexer.next_token()) != Token(TokenType.EOF, ""):
            print(token)