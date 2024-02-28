from enum import IntEnum

from typing import (
    Callable,
    Dict,
    List,
    Optional
)
from lenguaje.lexer import Lexer
from lenguaje.token import(
    Token,
    TokenType
)
"""
Mientras más grande sea el número se ejecuta de primero

el call a una función o parentesis se hace de primero
"""
class Precedence(IntEnum):
    LOWEST=1
    EQUALS=2
    LESSGREATER=3
    SUM=4
    PRODUCTO=5
    PREFIX=6
    CALL=7
"""
Se les asiga a los tokens la prioridad
"""
PRECEDNCES:Dict[TokenType,Precedence]={
    TokenType.EQ:Precedence.EQUALS,
    TokenType.NOE:Precedence.EQUALS,
    TokenType.LT:Precedence.LESSGREATER,
    TokenType.GT:Precedence.LESSGREATER,
    TokenType.PLUS:Precedence.SUM,
    TokenType.MINUS:Precedence.SUM,
    TokenType.MULTIPLICATION:Precedence.PRODUCTO,
    TokenType.LPAREN:Precedence.CALL
}

class Parser:

    def __init__(self,lexer:Lexer) -> None:
        self._lexer=lexer
        self._current_token:Optional[Token]=None
        self._peek_token:Optional[Token]=None
        self._errors:List[str]=[]

        self._advance_tokens()
        self._advance_tokens()

    
    def _advance_tokens(self)->None:
        self._current_token=self._peek_token
        self._peek_token=self._lexer.next_token()