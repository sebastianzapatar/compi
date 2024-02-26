from enum import(
    Enum,
    auto,
    unique
)
from typing import(
    Dict,
    NamedTuple
)
"""
Se crea la clase TokenType para definir los tipos de tokens
Cada token es único y su identificador no se repite
"""
@unique
class TokenType(Enum):
    ASSIGN=auto()#=
    COMMA=auto()#,
    DIVISION=auto()
    DOUBLE = auto()
    ELSE=auto()
    EOF=auto()#nada
    EQ=auto()#==
    FALSE=auto()
    FUNCTION=auto()
    GT=auto()#>
    GTE=auto()#>=
    IDENT=auto()#identificador de una variable
    IF=auto()
    ILLEGAL=auto()#?´~
    INT=auto()#int
    LET=auto()#Let para asignar variables
    LT=auto()#<
    LTE=auto()#<=
    NOE=auto()#!=
    NOT=auto()#!
    PLUS=auto()#+
    RETURN= auto()
    SEMICOLON=auto()#;
    TRUE= auto()
class Token(NamedTuple):
    token_type:TokenType
    literal:str

    def __str__(self) -> str:
        return f'{self.token_type.name}:{self.literal}'
def lookup_token_type(literal:str)->TokenType:
    keywords:Dict[str,TokenType]={
        'false':TokenType.FALSE,
        'true':TokenType.TRUE,
        'function':TokenType.FUNCTION,
        'return':TokenType.RETURN,
        'if':TokenType.IF,
        'else':TokenType.ELSE,
        'let':TokenType.LET
    }
    return keywords.get(literal,TokenType.IDENT)