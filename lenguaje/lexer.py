from re import match
from lenguaje.token import(
    Token,
    TokenType
)
"""
El lexer es le que identifica
cual token es y luego se pasa para generar el arbol
Y ser evaluado
"""
class Lexer:
    """
    Se inilizan las varialbes para utilizar en la clase
    """
    def __init__(self, source:str)->None:
        self._source = source
        self._current_pos = 0
        self._current_char = ""
        self._read_current_pos=0
        self._read_character()
    """
    Se asigna el token y se lee el siguiente caracter
    """
    def _read_character(self)->None:
        if self._read_current_pos >= len(self._source):
           self._current_char=""
        else:
            self._current_char = self._source[self._read_current_pos]
        self._current_pos =self._read_current_pos
        self._read_current_pos +=1
    """
    Para evitar espacios en blanco
    """
    def _skip_whitespace(self)->None:
        while self._current_char.isspace():
            self._read_character() 
    """
    Evalua cada token y devuelve su tipo
    """
    def next_token(self):
        
        self._skip_whitespace()
        if match(r'^=$', self._current_char):
            token = Token(TokenType.ASSIGN, self._current_char)
        elif match(r'^\+$', self._current_char):
            token = Token(TokenType.PLUS, self._current_char)
        elif match(r'^,$', self._current_char):
            token = Token(TokenType.COMMA, self._current_char)
        elif match(r'^;$', self._current_char):
            token = Token(TokenType.SEMICOLON, self._current_char)
        elif match(r'^$', self._current_char):
            token = Token(TokenType.EOF, self._current_char)
        else:
            token = Token(TokenType.ILLEGAL, self._current_char)
        self._read_character()
        return token