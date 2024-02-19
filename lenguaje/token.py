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
    EOF=auto()#nada
    ILLEGAL=auto()#?´~
    PLUS=auto()#+
    SEMICOLON=auto()#;
    """
    {
    }
    [
    ]
    -
    /
    (
    )
    ^
    !
    >
    <
    """
"""
Mostrar el token
"""
class Token(NamedTuple):
    token_type:TokenType
    literal:str

    def __str__(self) -> str:
        return f'{self.token_type.name}:{self.literal}'